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
# Libre Office Version: 7.2
# Namespace: com.sun.star.awt
from abc import ABC

class RoadmapItem(ABC):
    """
    Service Class


    See Also:
        `API RoadmapItem <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1RoadmapItem.html>`_
    """
    @property
    def Enabled(self) -> bool:
        """
        determines whether a control is enabled or disabled.
        """
    @property
    def ID(self) -> int:
        """
        The ID uniquely identifies the roadmap item.
        
        When the RoadmapItem is inserted into the Roadmap via \"insertByIndex\" the default value of the ID is the first available absolute digit that has not yet been assigned to other existing RoadmapItems.
        """
    @property
    def Interactive(self) -> bool:
        """
        When \"Interactive\" is true the RoadmapItem supports a certain \"HyperLabel
        functionality\": Moving the mouse pointer over the RoadmapItem will change it to a Refhand and underline the Label for the time the mouse pointer resides over the RoadmapItem.
        
        Clicking with mouse pointer will then notify the Roadmap Container. The property Interactive\" is readonly because it is adapted from the container of the RoadmapItem.
        """
    @property
    def Label(self) -> str:
        """
        The Label of the RoadmapItem does not include its Prefix that is automatically set after the following algorithm: (Index + 1) + \". \" + Label.
        """


