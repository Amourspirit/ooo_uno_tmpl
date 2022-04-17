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
# Namespace: com.sun.star.ucb
from abc import abstractmethod
from .x_universal_content_broker import XUniversalContentBroker as XUniversalContentBroker_38ce0f93

class UniversalContentBroker(XUniversalContentBroker_38ce0f93):
    """
    Service Class

    is a one-instance service that provides access to a set of Contents via ContentProviders.
    
    Traditionally, this service implements com.sun.star.lang.XInitialization and needed to be instantiated once with two arguments via com.sun.star.lang.XMultiComponentFactory.createInstanceWithArgumentsAndContext() for configuration before it could be obtained via plain com.sun.star.lang.XMultiComponentFactory.createInstanceWithContext().
    
    However, the only pair of initialization arguments used in practice is \"Local\"/\"Office\", so this service is simplified now to automatically configure itself with that argument pair upon first instantiation.
    
    (For backwards compatibility, the service implementation still supports com.sun.star.lang.XInitialization and can still explicitly be initialized via com.sun.star.lang.XMultiComponentFactory.createInstanceWithArgumentsAndContext() with two arguments of type string. These strings are used as a pair of keys to retrieve a set of content provider descriptions from the configuration management (stored at org.openoffice.ucb.Configuration.ContentProviders.key1.SecondaryKeys.key2.ProviderData within the configuration management's hierarchy). The retrieved descriptions are in turn used to register the corresponding content provider services at the broker.)

    See Also:
        `API UniversalContentBroker <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ucb_1_1UniversalContentBroker.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.UniversalContentBroker'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def create(self) -> None:
        """
        The (default) constructor.
        
        (This default constructor is only mentioned explicitly for technical reasons, so that its implementation calls the service implementation's com.sun.star.lang.XInitialization.initialize().)
        """


__all__ = ['UniversalContentBroker']

