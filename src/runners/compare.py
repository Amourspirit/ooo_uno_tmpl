# coding: utf-8
# region Imports
import os
from kwhelp import rules
from kwhelp.decorator import DecFuncEnum, RuleCheckAll
from enum import IntEnum
# endregion Imports

# region Compare


class CompareEnum(IntEnum):
    Before = -1
    Equal = 0
    After = 1


class CompareFile:

    @staticmethod
    @RuleCheckAll(rules.RulePathExist, ftype=DecFuncEnum.METHOD_STATIC)
    def compare(file1, file2) -> CompareEnum:
        time1 = os.path.getmtime(file1)
        time2 = os.path.getmtime(file2)
        if time1 < time2:
            return CompareEnum.Before
        if time1 > time2:
            return CompareEnum.After
        return CompareEnum.Equal

# endregion Compare
