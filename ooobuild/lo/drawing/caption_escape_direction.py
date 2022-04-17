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
# Namespace: com.sun.star.drawing


class CaptionEscapeDirection(object):
    """
    Const Class

    this flags describe escape direction for the line of a CaptionShape.

    See Also:
        `API CaptionEscapeDirection <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing_1_1CaptionEscapeDirection.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.CaptionEscapeDirection'
    __ooo_type_name__: str = 'const'

    horizontal = 0
    """
    the caption line leaves the caption area at the horizontal edge that is nearest to the caption point.
    """
    vertical = 1
    """
    the caption line leaves the caption area at the vertical edge that is nearest to the caption point.
    """
    auto = 2
    """
    the caption line leaves the caption area at the edge that is nearest to the caption point.
    """

__all__ = ['CaptionEscapeDirection']