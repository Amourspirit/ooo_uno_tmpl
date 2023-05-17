#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from Cheetah.compat import unicode
from _base_enum_pyi import BaseEnumPyi

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post1'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 1)
__CHEETAH_genTime__ = 1684288878.3199608
__CHEETAH_genTimestamp__ = 'Tue May 16 22:01:18 2023'
__CHEETAH_src__ = '_enum_pyi.tmpl'
__CHEETAH_srcLastModified__ = 'Tue May 16 22:01:02 2023'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class enum_pyi(BaseEnumPyi):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(enum_pyi, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        _v = VFN(VFFSL(SL,"self",True),"init_data",False)() # '$self.init_data()' on line 4, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.init_data()')) # from line 4, col 1.
        #  set is attribs is sorted
        #  str, list, tupple
        #  $enum_dict
        # 
        # key: const name
        # value: string or list, tuple of strings
        _v = VFN(VFFSL(SL,"self",True),"load_data",False)() # '$self.load_data()' on line 23, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.load_data()')) # from line 23, col 1.
        #  Main Template
        if VFFSL(SL,"write_class",True): # generated from line 25, col 1
            indt = "    "
        else: # generated from line 27, col 1
            indt = ""
        safe_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"name",True))
        fullname = VFFSL(SL,"namespace",True) + '.' + VFFSL(SL,"safe_name",True)
        s_enum = ''
        key_list = list(VFN(VFFSL(SL,"enum_dict",True),"keys",False)())
        s_enum = VFN(VFFSL(SL,"self",True),"dict_keys_to_str",False)(VFFSL(SL,"enum_dict",True))
        write('''# coding: utf-8
''')
        self._handleCheetahInclude("resources/inc_lic.txt", trans=trans, includeFrom="file", raw=True)
        write('''# Enum
# this is a auto generated file generated by Cheetah
# Namespace: ''')
        _v = VFFSL(SL,"namespace",True) # '$namespace' on line 39, col 14
        if _v is not None: write(_filter(_v, rawExpr='$namespace')) # from line 39, col 14.
        write('''
''')
        if VFFSL(SL,"libre_office_ver",True): # generated from line 40, col 1
            write('''# Libre Office Version: ''')
            _v = VFFSL(SL,"libre_office_ver",True) # '$libre_office_ver' on line 41, col 25
            if _v is not None: write(_filter(_v, rawExpr='$libre_office_ver')) # from line 41, col 25.
            write('''
''')
        write('''from __future__ import annotations
import uno
''')
        if VFFSL(SL,"write_class",True): # generated from line 45, col 1
            write('''

class ''')
            _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 48, col 7
            if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 48, col 7.
            write('''(uno.Enum):
''')
        else: # generated from line 49, col 1
            #  from com.sun.star._pyi.style.tab_align import TabAlign as TabAlign
            _v = VFN(VFFSL(SL,"self",True),"get_pyi_com_import",False)() # '$self.get_pyi_com_import()' on line 51, col 1
            if _v is not None: write(_filter(_v, rawExpr='$self.get_pyi_com_import()')) # from line 51, col 1.
            write('''
''')
        _v = VFFSL(SL,"indt",True) # '${indt}' on line 53, col 1
        if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 53, col 1.
        write('''"""
''')
        _v = VFFSL(SL,"indt",True) # '${indt}' on line 54, col 1
        if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 54, col 1.
        write('''Enum

''')
        if isinstance(VFFSL(SL,"desc",True), str) and VFFSL(SL,"desc",True): # generated from line 56, col 5
            _v = VFFSL(SL,"indt",True) # '${indt}' on line 57, col 1
            if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 57, col 1.
            _v = VFFSL(SL,"desc",True) # '${desc}' on line 57, col 8
            if _v is not None: write(_filter(_v, rawExpr='${desc}')) # from line 57, col 8.
            write('''
''')
        else: # generated from line 58, col 5
            for line in VFFSL(SL,"desc",True): # generated from line 59, col 9
                if VFFSL(SL,"line",True): # generated from line 60, col 13
                    _v = VFFSL(SL,"indt",True) # '${indt}' on line 61, col 1
                    if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 61, col 1.
                    _v = VFFSL(SL,"line",True) # '${line}' on line 61, col 8
                    if _v is not None: write(_filter(_v, rawExpr='${line}')) # from line 61, col 8.
                    write('''
''')
        if VFFSL(SL,"link",True): # generated from line 65, col 1
            write('''
''')
            _v = VFFSL(SL,"indt",True) # '${indt}' on line 67, col 1
            if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 67, col 1.
            write('''See Also:
''')
            _v = VFFSL(SL,"indt",True) # '${indt}' on line 68, col 1
            if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 68, col 1.
            write('''    `API ''')
            _v = VFFSL(SL,"name",True) # '$name' on line 68, col 17
            if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 68, col 17.
            write(''' <''')
            _v = VFFSL(SL,"link",True) # '$link' on line 68, col 24
            if _v is not None: write(_filter(_v, rawExpr='$link')) # from line 68, col 24.
            write('''>`_
''')
        _v = VFFSL(SL,"indt",True) # '${indt}' on line 70, col 1
        if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 70, col 1.
        write('''"""
''')
        #  Assign value because Literal is python 3.8 +
        _v = VFFSL(SL,"indt",True) # '${indt}' on line 72, col 1
        if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 72, col 1.
        write("""typeName: str = '""")
        _v = VFFSL(SL,"fullname",True) # '$fullname' on line 72, col 25
        if _v is not None: write(_filter(_v, rawExpr='$fullname')) # from line 72, col 25.
        write("""'

""")
        for key in VFFSL(SL,"key_list",True): # generated from line 74, col 1
            # $self.get_safe_word($key)$self.get_typing($self.get_safe_word($key))
            _v = VFFSL(SL,"indt",True) # '${indt}' on line 76, col 1
            if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 76, col 1.
            _v = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"key",True)) # '$self.get_safe_word($key)' on line 76, col 8
            if _v is not None: write(_filter(_v, rawExpr='$self.get_safe_word($key)')) # from line 76, col 8.
            write(''': Pyi''')
            _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 76, col 38
            if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 76, col 38.
            write(''' = ...
''')
            value = VFFSL(SL,"enum_dict",True)[VFFSL(SL,"key",True)]
            _v = VFFSL(SL,"indt",True) # '${indt}' on line 78, col 1
            if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 78, col 1.
            write('''"""
''')
            if isinstance(VFFSL(SL,"value",True), str): # generated from line 79, col 1
                _v = VFFSL(SL,"indt",True) # '${indt}' on line 80, col 1
                if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 80, col 1.
                _v = VFFSL(SL,"value",True) # '$value' on line 80, col 8
                if _v is not None: write(_filter(_v, rawExpr='$value')) # from line 80, col 8.
                write('''
''')
            else: # generated from line 81, col 1
                for line in VFFSL(SL,"value",True): # generated from line 82, col 5
                    _v = VFFSL(SL,"indt",True) # '${indt}' on line 83, col 1
                    if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 83, col 1.
                    _v = VFFSL(SL,"line",True) # '$line' on line 83, col 8
                    if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 83, col 8.
                    write('''
''')
            _v = VFFSL(SL,"indt",True) # '${indt}' on line 86, col 1
            if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 86, col 1.
            write('''"""
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    sort = True 

    name = ""

    namespace = ""

    allow_db = True

    libre_office_ver = False

    quote = set()

    typings = set()

    link = ""

    desc = "" 

    quote = set()

    typings = set()

    write_class = False

    enum_dict = {}

    _mainCheetahMethod_for_enum_pyi = 'respond'

## END CLASS DEFINITION

if not hasattr(enum_pyi, '_initCheetahAttributes'):
    templateAPIClass = getattr(enum_pyi,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(enum_pyi)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=enum_pyi()).run()


