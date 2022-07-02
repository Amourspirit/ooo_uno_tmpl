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
# Namespace: com.sun.star.connection
from .x_connector import XConnector as XConnector_e4a10d3b

class Connector(XConnector_e4a10d3b):
    """
    Service Class

    allows to establish a connection to another process.
    
    Connector is a delegating service. You can add further connectors by giving them a service name com.sun.star.connection.Connector.xxx, where xxx is the connection type used in the connection string during accept()/connect() call.

    See Also:
        `API Connector <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1connection_1_1Connector.html>`_
    """
    ...


