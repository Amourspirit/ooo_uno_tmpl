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
from _base_const_pyi import BaseConstPyi

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post2'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 2)
__CHEETAH_genTime__ = 1652559446.7120306
__CHEETAH_genTimestamp__ = 'Sat May 14 16:17:26 2022'
__CHEETAH_src__ = '_const_pyi.tmpl'
__CHEETAH_srcLastModified__ = 'Sat May 14 16:06:39 2022'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class const_pyi(BaseConstPyi):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(const_pyi, self).__init__(*args, **KWs)
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
        _v = VFN(VFFSL(SL,"self",True),"load_data",False)() # '$self.load_data()' on line 21, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.load_data()')) # from line 21, col 1.
        #  Main Template
        if VFFSL(SL,"write_class",True): # generated from line 23, col 1
            indt = "    "
        else: # generated from line 25, col 1
            indt = ""
        safe_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"name",True))
        fullname = VFFSL(SL,"namespace",True) + '.' + VFFSL(SL,"safe_name",True)
        write('''# coding: utf-8
''')
        self._handleCheetahInclude("resources/inc_lic.txt", trans=trans, includeFrom="file", raw=True)
        write('''# Const
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
from typing_extensions import Literal
''')
        if VFFSL(SL,"requires_typing",True): # generated from line 39, col 1
            write('''import typing
''')
        for imp in VFFSL(SL,"imports",True): # generated from line 42, col 1
            write('''import ''')
            _v = VFFSL(SL,"imp",True) # '$imp' on line 43, col 8
            if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 43, col 8.
            write('''
''')
        for frm, imp in VFFSL(SL,"from_imports",True): # generated from line 45, col 1
            write('''from ''')
            _v = VFFSL(SL,"frm",True) # '$frm' on line 46, col 6
            if _v is not None: write(_filter(_v, rawExpr='$frm')) # from line 46, col 6.
            write(''' import ''')
            _v = VFFSL(SL,"imp",True) # '$imp' on line 46, col 18
            if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 46, col 18.
            write('''
''')
        for frm, imp in VFFSL(SL,"from_typing_imports",True): # generated from line 48, col 1
            write('''from ''')
            _v = VFFSL(SL,"frm",True) # '$frm' on line 49, col 6
            if _v is not None: write(_filter(_v, rawExpr='$frm')) # from line 49, col 6.
            write(''' import ''')
            _v = VFFSL(SL,"imp",True) # '$imp' on line 49, col 18
            if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 49, col 18.
            write('''
''')
        if VFFSL(SL,"write_class",True): # generated from line 51, col 1
            write('''

class ''')
            _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 54, col 7
            if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 54, col 7.
            write('''(object):
''')
        _v = VFFSL(SL,"indt",True) # '${indt}' on line 56, col 1
        if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 56, col 1.
        write('''"""
''')
        _v = VFFSL(SL,"indt",True) # '${indt}' on line 57, col 1
        if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 57, col 1.
        write('''Const

''')
        if isinstance(VFFSL(SL,"desc",True), str): # generated from line 59, col 5
            _v = VFFSL(SL,"indt",True) # '${indt}' on line 60, col 1
            if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 60, col 1.
            _v = VFFSL(SL,"desc",True) # '${desc}' on line 60, col 8
            if _v is not None: write(_filter(_v, rawExpr='${desc}')) # from line 60, col 8.
            write('''
''')
        else: # generated from line 61, col 5
            for line in VFFSL(SL,"desc",True): # generated from line 62, col 9
                _v = VFFSL(SL,"indt",True) # '${indt}' on line 63, col 1
                if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 63, col 1.
                _v = VFFSL(SL,"line",True) # '${line}' on line 63, col 8
                if _v is not None: write(_filter(_v, rawExpr='${line}')) # from line 63, col 8.
                write('''
''')
        if VFFSL(SL,"link",True): # generated from line 66, col 1
            write('''
''')
            _v = VFFSL(SL,"indt",True) # '${indt}' on line 68, col 1
            if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 68, col 1.
            write('''See Also:
''')
            _v = VFFSL(SL,"indt",True) # '${indt}' on line 69, col 1
            if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 69, col 1.
            write('''    `API ''')
            _v = VFFSL(SL,"name",True) # '$name' on line 69, col 17
            if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 69, col 17.
            write(''' <''')
            _v = VFFSL(SL,"link",True) # '$link' on line 69, col 24
            if _v is not None: write(_filter(_v, rawExpr='$link')) # from line 69, col 24.
            write('''>`_
''')
        _v = VFFSL(SL,"indt",True) # '${indt}' on line 71, col 1
        if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 71, col 1.
        write('''"""
''')
        for item in VFFSL(SL,"attribs",True): # generated from line 72, col 1
            _v = VFFSL(SL,"indt",True) # '${indt}' on line 73, col 1
            if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 73, col 1.
            _v = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"item",True)['name']) # "$self.get_safe_word($item['name'])" on line 73, col 8
            if _v is not None: write(_filter(_v, rawExpr="$self.get_safe_word($item['name'])")) # from line 73, col 8.
            write(''': ''')
            _v = VFN(VFFSL(SL,"self",True),"get_const_type",False)(VFFSL(SL,"item",True)) # '$self.get_const_type($item)' on line 73, col 44
            if _v is not None: write(_filter(_v, rawExpr='$self.get_const_type($item)')) # from line 73, col 44.
            write('''
''')
            if len(VFFSL(SL,"item",True)['lines']) > 0: # generated from line 74, col 5
                _v = VFFSL(SL,"indt",True) # '${indt}' on line 75, col 1
                if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 75, col 1.
                write('''"""
''')
                if isinstance(VFFSL(SL,"item",True)['lines'], str): # generated from line 76, col 9
                    _v = VFFSL(SL,"indt",True) # '${indt}' on line 77, col 1
                    if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 77, col 1.
                    _v = VFFSL(SL,"item",True)['lines'] # "$item['lines']" on line 77, col 8
                    if _v is not None: write(_filter(_v, rawExpr="$item['lines']")) # from line 77, col 8.
                    write('''
''')
                else: # generated from line 78, col 9
                    for line in VFFSL(SL,"item",True)['lines']: # generated from line 79, col 13
                        _v = VFFSL(SL,"indt",True) # '${indt}' on line 80, col 1
                        if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 80, col 1.
                        _v = VFFSL(SL,"line",True) # '$line' on line 80, col 8
                        if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 80, col 8.
                        write('''
''')
                _v = VFFSL(SL,"indt",True) # '${indt}' on line 83, col 1
                if _v is not None: write(_filter(_v, rawExpr='${indt}')) # from line 83, col 1.
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

    write_class = False

    attribs = []

    _mainCheetahMethod_for_const_pyi = 'respond'

## END CLASS DEFINITION

if not hasattr(const_pyi, '_initCheetahAttributes'):
    templateAPIClass = getattr(const_pyi,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(const_pyi)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=const_pyi()).run()


