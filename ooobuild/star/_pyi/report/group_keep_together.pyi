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
# Namespace: com.sun.star.report
from typing_extensions import Literal


class GroupKeepTogether(object):
    """
    Const

    Specifies if groups in a multi column report where the group has the property XGroup.KeepTogether set to WHOLE_GROUP or WITH_FIRST_DETAIL will keep together by page or column.

    See Also:
        `API GroupKeepTogether <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1report_1_1GroupKeepTogether.html>`_
    """
    PER_PAGE: Literal[0]
    """
    Groups are kept together by page.
    """
    PER_COLUMN: Literal[1]
    """
    Groups are kept together by column.
    """

