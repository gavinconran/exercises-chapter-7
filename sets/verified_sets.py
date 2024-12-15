"""A module implementing the basic functionality of a verified set.

This version of the module uses inheritance.
"""

import numpy as np
from numbers import Integral


class VerifiedSet(set):
    """A parent of other classes which have particular verification rules."""

    def _verify(self, value):
        """Ensure that value is an allowed element value in this group."""
        raise NotImplementedError

    def add(self, value):
        self._verify(value)
        return super().add(value)

    def update(self, values):
        for value in values:
            self._verify(value)
        return super().update(values)

    def symmetric_difference_update(self, values):
        for value in values:
            self._verify(value)
        return super().symmetric_difference_update(values)        


class IntSet(VerifiedSet):
    """Only integers are allowed"""

    def _verify(self, value):
        if not isinstance(value, Integral): 
            raise TypeError(f"IntSet expected an integer, got a {type(value).__name__}.")

    def add(self, value):
        return super().add(value)

    def update(self, values):
        return super().update(values)

    def symmetric_difference_update(self, values):
        return super().symmetric_difference_update(values)
