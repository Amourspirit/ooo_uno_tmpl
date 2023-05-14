# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sheet


class FormulaMapGroupSpecialOffset(object):
    """
    Const Class

    Constants designating the offsets within the sequence returned by XFormulaOpCodeMapper.getAvailableMappings() when called for group FormulaMapGroup.SPECIAL.
    
    The number of constants may grow in future versions!
    
    **since**
    
        LibreOffice 7.3

    See Also:
        `API FormulaMapGroupSpecialOffset <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1FormulaMapGroupSpecialOffset.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.FormulaMapGroupSpecialOffset'
    __ooo_type_name__: str = 'const'

    PUSH = 0
    """
    Formula tokens containing the op-code obtained from this offset describe a formula operand token that will be pushed onto the formula stack while the formula is interpreted.
    
    The FormulaToken.Data member shall contain one of the following values:
    """
    CALL = 1
    STOP = 2
    """
    Formula tokens containing the op-code obtained from this offset instruct the formula interpreter to immediately stop interpreting the formula.
    
    The FormulaToken.Data member is not used and should be empty.
    """
    EXTERNAL = 3
    """
    Formula tokens containing the op-code obtained from this offset describe the reference to an external function (e.g.
    
    add-in function) used in formulas.
    
    The FormulaToken.Data member shall contain a string with the programmatic name of the function, e.g. \"com.sun.star.sheet.addin.Analysis.getEomonth\" for the EOMONTH function from the Analysis add-in.
    """
    NAME = 4
    """
    Formula tokens containing the op-code obtained from this offset describe the reference to a defined name (also known as named range) used in formulas.
    
    The FormulaToken.Data member shall contain an integer value of type long specifying the index of the defined name. This index can be obtained from the defined name using its NamedRange.TokenIndex property.
    """
    NO_NAME = 5
    """
    Formula tokens containing the op-code obtained from this offset describe an invalid name that resolves to the NAME? error in formulas.
    
    The FormulaToken.Data member is not used and should be empty.
    """
    MISSING = 6
    """
    Formula tokens containing the op-code obtained from this offset describe an empty function parameter.
    
    Example: In the formula =SUM(1;;2) the second parameter is empty and represented by a formula token containing the \"missing\" op-code.
    
    The FormulaToken.Data member is not used and should be empty.
    """
    BAD = 7
    """
    Formula tokens containing the op-code obtained from this offset describe \"bad\" data in a formula, e.g.
    
    data the formula parser was not able to parse.
    
    The FormulaToken.Data member shall contain a string with the bad data. This string will be displayed literally in the formula.
    """
    SPACES = 8
    """
    Formula tokens containing the op-code obtained from this offset describe whitespace characters within the string representation of a formula.
    
    Whitespace characters in formulas are used for readability and do not affect the result of the formula.
    
    The FormulaToken.Data member shall contain a positive integer value of type long specifying the number of space characters.
    """
    MAT_REF = 9
    DB_AREA = 10
    """
    Formula tokens containing the op-code obtained from this offset describe the reference to a database range used in formulas.
    
    The FormulaToken.Data member shall contain an integer value of type long specifying the index of the database range. This index can be obtained from the database range using its DatabaseRange.TokenIndex property.
    """
    MACRO = 11
    """
    Formula tokens containing the op-code obtained from this offset describe the reference to a macro function called in a formula.
    
    The FormulaToken.Data member shall contain a string specifying the name of the macro function.
    """
    COL_ROW_NAME = 12
    WHITESPACE = 13
    """
    Formula tokens containing the op-code obtained from this offset describe whitespace characters within the string representation of a formula.
    
    Whitespace characters in formulas are used for readability and do not affect the result of the formula.
    
    The FormulaToken.Data member shall contain a string of one (repeated) whitespace character. The length of the string determines the number of repetitions.
    
    Allowed whitespace characters are SPACE (U+0020), CHARACTER TABULATION (U+0009), LINE FEED (U+000A), and CARRIAGE RETURN (U+000D). See also ODF v1.3 OpenFormula 5.14 Whitespace.
    
    **since**
    
        LibreOffice 7.3
    """

__all__ = ['FormulaMapGroupSpecialOffset']
