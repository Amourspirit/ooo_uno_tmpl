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
# Libre Office Version: 7.2
# Namespace: com.sun.star.ucb
from typing_extensions import Literal


class FileSystemNotation(object):
    """
    Const

    The notational conventions used to denote file system paths on different file systems or operating systems.

    See Also:
        `API FileSystemNotation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb_1_1FileSystemNotation.html>`_
    """
    UNKNOWN_NOTATION: Literal[0]
    """
    No information regarding any conventions is available.
    """
    UNIX_NOTATION: Literal[1]
    """
    The conventions of Unix like file systems (e.g., /dir1/dir2/file).
    """
    DOS_NOTATION: Literal[2]
    """
    The conventions of DOS like file systems (e.g., a:\\dir1\\dir2\\file or UNC notation like \\\\host\\dir1\\dir2\\file).
    """
    MAC_NOTATION: Literal[3]
    """
    The conventions of Mac like file systems (e.g., volume:dir1:dir2:file).
    """

