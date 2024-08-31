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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.ucb
import typing


class CommandInfoChange:
    """
    Const

    specifies reasons for sending CommandInfoChangeEvents.

    See Also:
        `API CommandInfoChange <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb_1_1CommandInfoChange.html>`_
    """
    COMMAND_INSERTED: int = ...
    """
    A command was inserted into a XCommandInfo.
    """
    COMMAND_REMOVED: int = ...
    """
    A command was removed from a XCommandInfo.
    """

