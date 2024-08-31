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


class RuleAction:
    """
    Const

    These are the possible values for Rule.Action.

    See Also:
        `API RuleAction <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb_1_1RuleAction.html>`_
    """
    NONE: int = ...
    """
    \"None\" - Do nothing.
    """
    SHOW: int = ...
    """
    \"Show\" - Shows object when term matches.
    """
    HIDE: int = ...
    """
    \"Hide\" - Hides object when term matches.
    """
    MARK: int = ...
    """
    \"Mark\" - Marks object when term matches.
    """
    UNMARK: int = ...
    """
    \"UnMark\" - Removes mark from object when term matches.
    """
    MARKREAD: int = ...
    """
    \"MarkRead\" - Marks object as read when term matches.
    """
    MARKUNREAD: int = ...
    """
    \"MarkUnRead\" - Marks object as not read when term matches.
    """
    MOVE: int = ...
    """
    \"Move\" - Moves object to Rule.Parameter when term matches.
    """
    COPY: int = ...
    """
    \"Copy\" - Copies object to Rule.Parameter when term matches.
    """
    DELETE: int = ...
    """
    \"Delete\" - Deletes object when term matches.
    """
    LINK: int = ...
    """
    \"Link\" - Creates a link to Rule.Parameter when term matches.
    """
    FORWARD: int = ...
    """
    \"Forward\" - Forwards object to Rule.Parameter when term matches.
    """

