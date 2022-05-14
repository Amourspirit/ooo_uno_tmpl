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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.text
from typing_extensions import Literal


class FootnoteNumbering(object):
    """
    Const

    These constants are used to specify the footnote numbering.

    See Also:
        `API FootnoteNumbering <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1FootnoteNumbering.html>`_
    """
    PER_PAGE: Literal[0]
    """
    The counter of the automatic footnote numbering restarts each page.
    """
    PER_CHAPTER: Literal[1]
    """
    The counter of the automatic footnote numbering restarts each chapter.
    """
    PER_DOCUMENT: Literal[2]
    """
    The counter of the automatic footnote numbering does not restart.
    """

