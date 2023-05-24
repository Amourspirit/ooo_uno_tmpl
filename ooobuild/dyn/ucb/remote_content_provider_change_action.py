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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoEnumMeta
    class RemoteContentProviderChangeAction(metaclass=UnoEnumMeta, type_name="com.sun.star.ucb.RemoteContentProviderChangeAction", name_space="com.sun.star.ucb"):
        """Dynamically created class that represents ``com.sun.star.ucb.RemoteContentProviderChangeAction`` Enum. Class loosely mimics Enum"""
        pass
else:
    if TYPE_CHECKING:
        from com.sun.star.ucb.RemoteContentProviderChangeAction import ADDED as REMOTE_CONTENT_PROVIDER_CHANGE_ACTION_ADDED
        from com.sun.star.ucb.RemoteContentProviderChangeAction import REMOVED as REMOTE_CONTENT_PROVIDER_CHANGE_ACTION_REMOVED

        class RemoteContentProviderChangeAction(uno.Enum):
            """
            Enum Class


            See Also:
                `API RemoteContentProviderChangeAction <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb.html#abe4a959f1ea6647971dafe5b6c90c7ec>`_
            """

            def __init__(self, value: Any) -> None:
                super().__init__('com.sun.star.ucb.RemoteContentProviderChangeAction', value)

            __ooo_ns__: str = 'com.sun.star.ucb'
            __ooo_full_ns__: str = 'com.sun.star.ucb.RemoteContentProviderChangeAction'
            __ooo_type_name__: str = 'enum'

            ADDED = REMOTE_CONTENT_PROVIDER_CHANGE_ACTION_ADDED
            """
            The indicator that a remote content provider has been added.
            """
            REMOVED = REMOTE_CONTENT_PROVIDER_CHANGE_ACTION_REMOVED
            """
            The indicator that a remote content provider has been removed.
            """
    else:
        # keep document generators happy
        from ...lo.ucb.remote_content_provider_change_action import RemoteContentProviderChangeAction as RemoteContentProviderChangeAction


__all__ = ['RemoteContentProviderChangeAction']
