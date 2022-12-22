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
# Libre Office Version: 7.2
# Namespace: com.sun.star.lang
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class SystemDependent(metaclass=UnoConstMeta, type_name="com.sun.star.lang.SystemDependent", name_space="com.sun.star.lang"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.lang.SystemDependent``"""
        pass

    class SystemDependentEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.lang.SystemDependent", name_space="com.sun.star.lang"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.lang.SystemDependent`` as Enum values"""
        pass

else:
    from ...lo.lang.system_dependent import SystemDependent as SystemDependent

    class SystemDependentEnum(IntEnum):
        """
        Enum of Const Class SystemDependent

        These constants are used to specify systems which depend on return values.
        
        You should avoid system-dependent methods if possible.
        
        The Symbols are now prepended with SYSTEM_ thus we avoid collisions with system headers.
        
        .. deprecated::
        
            Class is deprecated.
        """
        SYSTEM_WIN32 = SystemDependent.SYSTEM_WIN32
        """
        The called interface method returns a value specified for Windows.
        
        These are Windows XP or higher.
        """
        SYSTEM_WIN16 = SystemDependent.SYSTEM_WIN16
        """
        The called interface method returns a value specified for 16-bit Windows.
        
        This is Windows 3.11.
        """
        SYSTEM_JAVA = SystemDependent.SYSTEM_JAVA
        """
        The called interface method returns a value specified for Java.
        
        These are JRE 1.1, JRE 1.2, JDK 1.1, JDK 1.2 or higher.
        
        The return should be a handle to a Java object locked with the call JavaEnvironment->NewGlobalRef( ... ) by the callee.
        """
        SYSTEM_OS2 = SystemDependent.SYSTEM_OS2
        """
        The called interface method returns a value specified for OS/2.
        """
        SYSTEM_MAC = SystemDependent.SYSTEM_MAC
        """
        The called interface method returns a value specified for macOS.
        """
        SYSTEM_XWINDOW = SystemDependent.SYSTEM_XWINDOW
        """
        The called interface method returns a value specified for the X Window System.
        """
        SYSTEM_IOS = SystemDependent.SYSTEM_IOS
        """
        The called interface method returns a value specified for iOS.
        """
        SYSTEM_ANDROID = SystemDependent.SYSTEM_ANDROID
        """
        The called interface method returns a value specified for Android.
        """

__all__ = ['SystemDependent', 'SystemDependentEnum']
