# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.3
# Namespace: com.sun.star.table


class BorderLineStyle(object):
    """
    Const Class


    See Also:
        `API BorderLineStyle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1table_1_1BorderLineStyle.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.table'
    __ooo_full_ns__: str = 'com.sun.star.table.BorderLineStyle'
    __ooo_type_name__: str = 'const'

    NONE = 32767
    """
    No border line.
    """
    SOLID = 0
    """
    Solid border line.
    """
    DOTTED = 1
    """
    Dotted border line.
    """
    DASHED = 2
    """
    Dashed border line.
    """
    DOUBLE = 3
    """
    Double border line.
    
    Widths of the lines and the gap are all equal, and vary equally with the total width.
    """
    THINTHICK_SMALLGAP = 4
    """
    Double border line with a thin line outside and a thick line inside separated by a small gap.
    """
    THINTHICK_MEDIUMGAP = 5
    """
    Double border line with a thin line outside and a thick line inside separated by a medium gap.
    """
    THINTHICK_LARGEGAP = 6
    """
    Double border line with a thin line outside and a thick line inside separated by a large gap.
    """
    THICKTHIN_SMALLGAP = 7
    """
    Double border line with a thick line outside and a thin line inside separated by a small gap.
    """
    THICKTHIN_MEDIUMGAP = 8
    """
    Double border line with a thick line outside and a thin line inside separated by a medium gap.
    """
    THICKTHIN_LARGEGAP = 9
    """
    Double border line with a thick line outside and a thin line inside separated by a large gap.
    """
    EMBOSSED = 10
    """
    3D embossed border line.
    """
    ENGRAVED = 11
    """
    3D engraved border line.
    """
    OUTSET = 12
    """
    Outset border line.
    """
    INSET = 13
    """
    Inset border line.
    """
    FINE_DASHED = 14
    """
    Finely dashed border line.
    """
    DOUBLE_THIN = 15
    """
    Double border line consisting of two fixed thin lines separated by a variable gap.
    """
    DASH_DOT = 16
    """
    Line consisting of a repetition of one dash and one dot.
    """
    DASH_DOT_DOT = 17
    """
    Line consisting of a repetition of one dash and 2 dots.
    """
    BORDER_LINE_STYLE_MAX = 17
    """
    Maximum valid border line style value.
    """

__all__ = ['BorderLineStyle']
