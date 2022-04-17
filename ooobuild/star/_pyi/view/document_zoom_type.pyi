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
# Namespace: com.sun.star.view
from typing_extensions import Literal


class DocumentZoomType:
    """
    Const Class

    These constants specify how the document content is zoomed into the document view.

    See Also:
        `API DocumentZoomType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1view_1_1DocumentZoomType.html>`_
    """
    OPTIMAL: Literal[0]
    """
    The page content width (excluding margins) at the current selection is fit into the view.
    """
    PAGE_WIDTH: Literal[1]
    """
    The page width at the current selection is fit into the view.
    """
    ENTIRE_PAGE: Literal[2]
    """
    A complete page of the document is fit into the view.
    """
    BY_VALUE: Literal[3]
    """
    The zoom is relative and is to be set via the property ViewSettings.ZoomValue.
    """
    PAGE_WIDTH_EXACT: Literal[4]
    """
    The page width at the current selection is fit into the view, with the view ends exactly at the end of the page.
    """

