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
from _base_const import BaseConst

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post2'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 2)
__CHEETAH_genTime__ = 1641504136.1755595
__CHEETAH_genTimestamp__ = 'Thu Jan  6 16:22:16 2022'
__CHEETAH_src__ = '_const_base.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Jan  5 14:44:35 2022'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class const_base(BaseConst):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(const_base, self).__init__(*args, **KWs)
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
        _v = VFN(VFFSL(SL,"self",True),"load_data",False)() # '$self.load_data()' on line 20, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.load_data()')) # from line 20, col 1.
        #  Main Template
        write('''# coding: utf-8
# Const Class
# this is a auto generated file generated by Cheetah
''')
        if VFFSL(SL,"libre_office_ver",True): # generated from line 25, col 1
            write('''# Libre Office Version: ''')
            _v = VFFSL(SL,"libre_office_ver",True) # '$libre_office_ver' on line 26, col 25
            if _v is not None: write(_filter(_v, rawExpr='$libre_office_ver')) # from line 26, col 25.
            write('''
''')
        if VFFSL(SL,"requires_typing",True): # generated from line 28, col 1
            write('''import typing
''')
        for imp in VFFSL(SL,"imports",True): # generated from line 31, col 1
            write('''import ''')
            _v = VFFSL(SL,"imp",True) # '$imp' on line 32, col 8
            if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 32, col 8.
            write('''
''')
        for frm, imp in VFFSL(SL,"from_imports",True): # generated from line 34, col 1
            write('''from ''')
            _v = VFFSL(SL,"frm",True) # '$frm' on line 35, col 6
            if _v is not None: write(_filter(_v, rawExpr='$frm')) # from line 35, col 6.
            write(''' import ''')
            _v = VFFSL(SL,"imp",True) # '$imp' on line 35, col 18
            if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 35, col 18.
            write('''
''')
        for frm, imp in VFFSL(SL,"from_typing_imports",True): # generated from line 37, col 1
            write('''from ''')
            _v = VFFSL(SL,"frm",True) # '$frm' on line 38, col 6
            if _v is not None: write(_filter(_v, rawExpr='$frm')) # from line 38, col 6.
            write(''' import ''')
            _v = VFFSL(SL,"imp",True) # '$imp' on line 38, col 18
            if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 38, col 18.
            write('''
''')
        write('''

class ''')
        _v = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"name",True)) # '$self.get_safe_word($name)' on line 42, col 7
        if _v is not None: write(_filter(_v, rawExpr='$self.get_safe_word($name)')) # from line 42, col 7.
        write('''(''')
        _v = VFFSL(SL,"base_class",True) # '$base_class' on line 42, col 34
        if _v is not None: write(_filter(_v, rawExpr='$base_class')) # from line 42, col 34.
        write('''):
    """
''')
        if isinstance(VFFSL(SL,"desc",True), str): # generated from line 44, col 5
            write('''    ''')
            _v = VFFSL(SL,"desc",True) # '$desc' on line 45, col 5
            if _v is not None: write(_filter(_v, rawExpr='$desc')) # from line 45, col 5.
            write('''
''')
        else: # generated from line 46, col 5
            for line in VFFSL(SL,"desc",True): # generated from line 47, col 9
                write('''    ''')
                _v = VFFSL(SL,"line",True) # '$line' on line 48, col 5
                if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 48, col 5.
                write('''
''')
        if VFFSL(SL,"link",True): # generated from line 51, col 1
            write('''
    See Also:
        `API ''')
            _v = VFFSL(SL,"name",True) # '$name' on line 54, col 14
            if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 54, col 14.
            write(''' <''')
            _v = VFFSL(SL,"link",True) # '$link' on line 54, col 21
            if _v is not None: write(_filter(_v, rawExpr='$link')) # from line 54, col 21.
            write('''>`_
''')
        write('''    """
''')
        for item in VFFSL(SL,"attribs",True): # generated from line 57, col 1
            write('''    ''')
            _v = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"item",True)['name']) # "$self.get_safe_word($item['name'])" on line 58, col 5
            if _v is not None: write(_filter(_v, rawExpr="$self.get_safe_word($item['name'])")) # from line 58, col 5.
            write(''' = ''')
            _v = VFN(VFFSL(SL,"self",True),"get_q_type",False)(VFFSL(SL,"item",True)['value']) # "$self.get_q_type($item['value'])" on line 58, col 42
            if _v is not None: write(_filter(_v, rawExpr="$self.get_q_type($item['value'])")) # from line 58, col 42.
            write('''
''')
            if len(VFFSL(SL,"item",True)['lines']) > 0: # generated from line 59, col 5
                write('''    """
''')
                if isinstance(VFFSL(SL,"item",True)['lines'], str): # generated from line 61, col 9
                    write('''    ''')
                    _v = VFFSL(SL,"item",True)['lines'] # "$item['lines']" on line 62, col 5
                    if _v is not None: write(_filter(_v, rawExpr="$item['lines']")) # from line 62, col 5.
                    write('''
''')
                else: # generated from line 63, col 9
                    for line in VFFSL(SL,"item",True)['lines']: # generated from line 64, col 13
                        write('''    ''')
                        _v = VFFSL(SL,"line",True) # '$line' on line 65, col 5
                        if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 65, col 5.
                        write('''
''')
                write('''    """
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

    attribs = []

    _mainCheetahMethod_for_const_base = 'respond'

## END CLASS DEFINITION

if not hasattr(const_base, '_initCheetahAttributes'):
    templateAPIClass = getattr(const_base,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(const_base)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=const_base()).run()


