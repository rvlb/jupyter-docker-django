# Decorator

import logging
from contextlib import ContextDecorator

from django.conf import settings
from django.db import DEFAULT_DB_ALIAS, connections


logger = logging.getLogger(__name__)


class QueryCountExceededException(Exception):
    pass


class max_query_count(ContextDecorator):  # noqa
    def __init__(
        self,
        *,
        max_queries=0,
        logger=logger,
        using=DEFAULT_DB_ALIAS,
        force_suppress_exception=False,
    ):
        self._max_queries = max_queries
        self._queries_before = 0
        self._queries_after = 0
        # This is a way to allow developers to suppress a N+1 exception in development
        self._force_suppress_exception = force_suppress_exception
        # These are for ensuring this will correctly work when DEBUG=False
        self._conn = connections[using]
        self._force_debug_cursor = None
        self.logger = logger

    def __enter__(self):
        self._force_debug_cursor = self._conn.force_debug_cursor
        self._conn.force_debug_cursor = True
        self._queries_before = len(self._conn.queries)
        return self

    def __exit__(self, *exc):
        self._queries_after = len(self._conn.queries)
        actual_queries = self._queries_after - self._queries_before
        self._conn.force_debug_cursor = self._force_debug_cursor
        if self._force_suppress_exception:
            return False

        if self._should_raise_exception():
            self._forbid_unoptimized_query(actual_queries, self._max_queries)
        else:
            try:
                self._forbid_unoptimized_query(actual_queries, self._max_queries)
            except QueryCountExceededException:
                logger.error(
                    "Exceeded expected queries, expected=%d, actual=%d",
                    self._max_queries,
                    actual_queries,
                    exc_info=True,
                )
            return False

    # Extracted into methods to make them easier to mock in the tests
    def _forbid_unoptimized_query(self, actual_queries, max_queries):
        if self._has_unoptimized_query(actual_queries, max_queries):
            raise QueryCountExceededException(
                f"Exceeded expected queries, expected={self._max_queries}, actual={actual_queries}"
            )

    def _has_unoptimized_query(self, actual_queries, max_queries):
        return actual_queries > max_queries

    def _should_raise_exception(self):
        return settings.DEBUG
