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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.rendering
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.rendering import XMtfRenderer as XMtfRenderer
    setattr(XMtfRenderer, '__ooo_ns__', 'com.sun.star.rendering')
    setattr(XMtfRenderer, '__ooo_full_ns__', 'com.sun.star.rendering.XMtfRenderer')
    setattr(XMtfRenderer, '__ooo_type_name__', 'interface')
else:
    from ...lo.rendering.x_mtf_renderer import XMtfRenderer as XMtfRenderer

__all__ = ['XMtfRenderer']

