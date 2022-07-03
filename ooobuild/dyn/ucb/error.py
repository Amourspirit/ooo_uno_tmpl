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
# Namespace: com.sun.star.ucb
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta,ConstEnumMeta
    class Error(metaclass=UnoConstMeta, type_name="com.sun.star.ucb.Error", name_space="com.sun.star.ucb"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.ucb.Error``"""
        pass

    class ErrorEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.ucb.Error", name_space="com.sun.star.ucb"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.ucb.Error`` as Enum values"""
        pass

else:
    from ...lo.ucb.error import Error as Error

    class ErrorEnum(IntEnum):
        """
        Enum of Const Class Error

        These codes are used to indicate errors.
        
        .. deprecated::
        
            Class is deprecated.
        """
        NONE = Error.NONE
        LOGIN_FAILURE_RECEIVE = Error.LOGIN_FAILURE_RECEIVE
        LOGIN_FAILURE_NEWSSEND = Error.LOGIN_FAILURE_NEWSSEND
        LOGIN_FAILURE_MAILSEND = Error.LOGIN_FAILURE_MAILSEND
        CONNECT_FAILURE = Error.CONNECT_FAILURE
        UCB_OFFLINE = Error.UCB_OFFLINE
        UCB_SERVER_ERROR = Error.UCB_SERVER_ERROR
        STORAGE_READONLY = Error.STORAGE_READONLY
        STORAGE_KILLED = Error.STORAGE_KILLED
        WRONG_FILE_FORMAT = Error.WRONG_FILE_FORMAT
        UNSUPPORTED_URL = Error.UNSUPPORTED_URL
        CNTOUT_NO_FROM = Error.CNTOUT_NO_FROM
        TOO_MANY_GROUPS = Error.TOO_MANY_GROUPS
        DELETE_ABORTED = Error.DELETE_ABORTED
        QUERY_DELETE = Error.QUERY_DELETE
        NOTAVAILABLE = Error.NOTAVAILABLE
        VIM_LIBRARY_ERROR = Error.VIM_LIBRARY_ERROR
        FOLDER_INVALID = Error.FOLDER_INVALID
        FTP_RESOLVERERROR = Error.FTP_RESOLVERERROR
        FTP_NETWORKERROR = Error.FTP_NETWORKERROR
        FTP_NOTNECESSARYCMD = Error.FTP_NOTNECESSARYCMD
        FTP_SERVICEUNAVAILABLE = Error.FTP_SERVICEUNAVAILABLE
        FTP_DCONFAILURE = Error.FTP_DCONFAILURE
        FTP_TRANSFERABORTED = Error.FTP_TRANSFERABORTED
        NO_VIM_LIBRARY = Error.NO_VIM_LIBRARY
        VIM_LIBRARY_CORRUPTED = Error.VIM_LIBRARY_CORRUPTED
        CCMAIL_EXPORT_ERROR = Error.CCMAIL_EXPORT_ERROR
        NO_CCMAIL_EXPORT_FILE = Error.NO_CCMAIL_EXPORT_FILE
        ILLEGAL_CCMAIL_EXPORT_FILE = Error.ILLEGAL_CCMAIL_EXPORT_FILE
        MESSAGE_NOT_FOUND = Error.MESSAGE_NOT_FOUND
        BAD_CCMAIL_EXPORT_PASSWORD = Error.BAD_CCMAIL_EXPORT_PASSWORD
        CCMAIL_EXPORT_TOO_LONG = Error.CCMAIL_EXPORT_TOO_LONG
        FOLDER_EXISTS = Error.FOLDER_EXISTS
        FOLDER_NOT_EXISTS = Error.FOLDER_NOT_EXISTS
        NO_VIM_BBOARDLIST = Error.NO_VIM_BBOARDLIST
        ILLEGAL_MESSAGE_ID = Error.ILLEGAL_MESSAGE_ID
        SERVER_PORT_SYNTAX = Error.SERVER_PORT_SYNTAX
        SERVERNAME_SYNTAX = Error.SERVERNAME_SYNTAX
        USERNAME_SYNTAX = Error.USERNAME_SYNTAX
        IS_RESCHEDULED = Error.IS_RESCHEDULED
        VIM_NO_FAKE_MESSAGE_ID = Error.VIM_NO_FAKE_MESSAGE_ID
        FSYS_ROOT_DELETE = Error.FSYS_ROOT_DELETE
        FILE_EXISTS = Error.FILE_EXISTS
        FILE_NOT_EXISTS = Error.FILE_NOT_EXISTS
        FSYS_MISPLACED_CHAR = Error.FSYS_MISPLACED_CHAR
        FSYS_INVALID_CHAR = Error.FSYS_INVALID_CHAR
        FSYS_INVALID_DEVICE = Error.FSYS_INVALID_DEVICE
        FSYS_ACCESS_DENIED = Error.FSYS_ACCESS_DENIED
        FSYS_LOCK_VIOLATION = Error.FSYS_LOCK_VIOLATION
        FSYS_VOLUME_FULL = Error.FSYS_VOLUME_FULL
        FSYS_NOT_SUPPORTED = Error.FSYS_NOT_SUPPORTED
        FSYS_UNKNOWN = Error.FSYS_UNKNOWN
        FSYS_NOT_A_FILE = Error.FSYS_NOT_A_FILE
        FSYS_NOT_A_DIRECTORY = Error.FSYS_NOT_A_DIRECTORY
        FSYS_IS_WILDCARD = Error.FSYS_IS_WILDCARD
        RENAMED_WRONG_FILE_FORMAT = Error.RENAMED_WRONG_FILE_FORMAT
        FSYS_UPDATE_NEEDED = Error.FSYS_UPDATE_NEEDED
        FSYS_CANT_RESOLVE_CONFLICT = Error.FSYS_CANT_RESOLVE_CONFLICT
        FSYS_CANT_ITERATE = Error.FSYS_CANT_ITERATE
        ONE_NOT_SEARCHABLE = Error.ONE_NOT_SEARCHABLE
        MULTIPLE_NOT_SEARCHABLE = Error.MULTIPLE_NOT_SEARCHABLE
        FSYS_CACHE_INCONSISTENT = Error.FSYS_CACHE_INCONSISTENT
        FSYS_READONLY = Error.FSYS_READONLY
        FSYS_LOCK = Error.FSYS_LOCK
        FSYS_UNLOCK = Error.FSYS_UNLOCK
        FSYS_DELETE = Error.FSYS_DELETE
        FSYS_IS_MARKED = Error.FSYS_IS_MARKED
        FTP_GENERAL_FAILURE = Error.FTP_GENERAL_FAILURE
        DO_LOG = Error.DO_LOG
        HTTP_COOKIE_REQUEST = Error.HTTP_COOKIE_REQUEST
        FSYS_LOST_ROOT = Error.FSYS_LOST_ROOT
        FTP_PROXY = Error.FTP_PROXY
        SOURCE_SAME_AS_TARGET = Error.SOURCE_SAME_AS_TARGET
        CONFIRM_EMPTY_TRASH = Error.CONFIRM_EMPTY_TRASH
        FSYS_NO_TARGET = Error.FSYS_NO_TARGET
        FSYS_RECURSIVE = Error.FSYS_RECURSIVE
        FSYS_INSERT_MEDIUM = Error.FSYS_INSERT_MEDIUM
        NO_DOCINFO = Error.NO_DOCINFO
        CCMAIL_EXPORT_NOT_TERMINATING = Error.CCMAIL_EXPORT_NOT_TERMINATING
        EXTERNAL_COMMAND_FAILED = Error.EXTERNAL_COMMAND_FAILED
        RENAME_FAILED = Error.RENAME_FAILED
        NOT_HANDLED = Error.NOT_HANDLED
        COULD_NOT_INIT_COMPONENT = Error.COULD_NOT_INIT_COMPONENT
        TRANSFER_URL_NOT_SUPPORTED = Error.TRANSFER_URL_NOT_SUPPORTED
        EMPTY_SERVERNAME = Error.EMPTY_SERVERNAME
        EMPTY_USERNAME = Error.EMPTY_USERNAME
        BAD_INET = Error.BAD_INET
        IMAP_SERVER_MSG = Error.IMAP_SERVER_MSG
        IMAP_CONNECTION_CLOSED = Error.IMAP_CONNECTION_CLOSED
        IMAP_NOT_IMAP4 = Error.IMAP_NOT_IMAP4
        IMAP_BAD_SERVER = Error.IMAP_BAD_SERVER
        REORGANIZE_FILE_LOCKED = Error.REORGANIZE_FILE_LOCKED
        IMAP_BAD_TITLE = Error.IMAP_BAD_TITLE
        SERVER_CONNECT_FAILURE = Error.SERVER_CONNECT_FAILURE
        PASSWORD_SYNTAX = Error.PASSWORD_SYNTAX
        QUERY_DELETE_CACHE = Error.QUERY_DELETE_CACHE
        REORGANIZE_NO_DISKSPACE = Error.REORGANIZE_NO_DISKSPACE
        LOGIN_FAILURE_ACCOUNT = Error.LOGIN_FAILURE_ACCOUNT
        ACCOUNT_SYNTAX = Error.ACCOUNT_SYNTAX

__all__ = ['Error', 'ErrorEnum']
