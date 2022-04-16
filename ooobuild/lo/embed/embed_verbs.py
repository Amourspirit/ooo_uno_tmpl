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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.embed


class EmbedVerbs(object):
    """
    Const Class

    This constants set contains possible verbs for a contained object.

    See Also:
        `API EmbedVerbs <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1embed_1_1EmbedVerbs.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.EmbedVerbs'
    __ooo_type_name__: str = 'const'

    MS_OLEVERB_PRIMARY = 0
    """
    lets the object do default activation, as by double-click.
    """
    MS_OLEVERB_SHOW = -1
    """
    lets the object open itself for editing of viewing.
    """
    MS_OLEVERB_OPEN = -2
    """
    lets the object activate itself outplace.
    """
    MS_OLEVERB_HIDE = -3
    """
    lets the inplace object remove its UI from container.
    """
    MS_OLEVERB_UIACTIVATE = -4
    """
    lets the object proceed with UI activation.
    """
    MS_OLEVERB_IPACTIVATE = -5
    """
    lets the object activate itself inplace.
    """
    MS_OLEVERB_DISCARDUNDOSTATE = -6
    """
    lets the object forget any undo state.
    """

__all__ = ['EmbedVerbs']
