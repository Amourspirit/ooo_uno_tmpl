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
# Namespace: com.sun.star.linguistic2
import typing


class DictionaryEventFlags:
    """
    Const

    flags used for the event type in dictionary events.
    
    These flags represent the type of events that a dictionary may broadcast.

    See Also:
        `API DictionaryEventFlags <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1linguistic2_1_1DictionaryEventFlags.html>`_
    """
    ADD_ENTRY: int = ...
    """
    indicates that at least one entry has been added.
    """
    DEL_ENTRY: int = ...
    """
    indicates that at least one entry has been deleted.
    """
    CHG_NAME: int = ...
    """
    the dictionary's name has changed.
    """
    CHG_LANGUAGE: int = ...
    """
    the dictionary's language has changed.
    """
    ENTRIES_CLEARED: int = ...
    """
    all entries have been removed.
    """
    ACTIVATE_DIC: int = ...
    """
    used when the dictionary was activated.
    """
    DEACTIVATE_DIC: int = ...
    """
    used when the dictionary was deactivated.
    """
