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
from _base_enum_dyn import BaseEnumDyn

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post1'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 1)
__CHEETAH_genTime__ = 1725127803.8701785
__CHEETAH_genTimestamp__ = 'Sat Aug 31 14:10:03 2024'
__CHEETAH_src__ = '_enum_dyn.tmpl'
__CHEETAH_srcLastModified__ = 'Sat Aug 31 14:09:50 2024'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class enum_dyn(BaseEnumDyn):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(enum_dyn, self).__init__(*args, **KWs)
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
        #   following attr will get values from BaseEnumDyn class
        _v = VFN(VFFSL(SL,"self",True),"load_data",False)() # '$self.load_data()' on line 28, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.load_data()')) # from line 28, col 1.
        #  Main Template
        safe_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"name",True))
        fullname = VFFSL(SL,"namespace",True) + '.' + VFFSL(SL,"safe_name",True)
        s_enum = ''
        key_list = list(VFN(VFFSL(SL,"enum_dict",True),"keys",False)())
        uno_obj_ns = VFFSL(SL,"dyn",True) + VFN(VFN(VFFSL(SL,"fullname",True),"removeprefix",False)('com.sun.star'),"rsplit",False)(sep='.', maxsplit=1)[0]
        uno_obj_in = VFFSL(SL,"uno_obj",True) + VFN(VFFSL(SL,"fullname",True),"removeprefix",False)('com.sun.star')
        s_enum = VFN(VFFSL(SL,"self",True),"dict_keys_to_str",False)(VFFSL(SL,"enum_dict",True))
        uno_enum_namespace = VFFSL(SL,"helper_ns",True) + '.' + VFFSL(SL,"enum_mod",True)
        write('''# coding: utf-8
''')
        self._handleCheetahInclude("resources/inc_lic.txt", trans=trans, includeFrom="file", raw=True)
        write('''# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: ''')
        _v = VFFSL(SL,"namespace",True) # '$namespace' on line 42, col 14
        if _v is not None: write(_filter(_v, rawExpr='$namespace')) # from line 42, col 14.
        write('''
''')
        if VFFSL(SL,"libre_office_ver",True): # generated from line 43, col 1
            write('''# Libre Office Version: ''')
            _v = VFFSL(SL,"libre_office_ver",True) # '$libre_office_ver' on line 44, col 25
            if _v is not None: write(_filter(_v, rawExpr='$libre_office_ver')) # from line 44, col 25.
            write('''
''')
        write('''from __future__ import annotations
import uno
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ''')
        _v = VFFSL(SL,"uno_enum_namespace",True) # '$uno_enum_namespace' on line 56, col 10
        if _v is not None: write(_filter(_v, rawExpr='$uno_enum_namespace')) # from line 56, col 10.
        write(''' import UnoEnumMeta
    class ''')
        _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 57, col 11
        if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 57, col 11.
        write('''(metaclass=UnoEnumMeta, type_name="''')
        _v = VFFSL(SL,"fullname",True) # '$fullname' on line 57, col 58
        if _v is not None: write(_filter(_v, rawExpr='$fullname')) # from line 57, col 58.
        write('''", name_space="''')
        _v = VFFSL(SL,"namespace",True) # '$namespace' on line 57, col 82
        if _v is not None: write(_filter(_v, rawExpr='$namespace')) # from line 57, col 82.
        write('''"):
        """Dynamically created class that represents ``''')
        _v = VFFSL(SL,"fullname",True) # '$fullname' on line 58, col 56
        if _v is not None: write(_filter(_v, rawExpr='$fullname')) # from line 58, col 56.
        write('''`` Enum. Class loosely mimics Enum"""
        pass
else:
    ''')
        _v = VFN(VFFSL(SL,"self",True),"get_rel_import",False)(in_str=VFFSL(SL,"uno_obj_in",True), ns=VFFSL(SL,"uno_obj_ns",True)) # '$self.get_rel_import(in_str=$uno_obj_in, ns=$uno_obj_ns)' on line 61, col 5
        if _v is not None: write(_filter(_v, rawExpr='$self.get_rel_import(in_str=$uno_obj_in, ns=$uno_obj_ns)')) # from line 61, col 5.
        write(''' as ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 61, col 65
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 61, col 65.
        write('''

__all__ = ["''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 63, col 13
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 63, col 13.
        write('''"]''')
        
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

    enum_dict = {}

    uno_obj = ''

    dyn = ''

    oenv = 'ooo.oenv.env_const'

    helper_ns = ''

    enum_mod = ''

    _mainCheetahMethod_for_enum_dyn = 'respond'

## END CLASS DEFINITION

if not hasattr(enum_dyn, '_initCheetahAttributes'):
    templateAPIClass = getattr(enum_dyn,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(enum_dyn)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=enum_dyn()).run()


