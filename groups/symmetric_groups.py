"""A module implementing the basic functionality of mathematical groups.

This version of the module uses inheritance.
"""

from numbers import Integral
import numpy as np
from example_code.groups import Group


class SymmetricGroup(Group):
    """A symmetric group over n values."""

    symbol = "S"

    def _validate(self, value):
        """Ensure that value is an allowed element value in this group."""
        value = np.ndarray(value)
        if not (sorted(value.shape) == [i for i in np.arange(self.n)]): 
            raise ValueError("Element value must be a permutation of integers"
                             f" in the range [0, {self.n})")

    def operation(self, a, b):
        """Perform the group operation on two values.

        The group operation is  the composition a(b).
        """
        return a[b]
