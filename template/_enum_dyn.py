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
__CHEETAH_version__ = '3.2.6.post2'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 2)
__CHEETAH_genTime__ = 1644265907.1336803
__CHEETAH_genTimestamp__ = 'Mon Feb  7 15:31:47 2022'
__CHEETAH_src__ = '_enum_dyn.tmpl'
__CHEETAH_srcLastModified__ = 'Mon Feb  7 15:31:43 2022'
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
        # set s_enum = ''
        key_list = list(VFN(VFFSL(SL,"enum_dict",True),"keys",False)())
        uno_obj_ns = VFFSL(SL,"dyn",True) + VFN(VFN(VFFSL(SL,"fullname",True),"removeprefix",False)('com.sun.star'),"rsplit",False)(sep='.', maxsplit=1)[0]
        uno_obj_in = VFFSL(SL,"uno_obj",True) + VFN(VFFSL(SL,"fullname",True),"removeprefix",False)('com.sun.star')
        # set $s_enum = $self.dict_keys_to_str($enum_dict)
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
        write('''from typing import TYPE_CHECKING
from enum import Enum
from ''')
        _v = VFFSL(SL,"oenv",True) # '$oenv' on line 48, col 6
        if _v is not None: write(_filter(_v, rawExpr='$oenv')) # from line 48, col 6.
        write(''' import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ''')
        _v = VFFSL(SL,"uno_enum_namespace",True) # '$uno_enum_namespace' on line 54, col 10
        if _v is not None: write(_filter(_v, rawExpr='$uno_enum_namespace')) # from line 54, col 10.
        write(''' import uno_enum_class_new
    from ''')
        _v = VFFSL(SL,"namespace",True) # '$namespace' on line 55, col 10
        if _v is not None: write(_filter(_v, rawExpr='$namespace')) # from line 55, col 10.
        write(''' import ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 55, col 28
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 55, col 28.
        write(''' as U''')
        _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 55, col 43
        if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 55, col 43.
        write('''

    def _dynamic_enum():
        # Dynamically create class that actually contains UNO enum instances
        global ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 59, col 16
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 59, col 16.
        write('''
        _dict = {
''')
        for key in VFFSL(SL,"key_list",True): # generated from line 61, col 1
            safe_key = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"key",True))
            write('''            "''')
            _v = VFFSL(SL,"safe_key",True) # '$safe_key' on line 63, col 14
            if _v is not None: write(_filter(_v, rawExpr='$safe_key')) # from line 63, col 14.
            write('''": U''')
            _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 63, col 27
            if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 63, col 27.
            write('''.''')
            _v = VFFSL(SL,"safe_key",True) # '${safe_key}' on line 63, col 40
            if _v is not None: write(_filter(_v, rawExpr='${safe_key}')) # from line 63, col 40.
            write(''',
''')
        write('''        }

        ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 67, col 9
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 67, col 9.
        write(""" = type('""")
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 67, col 28
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 67, col 28.
        write('''\', (object,), {
            \'__doc__\': \'class created dynamically. Class loosly mimics Enum\',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 72, col 21
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 72, col 21.
        write(''', k, v)
        setattr(''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 73, col 17
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 73, col 17.
        write(""", ' __ooo_ns__', '""")
        _v = VFFSL(SL,"namespace",True) # '$namespace' on line 73, col 45
        if _v is not None: write(_filter(_v, rawExpr='$namespace')) # from line 73, col 45.
        write("""')
        setattr(""")
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 74, col 17
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 74, col 17.
        write(""", ' __ooo_full_ns__', '""")
        _v = VFFSL(SL,"fullname",True) # '$fullname' on line 74, col 50
        if _v is not None: write(_filter(_v, rawExpr='$fullname')) # from line 74, col 50.
        write("""')
        setattr(""")
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 75, col 17
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 75, col 17.
        write(""", ' __ooo_type_name__', 'enum')
    _dynamic_enum()
else:
    """)
        _v = VFN(VFFSL(SL,"self",True),"get_rel_import",False)(in_str=VFFSL(SL,"uno_obj_in",True), ns=VFFSL(SL,"uno_obj_ns",True)) # '$self.get_rel_import(in_str=$uno_obj_in, ns=$uno_obj_ns)' on line 78, col 5
        if _v is not None: write(_filter(_v, rawExpr='$self.get_rel_import(in_str=$uno_obj_in, ns=$uno_obj_ns)')) # from line 78, col 5.
        write(''' as ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 78, col 65
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 78, col 65.
        write("""

__all__ = ['""")
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 80, col 13
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 80, col 13.
        write("""']
""")
        
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

    oenv = ''

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


