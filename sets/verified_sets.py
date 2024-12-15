"""A module implementing the basic functionality of a verified set.

This version of the module uses inheritance.
"""

from numbers import Integral


class VerifiedSet(set):
    """A parent of other classes which have particular verification rules."""

    symbol = 'VS'

    def __init__(self, new_set):
        """Initialise object."""
        if self.symbol == 'VS':
            raise NotImplementedError
        else:
            super().__init__(new_set)

    def _verify(self, value):
        """Ensure that value is an allowed element value in this group."""
        raise NotImplementedError

    def add(self, value):
        """Add element to set."""
        self._verify(value)
        return super().add(value)

    def update(self, values):
        """Update set with new set."""
        for value in values:
            self._verify(value)
        return super().update(values)

    def symmetric_difference_update(self, values):
        """Update set and delete duplicates with new set."""
        for value in values:
            self._verify(value)
        return super().symmetric_difference_update(values)


class IntSet(VerifiedSet):
    """Only integers are allowed."""

    symbol = 'IS'

    def __init__(self, new_set):
        """Initialise IntSet object."""
        super().__init__(new_set)

    def _verify(self, value):
        """Ensure that value is an integer in this group."""
        if not isinstance(value, Integral):
            raise TypeError(f"IntSet expected an integer, \
                got a {type(value).__name__}.")

    def add(self, value):
        """Add element to set."""
        return super().add(value)

    def update(self, values):
        """Update set with new set."""
        return super().update(values)

    def symmetric_difference_update(self, values):
        """Update set and delete duplicates with new set."""
        return super().symmetric_difference_update(values)
