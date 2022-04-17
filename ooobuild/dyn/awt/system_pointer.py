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
# Namespace: com.sun.star.awt
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.awt import SystemPointer as SystemPointer
    if hasattr(SystemPointer, '_constants') and isinstance(SystemPointer._constants, dict):
        SystemPointer._constants['__ooo_ns__'] = 'com.sun.star.awt'
        SystemPointer._constants['__ooo_full_ns__'] = 'com.sun.star.awt.SystemPointer'
        SystemPointer._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global SystemPointerEnum
        ls = [f for f in dir(SystemPointer) if not callable(getattr(SystemPointer, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(SystemPointer, name)
        SystemPointerEnum = IntEnum('SystemPointerEnum', _dict)
    build_enum()
else:
    from ...lo.awt.system_pointer import SystemPointer as SystemPointer

    class SystemPointerEnum(IntEnum):
        """
        Enum of Const Class SystemPointer

        specifies the shape of a mouse pointer.
        """
        ARROW = SystemPointer.ARROW
        """
        specifies the normal arrow-like mouse pointer.
        """
        INVISIBLE = SystemPointer.INVISIBLE
        """
        specifies an invisible mouse pointer.
        """
        WAIT = SystemPointer.WAIT
        """
        specifies a waiting symbol as a mouse pointer (for example hourglass).
        """
        TEXT = SystemPointer.TEXT
        """
        specifies a mouse pointer for text (cursor-like).
        """
        HELP = SystemPointer.HELP
        """
        specifies a mouse pointer for on-line help.
        """
        CROSS = SystemPointer.CROSS
        """
        specifies a cross as a mouse pointer.
        """
        MOVE = SystemPointer.MOVE
        """
        specifies a mouse pointer which symbolizes movement.
        """
        NSIZE = SystemPointer.NSIZE
        """
        specifies a mouse pointer which symbolizes resizing for a top border.
        """
        SSIZE = SystemPointer.SSIZE
        """
        specifies a mouse pointer which symbolizes resizing for a bottom border.
        """
        WSIZE = SystemPointer.WSIZE
        """
        specifies a mouse pointer which symbolizes resizing for a left border.
        """
        ESIZE = SystemPointer.ESIZE
        """
        specifies a mouse pointer which symbolizes resizing for a right border.
        """
        NWSIZE = SystemPointer.NWSIZE
        """
        specifies a mouse pointer which symbolizes resizing for the top-left corner.
        """
        NESIZE = SystemPointer.NESIZE
        """
        specifies a mouse pointer which symbolizes resizing for the top-right corner.
        """
        SWSIZE = SystemPointer.SWSIZE
        """
        specifies a mouse pointer which symbolizes resizing for the bottom-left corner.
        """
        SESIZE = SystemPointer.SESIZE
        """
        specifies a mouse pointer which symbolizes resizing for the bottom-right corner.
        """
        WINDOW_NSIZE = SystemPointer.WINDOW_NSIZE
        """
        specifies a mouse pointer which symbolizes window resizing for a top border.
        """
        WINDOW_SSIZE = SystemPointer.WINDOW_SSIZE
        """
        specifies a mouse pointer which symbolizes window resizing for a bottom border.
        """
        WINDOW_WSIZE = SystemPointer.WINDOW_WSIZE
        """
        specifies a mouse pointer which symbolizes window resizing for a left border.
        """
        WINDOW_ESIZE = SystemPointer.WINDOW_ESIZE
        """
        specifies a mouse pointer which symbolizes window resizing for a right border.
        """
        WINDOW_NWSIZE = SystemPointer.WINDOW_NWSIZE
        """
        specifies a mouse pointer which symbolizes window resizing for the top-left corner.
        """
        WINDOW_NESIZE = SystemPointer.WINDOW_NESIZE
        """
        specifies a mouse pointer which symbolizes window resizing for the top-right corner.
        """
        WINDOW_SWSIZE = SystemPointer.WINDOW_SWSIZE
        """
        specifies a mouse pointer which symbolizes window resizing for the bottom-left corner.
        """
        WINDOW_SESIZE = SystemPointer.WINDOW_SESIZE
        """
        specifies a mouse pointer which symbolizes window resizing for the bottom-right corner.
        """
        HSPLIT = SystemPointer.HSPLIT
        """
        specifies a mouse pointer which symbolizes horizontal splitting.
        """
        VSPLIT = SystemPointer.VSPLIT
        """
        specifies a mouse pointer which symbolizes vertical splitting.
        """
        HSIZEBAR = SystemPointer.HSIZEBAR
        """
        specifies a mouse pointer which symbolizes horizontal resizing.
        """
        VSIZEBAR = SystemPointer.VSIZEBAR
        """
        specifies a mouse pointer which symbolizes vertical resizing.
        """
        HAND = SystemPointer.HAND
        """
        specifies a hand symbol as mouse pointer.
        """
        REFHAND = SystemPointer.REFHAND
        """
        specifies a pointing hand symbol as mouse pointer.
        """
        PEN = SystemPointer.PEN
        """
        specifies a pen symbol as mouse pointer.
        """
        MAGNIFY = SystemPointer.MAGNIFY
        """
        specifies a magnify symbol as mouse pointer.
        """
        FILL = SystemPointer.FILL
        """
        specifies a fill symbol as mouse pointer.
        """
        ROTATE = SystemPointer.ROTATE
        """
        specifies a rotate symbol as mouse pointer.
        """
        HSHEAR = SystemPointer.HSHEAR
        """
        specifies a horizontal shear symbol as mouse pointer.
        """
        VSHEAR = SystemPointer.VSHEAR
        """
        specifies a vertical shear symbol as mouse pointer.
        """
        MIRROR = SystemPointer.MIRROR
        """
        specifies a mirror symbol as mouse pointer.
        """
        CROOK = SystemPointer.CROOK
        """
        specifies a crook symbol as mouse pointer.
        """
        CROP = SystemPointer.CROP
        """
        specifies a crop symbol as mouse pointer.
        """
        MOVEPOINT = SystemPointer.MOVEPOINT
        """
        specifies a mouse pointer which symbolizes moving a point.
        """
        MOVEBEZIERWEIGHT = SystemPointer.MOVEBEZIERWEIGHT
        """
        specifies a mouse pointer which symbolizes moving a Bezier weight.
        """
        MOVEDATA = SystemPointer.MOVEDATA
        """
        specifies a mouse pointer which symbolizes moving data.
        """
        COPYDATA = SystemPointer.COPYDATA
        """
        specifies a mouse pointer which symbolizes copying data.
        """
        LINKDATA = SystemPointer.LINKDATA
        """
        specifies a mouse pointer which symbolizes linking data.
        """
        MOVEDATALINK = SystemPointer.MOVEDATALINK
        """
        specifies a mouse pointer which symbolizes moving a data link.
        """
        COPYDATALINK = SystemPointer.COPYDATALINK
        """
        specifies a mouse pointer which symbolizes copying a data link.
        """
        MOVEFILE = SystemPointer.MOVEFILE
        """
        specifies a mouse pointer which symbolizes moving a file.
        """
        COPYFILE = SystemPointer.COPYFILE
        """
        specifies a mouse pointer which symbolizes copying a file.
        """
        LINKFILE = SystemPointer.LINKFILE
        """
        specifies a mouse pointer which symbolizes linking a file.
        """
        MOVEFILELINK = SystemPointer.MOVEFILELINK
        """
        specifies a mouse pointer which symbolizes moving a file link.
        """
        COPYFILELINK = SystemPointer.COPYFILELINK
        """
        specifies a mouse pointer which symbolizes copying a file link.
        """
        MOVEFILES = SystemPointer.MOVEFILES
        """
        specifies a mouse pointer which symbolizes moving multiple files.
        """
        COPYFILES = SystemPointer.COPYFILES
        """
        specifies a mouse pointer which symbolizes copying multiple files.
        """
        NOTALLOWED = SystemPointer.NOTALLOWED
        """
        specifies a mouse pointer which symbolizes \"not allowed\".
        """
        DRAW_LINE = SystemPointer.DRAW_LINE
        """
        specifies a mouse pointer which symbolizes drawing a line.
        """
        DRAW_RECT = SystemPointer.DRAW_RECT
        """
        specifies a mouse pointer which symbolizes drawing a rectangle.
        """
        DRAW_POLYGON = SystemPointer.DRAW_POLYGON
        """
        specifies a mouse pointer which symbolizes drawing a polygon.
        """
        DRAW_BEZIER = SystemPointer.DRAW_BEZIER
        """
        specifies a mouse pointer which symbolizes drawing a Bezier.
        """
        DRAW_ARC = SystemPointer.DRAW_ARC
        """
        specifies a mouse pointer which symbolizes drawing an arc.
        """
        DRAW_PIE = SystemPointer.DRAW_PIE
        """
        specifies a mouse pointer which symbolizes drawing a pie.
        """
        DRAW_CIRCLECUT = SystemPointer.DRAW_CIRCLECUT
        """
        specifies a mouse pointer which symbolizes drawing a circle cut.
        """
        DRAW_ELLIPSE = SystemPointer.DRAW_ELLIPSE
        """
        specifies a mouse pointer which symbolizes drawing an ellipse.
        """
        DRAW_FREEHAND = SystemPointer.DRAW_FREEHAND
        """
        specifies a mouse pointer which symbolizes drawing free handed.
        """
        DRAW_CONNECT = SystemPointer.DRAW_CONNECT
        """
        specifies a mouse pointer which symbolizes drawing a connector.
        """
        DRAW_TEXT = SystemPointer.DRAW_TEXT
        """
        specifies a mouse pointer which symbolizes drawing text.
        """
        DRAW_CAPTION = SystemPointer.DRAW_CAPTION
        """
        specifies a mouse pointer which symbolizes drawing a text caption.
        """
        CHART = SystemPointer.CHART
        """
        specifies a mouse pointer which symbolizes a chart.
        """
        DETECTIVE = SystemPointer.DETECTIVE
        """
        specifies a mouse pointer which symbolizes a detective.
        """
        PIVOT_COL = SystemPointer.PIVOT_COL
        """
        specifies a mouse pointer which symbolizes a pivot column.
        """
        PIVOT_ROW = SystemPointer.PIVOT_ROW
        """
        specifies a mouse pointer which symbolizes a pivot row.
        """
        PIVOT_FIELD = SystemPointer.PIVOT_FIELD
        """
        specifies a mouse pointer which symbolizes a pivot field.
        """
        CHAIN = SystemPointer.CHAIN
        """
        specifies a mouse pointer which symbolizes a chain.
        """
        CHAIN_NOTALLOWED = SystemPointer.CHAIN_NOTALLOWED
        """
        specifies a mouse pointer which symbolizes \"chaining not allowed\".
        """

__all__ = ['SystemPointer', 'SystemPointerEnum']