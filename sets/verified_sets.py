"""A module implementing the basic functionality of a verified set.

This version of the module uses inheritance.
"""

# all tests passed
from numbers import Integral


class UniquenessError(KeyError):
    """Exception Class."""

    pass


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

    def union(self, other):
        """Create a newset of self union other."""
        for item in other:
            self._verify(item)
        return super().union(other)

    def intersection(self, other):
        """Create a newset of self intersect other."""
        for item in other:
            self._verify(item)
        return super().intersection(other)

    def difference(self, other):
        """Return set containing items only existing in set x, not set y."""
        for item in other:
            self._verify(item)
        return super().difference(other)

    def symmetric_difference(self, other):
        """Return set of items in both sets, except those present in both."""
        for item in other:
            self._verify(item)
        return super().symmetric_difference(other)

    def copy(self):
        """Return a deep copy of self."""
        return super().copy()


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

    def union(self, other):
        """Create a newset of self union other."""
        return IntSet(super().union(other))

    def intersection(self, other):
        """Create a newset of self intersect other."""
        return IntSet(super().intersection(other))

    def difference(self, other):
        """Return set containing items only existing in set x, not set y."""
        for item in other:
            self._verify(item)
        return IntSet(super().difference(other))

    def symmetric_difference(self, other):
        """Return set of items in both sets, except those present in both."""
        return IntSet(super().symmetric_difference(other))

    def copy(self):
        """Return a deep copy of self."""
        return IntSet(super().copy())


class UniqueSet(VerifiedSet):
    """Only values not in set can be added."""

    symbol = 'QS'

    def __init__(self, new_set):
        """Initialise UniqueSet object."""
        super().__init__(new_set)

    def _verify(self, value):
        """Ensure that value is an integer in this group."""
        if not isinstance(value, Integral):
            raise TypeError(f"IntSet expected an integer, \
                got a {type(value).__name__}.")
        if value in self:
            raise UniquenessError
