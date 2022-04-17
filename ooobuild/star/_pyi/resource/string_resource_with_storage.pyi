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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.resource
import typing
from .x_string_resource_with_storage import XStringResourceWithStorage as XStringResourceWithStorage_ca5312f8
if typing.TYPE_CHECKING:
    from ..embed.x_storage import XStorage as XStorage_8e460a32
    from ..lang.locale import Locale as Locale_70d308fa

class StringResourceWithStorage(XStringResourceWithStorage_ca5312f8):
    """
    Service Class

    specifies a service providing access to a resource string table implementing the com.sun.star.resource.XStringResourceWithStorage interface.

    See Also:
        `API StringResourceWithStorage <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1resource_1_1StringResourceWithStorage.html>`_
    """
    def create(self, Storage: 'XStorage_8e460a32', ReadOnly: bool, locale: 'Locale_70d308fa', BaseName: str, Comment: str) -> None:
        """
        is used to initialize the object on its creation.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """


