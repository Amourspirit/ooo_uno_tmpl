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
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.ucb.IOErrorCode import ABORT as I_O_ERROR_CODE_ABORT
    from com.sun.star.ucb.IOErrorCode import ACCESS_DENIED as I_O_ERROR_CODE_ACCESS_DENIED
    from com.sun.star.ucb.IOErrorCode import ALREADY_EXISTING as I_O_ERROR_CODE_ALREADY_EXISTING
    from com.sun.star.ucb.IOErrorCode import BAD_CRC as I_O_ERROR_CODE_BAD_CRC
    from com.sun.star.ucb.IOErrorCode import CANT_CREATE as I_O_ERROR_CODE_CANT_CREATE
    from com.sun.star.ucb.IOErrorCode import CANT_READ as I_O_ERROR_CODE_CANT_READ
    from com.sun.star.ucb.IOErrorCode import CANT_SEEK as I_O_ERROR_CODE_CANT_SEEK
    from com.sun.star.ucb.IOErrorCode import CANT_TELL as I_O_ERROR_CODE_CANT_TELL
    from com.sun.star.ucb.IOErrorCode import CANT_WRITE as I_O_ERROR_CODE_CANT_WRITE
    from com.sun.star.ucb.IOErrorCode import CURRENT_DIRECTORY as I_O_ERROR_CODE_CURRENT_DIRECTORY
    from com.sun.star.ucb.IOErrorCode import DEVICE_NOT_READY as I_O_ERROR_CODE_DEVICE_NOT_READY
    from com.sun.star.ucb.IOErrorCode import DIFFERENT_DEVICES as I_O_ERROR_CODE_DIFFERENT_DEVICES
    from com.sun.star.ucb.IOErrorCode import GENERAL as I_O_ERROR_CODE_GENERAL
    from com.sun.star.ucb.IOErrorCode import INVALID_ACCESS as I_O_ERROR_CODE_INVALID_ACCESS
    from com.sun.star.ucb.IOErrorCode import INVALID_CHARACTER as I_O_ERROR_CODE_INVALID_CHARACTER
    from com.sun.star.ucb.IOErrorCode import INVALID_DEVICE as I_O_ERROR_CODE_INVALID_DEVICE
    from com.sun.star.ucb.IOErrorCode import INVALID_LENGTH as I_O_ERROR_CODE_INVALID_LENGTH
    from com.sun.star.ucb.IOErrorCode import INVALID_PARAMETER as I_O_ERROR_CODE_INVALID_PARAMETER
    from com.sun.star.ucb.IOErrorCode import IS_WILDCARD as I_O_ERROR_CODE_IS_WILDCARD
    from com.sun.star.ucb.IOErrorCode import LOCKING_VIOLATION as I_O_ERROR_CODE_LOCKING_VIOLATION
    from com.sun.star.ucb.IOErrorCode import MISPLACED_CHARACTER as I_O_ERROR_CODE_MISPLACED_CHARACTER
    from com.sun.star.ucb.IOErrorCode import NAME_TOO_LONG as I_O_ERROR_CODE_NAME_TOO_LONG
    from com.sun.star.ucb.IOErrorCode import NOT_EXISTING as I_O_ERROR_CODE_NOT_EXISTING
    from com.sun.star.ucb.IOErrorCode import NOT_EXISTING_PATH as I_O_ERROR_CODE_NOT_EXISTING_PATH
    from com.sun.star.ucb.IOErrorCode import NOT_SUPPORTED as I_O_ERROR_CODE_NOT_SUPPORTED
    from com.sun.star.ucb.IOErrorCode import NO_DIRECTORY as I_O_ERROR_CODE_NO_DIRECTORY
    from com.sun.star.ucb.IOErrorCode import NO_FILE as I_O_ERROR_CODE_NO_FILE
    from com.sun.star.ucb.IOErrorCode import OUT_OF_DISK_SPACE as I_O_ERROR_CODE_OUT_OF_DISK_SPACE
    from com.sun.star.ucb.IOErrorCode import OUT_OF_FILE_HANDLES as I_O_ERROR_CODE_OUT_OF_FILE_HANDLES
    from com.sun.star.ucb.IOErrorCode import OUT_OF_MEMORY as I_O_ERROR_CODE_OUT_OF_MEMORY
    from com.sun.star.ucb.IOErrorCode import PENDING as I_O_ERROR_CODE_PENDING
    from com.sun.star.ucb.IOErrorCode import RECURSIVE as I_O_ERROR_CODE_RECURSIVE
    from com.sun.star.ucb.IOErrorCode import UNKNOWN as I_O_ERROR_CODE_UNKNOWN
    from com.sun.star.ucb.IOErrorCode import WRITE_PROTECTED as I_O_ERROR_CODE_WRITE_PROTECTED
    from com.sun.star.ucb.IOErrorCode import WRONG_FORMAT as I_O_ERROR_CODE_WRONG_FORMAT
    from com.sun.star.ucb.IOErrorCode import WRONG_VERSION as I_O_ERROR_CODE_WRONG_VERSION

    class IOErrorCode(uno.Enum):
        """
        Enum Class


        See Also:
            `API IOErrorCode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb.html#ab0378c2985abaca86838ed9936c3a2d5>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.ucb.IOErrorCode', value)

        __ooo_ns__: str = 'com.sun.star.ucb'
        __ooo_full_ns__: str = 'com.sun.star.ucb.IOErrorCode'
        __ooo_type_name__: str = 'enum'

        ABORT = cast("IOErrorCode", I_O_ERROR_CODE_ABORT)
        """
        An operation was aborted.
        """
        ACCESS_DENIED = cast("IOErrorCode", I_O_ERROR_CODE_ACCESS_DENIED)
        """
        An object cannot be accessed due to insufficient user rights.
        """
        ALREADY_EXISTING = cast("IOErrorCode", I_O_ERROR_CODE_ALREADY_EXISTING)
        """
        An object already exists.
        """
        BAD_CRC = cast("IOErrorCode", I_O_ERROR_CODE_BAD_CRC)
        """
        A bad checksum.
        """
        CANT_CREATE = cast("IOErrorCode", I_O_ERROR_CODE_CANT_CREATE)
        """
        An object could not be created.
        """
        CANT_READ = cast("IOErrorCode", I_O_ERROR_CODE_CANT_READ)
        """
        Data could not be read from a file.
        """
        CANT_SEEK = cast("IOErrorCode", I_O_ERROR_CODE_CANT_SEEK)
        """
        A seek operation could not be run.
        """
        CANT_TELL = cast("IOErrorCode", I_O_ERROR_CODE_CANT_TELL)
        """
        A tell operation could not be run.
        """
        CANT_WRITE = cast("IOErrorCode", I_O_ERROR_CODE_CANT_WRITE)
        """
        Data could not be written to a file.
        """
        CURRENT_DIRECTORY = cast("IOErrorCode", I_O_ERROR_CODE_CURRENT_DIRECTORY)
        """
        A function is not possible because the path contains the current directory.
        """
        DEVICE_NOT_READY = cast("IOErrorCode", I_O_ERROR_CODE_DEVICE_NOT_READY)
        """
        A device (drive) not ready.
        """
        DIFFERENT_DEVICES = cast("IOErrorCode", I_O_ERROR_CODE_DIFFERENT_DEVICES)
        """
        A function is not possible because the devices (drives) are not identical.
        """
        GENERAL = cast("IOErrorCode", I_O_ERROR_CODE_GENERAL)
        """
        A general input/output error.
        """
        INVALID_ACCESS = cast("IOErrorCode", I_O_ERROR_CODE_INVALID_ACCESS)
        """
        An invalid attempt was made to access an object.
        """
        INVALID_CHARACTER = cast("IOErrorCode", I_O_ERROR_CODE_INVALID_CHARACTER)
        """
        A file name contains invalid characters.
        """
        INVALID_DEVICE = cast("IOErrorCode", I_O_ERROR_CODE_INVALID_DEVICE)
        """
        A specified device is invalid.
        """
        INVALID_LENGTH = cast("IOErrorCode", I_O_ERROR_CODE_INVALID_LENGTH)
        """
        Invalid data length.
        """
        INVALID_PARAMETER = cast("IOErrorCode", I_O_ERROR_CODE_INVALID_PARAMETER)
        """
        An operation was started with an invalid parameter.
        """
        IS_WILDCARD = cast("IOErrorCode", I_O_ERROR_CODE_IS_WILDCARD)
        """
        An operation cannot be run on file names containing wildcards.
        """
        LOCKING_VIOLATION = cast("IOErrorCode", I_O_ERROR_CODE_LOCKING_VIOLATION)
        """
        A locking problem.
        """
        MISPLACED_CHARACTER = cast("IOErrorCode", I_O_ERROR_CODE_MISPLACED_CHARACTER)
        """
        An invalid file name.
        """
        NAME_TOO_LONG = cast("IOErrorCode", I_O_ERROR_CODE_NAME_TOO_LONG)
        """
        A file name is too long.
        """
        NOT_EXISTING = cast("IOErrorCode", I_O_ERROR_CODE_NOT_EXISTING)
        """
        A nonexistent object.
        """
        NOT_EXISTING_PATH = cast("IOErrorCode", I_O_ERROR_CODE_NOT_EXISTING_PATH)
        """
        The path to a file does not exist.
        """
        NOT_SUPPORTED = cast("IOErrorCode", I_O_ERROR_CODE_NOT_SUPPORTED)
        """
        An action is not supported.
        """
        NO_DIRECTORY = cast("IOErrorCode", I_O_ERROR_CODE_NO_DIRECTORY)
        """
        An object is not a directory.
        """
        NO_FILE = cast("IOErrorCode", I_O_ERROR_CODE_NO_FILE)
        """
        An object is not a file.
        """
        OUT_OF_DISK_SPACE = cast("IOErrorCode", I_O_ERROR_CODE_OUT_OF_DISK_SPACE)
        """
        No more space on a device.
        """
        OUT_OF_FILE_HANDLES = cast("IOErrorCode", I_O_ERROR_CODE_OUT_OF_FILE_HANDLES)
        """
        No more file handles available.
        """
        OUT_OF_MEMORY = cast("IOErrorCode", I_O_ERROR_CODE_OUT_OF_MEMORY)
        """
        An operation could not be run due to insufficient memory.
        """
        PENDING = cast("IOErrorCode", I_O_ERROR_CODE_PENDING)
        """
        An operation is still pending.
        """
        RECURSIVE = cast("IOErrorCode", I_O_ERROR_CODE_RECURSIVE)
        """
        An object cannot be copied into itself.
        """
        UNKNOWN = cast("IOErrorCode", I_O_ERROR_CODE_UNKNOWN)
        """
        Unknown.
        
        An unknown I/O error has occurred.
        """
        WRITE_PROTECTED = cast("IOErrorCode", I_O_ERROR_CODE_WRITE_PROTECTED)
        """
        A function is not possible because the object is write protected.
        """
        WRONG_FORMAT = cast("IOErrorCode", I_O_ERROR_CODE_WRONG_FORMAT)
        """
        An incorrect file format.
        """
        WRONG_VERSION = cast("IOErrorCode", I_O_ERROR_CODE_WRONG_VERSION)
        """
        An incorrect file version.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class IOErrorCode(metaclass=UnoEnumMeta, type_name="com.sun.star.ucb.IOErrorCode", name_space="com.sun.star.ucb"):
        """Dynamically created class that represents ``com.sun.star.ucb.IOErrorCode`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['IOErrorCode']
