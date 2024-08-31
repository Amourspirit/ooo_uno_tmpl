# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.animations
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class TransitionSubType(metaclass=UnoConstMeta, type_name="com.sun.star.animations.TransitionSubType", name_space="com.sun.star.animations"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.animations.TransitionSubType``"""
        pass

    class TransitionSubTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.animations.TransitionSubType", name_space="com.sun.star.animations"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.animations.TransitionSubType`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.animations import TransitionSubType as TransitionSubType
    else:
        # keep document generators happy
        from ...lo.animations.transition_sub_type import TransitionSubType as TransitionSubType

    class TransitionSubTypeEnum(IntEnum):
        """
        Enum of Const Class TransitionSubType

        """
        DEFAULT = TransitionSubType.DEFAULT
        LEFTTORIGHT = TransitionSubType.LEFTTORIGHT
        TOPTOBOTTOM = TransitionSubType.TOPTOBOTTOM
        TOPLEFT = TransitionSubType.TOPLEFT
        TOPRIGHT = TransitionSubType.TOPRIGHT
        BOTTOMRIGHT = TransitionSubType.BOTTOMRIGHT
        BOTTOMLEFT = TransitionSubType.BOTTOMLEFT
        TOPCENTER = TransitionSubType.TOPCENTER
        RIGHTCENTER = TransitionSubType.RIGHTCENTER
        BOTTOMCENTER = TransitionSubType.BOTTOMCENTER
        LEFTCENTER = TransitionSubType.LEFTCENTER
        CORNERSIN = TransitionSubType.CORNERSIN
        CORNERSOUT = TransitionSubType.CORNERSOUT
        VERTICAL = TransitionSubType.VERTICAL
        HORIZONTAL = TransitionSubType.HORIZONTAL
        DIAGONALBOTTOMLEFT = TransitionSubType.DIAGONALBOTTOMLEFT
        DIAGONALTOPLEFT = TransitionSubType.DIAGONALTOPLEFT
        DOUBLEBARNDOOR = TransitionSubType.DOUBLEBARNDOOR
        DOUBLEDIAMOND = TransitionSubType.DOUBLEDIAMOND
        DOWN = TransitionSubType.DOWN
        LEFT = TransitionSubType.LEFT
        UP = TransitionSubType.UP
        RIGHT = TransitionSubType.RIGHT
        RECTANGLE = TransitionSubType.RECTANGLE
        DIAMOND = TransitionSubType.DIAMOND
        CIRCLE = TransitionSubType.CIRCLE
        FOURPOINT = TransitionSubType.FOURPOINT
        FIVEPOINT = TransitionSubType.FIVEPOINT
        SIXPOINT = TransitionSubType.SIXPOINT
        HEART = TransitionSubType.HEART
        KEYHOLE = TransitionSubType.KEYHOLE
        CLOCKWISETWELVE = TransitionSubType.CLOCKWISETWELVE
        CLOCKWISETHREE = TransitionSubType.CLOCKWISETHREE
        CLOCKWISESIX = TransitionSubType.CLOCKWISESIX
        CLOCKWISENINE = TransitionSubType.CLOCKWISENINE
        TWOBLADEVERTICAL = TransitionSubType.TWOBLADEVERTICAL
        TWOBLADEHORIZONTAL = TransitionSubType.TWOBLADEHORIZONTAL
        FOURBLADE = TransitionSubType.FOURBLADE
        CLOCKWISETOP = TransitionSubType.CLOCKWISETOP
        CLOCKWISERIGHT = TransitionSubType.CLOCKWISERIGHT
        CLOCKWISEBOTTOM = TransitionSubType.CLOCKWISEBOTTOM
        CLOCKWISELEFT = TransitionSubType.CLOCKWISELEFT
        CLOCKWISETOPLEFT = TransitionSubType.CLOCKWISETOPLEFT
        COUNTERCLOCKWISEBOTTOMLEFT = TransitionSubType.COUNTERCLOCKWISEBOTTOMLEFT
        CLOCKWISEBOTTOMRIGHT = TransitionSubType.CLOCKWISEBOTTOMRIGHT
        COUNTERCLOCKWISETOPRIGHT = TransitionSubType.COUNTERCLOCKWISETOPRIGHT
        CENTERTOP = TransitionSubType.CENTERTOP
        CENTERRIGHT = TransitionSubType.CENTERRIGHT
        TOP = TransitionSubType.TOP
        BOTTOM = TransitionSubType.BOTTOM
        FANOUTVERTICAL = TransitionSubType.FANOUTVERTICAL
        FANOUTHORIZONTAL = TransitionSubType.FANOUTHORIZONTAL
        FANINVERTICAL = TransitionSubType.FANINVERTICAL
        FANINHORIZONTAL = TransitionSubType.FANINHORIZONTAL
        PARALLELVERTICAL = TransitionSubType.PARALLELVERTICAL
        PARALLELDIAGONAL = TransitionSubType.PARALLELDIAGONAL
        OPPOSITEVERTICAL = TransitionSubType.OPPOSITEVERTICAL
        OPPOSITEHORIZONTAL = TransitionSubType.OPPOSITEHORIZONTAL
        PARALLELDIAGONALTOPLEFT = TransitionSubType.PARALLELDIAGONALTOPLEFT
        PARALLELDIAGONALBOTTOMLEFT = TransitionSubType.PARALLELDIAGONALBOTTOMLEFT
        TOPLEFTHORIZONTAL = TransitionSubType.TOPLEFTHORIZONTAL
        TOPLEFTDIAGONAL = TransitionSubType.TOPLEFTDIAGONAL
        TOPRIGHTDIAGONAL = TransitionSubType.TOPRIGHTDIAGONAL
        BOTTOMRIGHTDIAGONAL = TransitionSubType.BOTTOMRIGHTDIAGONAL
        BOTTOMLEFTDIAGONAL = TransitionSubType.BOTTOMLEFTDIAGONAL
        TOPLEFTCLOCKWISE = TransitionSubType.TOPLEFTCLOCKWISE
        TOPRIGHTCLOCKWISE = TransitionSubType.TOPRIGHTCLOCKWISE
        BOTTOMRIGHTCLOCKWISE = TransitionSubType.BOTTOMRIGHTCLOCKWISE
        BOTTOMLEFTCLOCKWISE = TransitionSubType.BOTTOMLEFTCLOCKWISE
        TOPLEFTCOUNTERCLOCKWISE = TransitionSubType.TOPLEFTCOUNTERCLOCKWISE
        TOPRIGHTCOUNTERCLOCKWISE = TransitionSubType.TOPRIGHTCOUNTERCLOCKWISE
        BOTTOMRIGHTCOUNTERCLOCKWISE = TransitionSubType.BOTTOMRIGHTCOUNTERCLOCKWISE
        BOTTOMLEFTCOUNTERCLOCKWISE = TransitionSubType.BOTTOMLEFTCOUNTERCLOCKWISE
        VERTICALTOPSAME = TransitionSubType.VERTICALTOPSAME
        VERTICALBOTTOMSAME = TransitionSubType.VERTICALBOTTOMSAME
        VERTICALTOPLEFTOPPOSITE = TransitionSubType.VERTICALTOPLEFTOPPOSITE
        VERTICALBOTTOMLEFTOPPOSITE = TransitionSubType.VERTICALBOTTOMLEFTOPPOSITE
        HORIZONTALLEFTSAME = TransitionSubType.HORIZONTALLEFTSAME
        HORIZONTALRIGHTSAME = TransitionSubType.HORIZONTALRIGHTSAME
        HORIZONTALTOPLEFTOPPOSITE = TransitionSubType.HORIZONTALTOPLEFTOPPOSITE
        HORIZONTALTOPRIGHTOPPOSITE = TransitionSubType.HORIZONTALTOPRIGHTOPPOSITE
        DIAGONALBOTTOMLEFTOPPOSITE = TransitionSubType.DIAGONALBOTTOMLEFTOPPOSITE
        DIAGONALTOPLEFTOPPOSITE = TransitionSubType.DIAGONALTOPLEFTOPPOSITE
        TWOBOXTOP = TransitionSubType.TWOBOXTOP
        TWOBOXBOTTOM = TransitionSubType.TWOBOXBOTTOM
        TWOBOXLEFT = TransitionSubType.TWOBOXLEFT
        TWOBOXRIGHT = TransitionSubType.TWOBOXRIGHT
        FOURBOXVERTICAL = TransitionSubType.FOURBOXVERTICAL
        FOURBOXHORIZONTAL = TransitionSubType.FOURBOXHORIZONTAL
        VERTICALLEFT = TransitionSubType.VERTICALLEFT
        VERTICALRIGHT = TransitionSubType.VERTICALRIGHT
        HORIZONTALLEFT = TransitionSubType.HORIZONTALLEFT
        HORIZONTALRIGHT = TransitionSubType.HORIZONTALRIGHT
        FROMLEFT = TransitionSubType.FROMLEFT
        FROMTOP = TransitionSubType.FROMTOP
        FROMRIGHT = TransitionSubType.FROMRIGHT
        FROMBOTTOM = TransitionSubType.FROMBOTTOM
        CROSSFADE = TransitionSubType.CROSSFADE
        FADETOCOLOR = TransitionSubType.FADETOCOLOR
        FADEFROMCOLOR = TransitionSubType.FADEFROMCOLOR
        FADEOVERCOLOR = TransitionSubType.FADEOVERCOLOR
        THREEBLADE = TransitionSubType.THREEBLADE
        EIGHTBLADE = TransitionSubType.EIGHTBLADE
        ONEBLADE = TransitionSubType.ONEBLADE
        ACROSS = TransitionSubType.ACROSS
        TOPLEFTVERTICAL = TransitionSubType.TOPLEFTVERTICAL
        COMBHORIZONTAL = TransitionSubType.COMBHORIZONTAL
        COMBVERTICAL = TransitionSubType.COMBVERTICAL
        IN = TransitionSubType.IN
        OUT = TransitionSubType.OUT
        ROTATEIN = TransitionSubType.ROTATEIN
        ROTATEOUT = TransitionSubType.ROTATEOUT
        FROMTOPLEFT = TransitionSubType.FROMTOPLEFT
        FROMTOPRIGHT = TransitionSubType.FROMTOPRIGHT
        FROMBOTTOMLEFT = TransitionSubType.FROMBOTTOMLEFT
        FROMBOTTOMRIGHT = TransitionSubType.FROMBOTTOMRIGHT

__all__ = ['TransitionSubType', 'TransitionSubTypeEnum']
