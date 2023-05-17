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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class PosSize(object):
    """
    Const

    These constants are used to flag the parameters of a rectangle.

    See Also:
        `API PosSize <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1PosSize.html>`_
    """
    X: Literal[1]
    """
    flags the x-coordinate.
    """
    Y: Literal[2]
    """
    flags the y-coordinate.
    """
    WIDTH: Literal[4]
    """
    flags the width.
    """
    HEIGHT: Literal[8]
    """
    flags the height.
    """
    POS: Literal[3]
    """
    flags the x- and y-coordinate.
    """
    SIZE: Literal[12]
    """
    flags the width and height.
    """
    POSSIZE: Literal[15]
    """
    flags the x- and y-coordinate, width and height.
    """

