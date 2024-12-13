"""A module implementing the basic functionality of mathematical groups.

This version of the module uses inheritance.
"""

import numpy as np
from numbers import Integral
from example_code.groups import Group


class SymmetricGroup(Group):
    """A symmetric group over n values."""

    symbol = "S"

    def _validate(self, value):
        """Ensure that value is an allowed element value in this group."""
        # if (isinstance(value, str)):
        #    raise ValueError("Element value must be a permutation of"
        #                     f"integers in the range [0, {self.n})")
        if not (isinstance(value.dtype, Integral)
                and sorted(np.ndarray(value).shape)
                == [i for i in np.arange(self.n)]):
            raise ValueError("Element value must be a permutation of "
                             f"integers in the range [0, {self.n})")

    def operation(self, a, b):
        """Perform the group operation on two values.

        The group operation is  the composition a(b).
        """
        return a[b]
