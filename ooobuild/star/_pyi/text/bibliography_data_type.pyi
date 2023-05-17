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
# Namespace: com.sun.star.text
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class BibliographyDataType(object):
    """
    Const

    These values define the type of bibliographic data like book, journal, magazine, etc.

    See Also:
        `API BibliographyDataType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1BibliographyDataType.html>`_
    """
    ARTICLE: Literal[0]
    """
    An article from a journal or magazine.
    """
    BOOK: Literal[1]
    """
    A book with an explicit publisher.
    """
    BOOKLET: Literal[2]
    """
    A work that is printed and bound, but without a named publisher or sponsoring institution.
    """
    CONFERENCE: Literal[3]
    """
    An article in the proceedings of a conference.
    
    This entry is identical to the \"inproceedings\" entry and is included for compatibility with BiBTex.
    """
    INBOOK: Literal[4]
    """
    A part of a book, which may be a chapter and/or a range of pages.
    """
    INCOLLECTION: Literal[5]
    """
    A part of a book with its own title.
    """
    INPROCEEDINGS: Literal[6]
    """
    An article in the proceedings of a conference.
    """
    JOURNAL: Literal[7]
    """
    A journal or magazine.
    """
    MANUAL: Literal[8]
    """
    Technical documentation.
    """
    MASTERSTHESIS: Literal[9]
    """
    A Master's thesis.
    """
    MISC: Literal[10]
    """
    This type is used when nothing else seems appropriate.
    """
    PHDTHESIS: Literal[11]
    """
    A PhD thesis.
    """
    PROCEEDINGS: Literal[12]
    """
    The proceedings of a conference.
    """
    TECHREPORT: Literal[13]
    """
    A report published by a school or other institution, usually numbered within a series.
    """
    UNPUBLISHED: Literal[14]
    """
    A document with an author and title, but not formally published.
    """
    EMAIL: Literal[15]
    """
    An eMail document.
    """
    WWW: Literal[16]
    """
    A Web document.
    """
    CUSTOM1: Literal[17]
    """
    A user defined document type.
    """
    CUSTOM2: Literal[18]
    """
    A user defined document type.
    """
    CUSTOM3: Literal[19]
    """
    A user defined document type.
    """
    CUSTOM4: Literal[20]
    """
    A user defined document type.
    """
    CUSTOM5: Literal[21]
    """
    A user defined document type.
    """

