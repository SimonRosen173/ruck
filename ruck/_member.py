#  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
#  MIT License
#
#  Copyright (c) 2021 Nathan Juraj Michlo
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

from typing import Any
from typing import List

import numpy as np


# ========================================================================= #
# Members                                                                   #
# ========================================================================= #


class MemberIsNotEvaluatedError(Exception):
    pass


class MemberAlreadyEvaluatedError(Exception):
    pass


class Member(object):

    def __init__(self, value: Any):
        self._value = value
        self._fitness = None

    @property
    def value(self) -> Any:
        return self._value

    @property
    def fitness(self):
        if not self.is_evaluated:
            raise MemberIsNotEvaluatedError('The member has not been evaluated, the fitness has not yet been set.')
        return self._fitness

    @fitness.setter
    def fitness(self, value):
        if self.is_evaluated:
            raise MemberAlreadyEvaluatedError('The member has already been evaluated, the fitness can only ever be set once. Create a new member instead!')
        if np.isnan(value):
            raise ValueError('fitness values cannot be NaN, this is an error!')
        self._fitness = value

    @property
    def is_evaluated(self) -> bool:
        return (self._fitness is not None)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        if self.is_evaluated:
            return f'{self.__class__.__name__}<{self.fitness}>'
        else:
            return f'{self.__class__.__name__}<>'


# ========================================================================= #
# Population                                                                #
# ========================================================================= #


PopulationHint  = List[Member]


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
