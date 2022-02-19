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
from _base_const_dyn import BaseConstDyn

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post2'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 2)
__CHEETAH_genTime__ = 1645301405.7004495
__CHEETAH_genTimestamp__ = 'Sat Feb 19 15:10:05 2022'
__CHEETAH_src__ = '_const_dyn.tmpl'
__CHEETAH_srcLastModified__ = 'Sat Feb 19 15:10:01 2022'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class const_dyn(BaseConstDyn):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(const_dyn, self).__init__(*args, **KWs)
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
        #  str or list or tupple
        #   following attr will get values from BaseEnumDyn class
        _v = VFN(VFFSL(SL,"self",True),"load_data",False)() # '$self.load_data()' on line 23, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.load_data()')) # from line 23, col 1.
        #  Main Template
        safe_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"name",True))
        fullname = VFFSL(SL,"namespace",True) + '.' + VFFSL(SL,"safe_name",True)
        uno_obj_ns = VFFSL(SL,"dyn",True) + VFN(VFN(VFFSL(SL,"fullname",True),"removeprefix",False)('com.sun.star'),"rsplit",False)(sep='.', maxsplit=1)[0]
        uno_obj_in = VFFSL(SL,"uno_obj",True) + VFN(VFFSL(SL,"fullname",True),"removeprefix",False)('com.sun.star')
        enum_class = 'IntFlag' if VFFSL(SL,"flags",True) else 'IntEnum'
        write('''# coding: utf-8
''')
        self._handleCheetahInclude("resources/inc_lic.txt", trans=trans, includeFrom="file", raw=True)
        write('''# Const Class
# this is a auto generated file generated by Cheetah
''')
        if VFFSL(SL,"libre_office_ver",True): # generated from line 34, col 1
            write('''# Libre Office Version: ''')
            _v = VFFSL(SL,"libre_office_ver",True) # '$libre_office_ver' on line 35, col 25
            if _v is not None: write(_filter(_v, rawExpr='$libre_office_ver')) # from line 35, col 25.
            write('''
''')
        write('''# Namespace: ''')
        _v = VFFSL(SL,"namespace",True) # '$namespace' on line 37, col 14
        if _v is not None: write(_filter(_v, rawExpr='$namespace')) # from line 37, col 14.
        write('''
from enum import ''')
        _v = VFFSL(SL,"enum_class",True) # '$enum_class' on line 38, col 18
        if _v is not None: write(_filter(_v, rawExpr='$enum_class')) # from line 38, col 18.
        write('''
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ''')
        _v = VFFSL(SL,"namespace",True) # '$namespace' on line 46, col 10
        if _v is not None: write(_filter(_v, rawExpr='$namespace')) # from line 46, col 10.
        write(''' import ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 46, col 28
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 46, col 28.
        write(''' as ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 46, col 42
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 46, col 42.
        write('''
''')
        # 
        #     Build enum dynamicallly.
        # 
        #     Bulding enum statically can cause issues in backwards compatibility such as com.sun.star.style.NumberingType
        #     contains attribs in 7x version that were not availabe in 6x version.
        write('''    def build_enum():
        global ''')
        _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 54, col 16
        if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 54, col 16.
        write('''Enum
        ls = [f for f in dir(''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 55, col 30
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 55, col 30.
        write(''') if not callable(getattr(''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 55, col 66
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 55, col 66.
        write(""", f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(""")
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 58, col 35
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 58, col 35.
        write(''', name)
        ''')
        _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 59, col 9
        if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 59, col 9.
        write('''Enum = ''')
        _v = VFFSL(SL,"enum_class",True) # '${enum_class}' on line 59, col 28
        if _v is not None: write(_filter(_v, rawExpr='${enum_class}')) # from line 59, col 28.
        write("""('""")
        _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 59, col 43
        if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 59, col 43.
        write("""Enum', _dict)
    build_enum()
else:
    """)
        _v = VFN(VFFSL(SL,"self",True),"get_rel_import",False)(in_str=VFFSL(SL,"uno_obj_in",True), ns=VFFSL(SL,"uno_obj_ns",True)) # '$self.get_rel_import(in_str=$uno_obj_in, ns=$uno_obj_ns)' on line 62, col 5
        if _v is not None: write(_filter(_v, rawExpr='$self.get_rel_import(in_str=$uno_obj_in, ns=$uno_obj_ns)')) # from line 62, col 5.
        write(''' as ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 62, col 65
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 62, col 65.
        write('''

    class ''')
        _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 64, col 11
        if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 64, col 11.
        write('''Enum(''')
        _v = VFFSL(SL,"enum_class",True) # '$enum_class' on line 64, col 28
        if _v is not None: write(_filter(_v, rawExpr='$enum_class')) # from line 64, col 28.
        write('''):
        """
        Enum of Const Class ''')
        _v = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"name",True)) # '$self.get_safe_word($name)' on line 66, col 29
        if _v is not None: write(_filter(_v, rawExpr='$self.get_safe_word($name)')) # from line 66, col 29.
        write('''

''')
        if isinstance(VFFSL(SL,"desc",True), str): # generated from line 68, col 9
            write('''        ''')
            _v = VFFSL(SL,"desc",True) # '$desc' on line 69, col 9
            if _v is not None: write(_filter(_v, rawExpr='$desc')) # from line 69, col 9.
            write('''
''')
        else: # generated from line 70, col 9
            for line in VFFSL(SL,"desc",True): # generated from line 71, col 13
                write('''        ''')
                _v = VFFSL(SL,"line",True) # '$line' on line 72, col 9
                if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 72, col 9.
                write('''
''')
        write('''        """
''')
        for item in VFFSL(SL,"attribs",True): # generated from line 76, col 5
            write('''        ''')
            _v = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"item",True)['name']) # "$self.get_safe_word($item['name'])" on line 77, col 9
            if _v is not None: write(_filter(_v, rawExpr="$self.get_safe_word($item['name'])")) # from line 77, col 9.
            write(''' = ''')
            _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 77, col 46
            if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 77, col 46.
            write('''.''')
            _v = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"item",True)['name']) # "$self.get_safe_word($item['name'])" on line 77, col 59
            if _v is not None: write(_filter(_v, rawExpr="$self.get_safe_word($item['name'])")) # from line 77, col 59.
            write('''
''')
            if len(VFFSL(SL,"item",True)['lines']) > 0: # generated from line 78, col 9
                write('''        """
''')
                if isinstance(VFFSL(SL,"item",True)['lines'], str): # generated from line 80, col 13
                    write('''        ''')
                    _v = VFFSL(SL,"item",True)['lines'] # "$item['lines']" on line 81, col 9
                    if _v is not None: write(_filter(_v, rawExpr="$item['lines']")) # from line 81, col 9.
                    write('''
''')
                else: # generated from line 82, col 13
                    for line in VFFSL(SL,"item",True)['lines']: # generated from line 83, col 17
                        write('''        ''')
                        _v = VFFSL(SL,"line",True) # '$line' on line 84, col 9
                        if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 84, col 9.
                        write('''
''')
                write('''        """
''')
        write("""
__all__ = ['""")
        _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 91, col 13
        if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 91, col 13.
        write("""', '""")
        _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 91, col 29
        if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 91, col 29.
        write("""Enum']""")
        
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

    hex = False

    flags = False

    name = ""

    namespace = ""

    libre_office_ver = False

    link = ""

    base_class = ""

    quote = set()

    typings = set()

    desc = "" 

    imports = []

    from_imports = []

    from_typing_imports = []

    requires_typing = False

    attribs = []

    uno_obj = ''

    dyn = ''

    _mainCheetahMethod_for_const_dyn = 'respond'

## END CLASS DEFINITION

if not hasattr(const_dyn, '_initCheetahAttributes'):
    templateAPIClass = getattr(const_dyn,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(const_dyn)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=const_dyn()).run()


