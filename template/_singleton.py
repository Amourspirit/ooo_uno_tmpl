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
import typing
from _base_singleton import BaseSingleton

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post2'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 2)
__CHEETAH_genTime__ = 1641050169.6318295
__CHEETAH_genTimestamp__ = 'Sat Jan  1 10:16:09 2022'
__CHEETAH_src__ = '_singleton.tmpl'
__CHEETAH_srcLastModified__ = 'Sat Jan  1 10:15:18 2022'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class singleton(BaseSingleton):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(singleton, self).__init__(*args, **KWs)
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
        
        #  see: https://cheetahtemplate.org/users_guide/inheritanceEtc.html#implements
        _v = VFN(VFFSL(SL,"self",True),"init_data",False)() # '$self.init_data()' on line 6, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.init_data()')) # from line 6, col 1.
        #  $from_imports is a tuple eg: $from_imports = [('.tab_align', 'TabAlign')]
        _v = VFN(VFFSL(SL,"self",True),"load_data",False)() # '$self.load_data()' on line 21, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.load_data()')) # from line 21, col 1.
        #  main Template
        safe_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"name",True))
        is_method = 'methods' in VFFSL(SL,"attribs",True)
        is_properties = 'properties' in VFFSL(SL,"attribs",True)
        write('''# coding: utf-8
# this is a auto generated file generated by Cheetah
# Generated: ''')
        _v = VFN(VFFSL(SL,"self",True),"get_timestamp_utc",False)() # '$self.get_timestamp_utc()' on line 28, col 14
        if _v is not None: write(_filter(_v, rawExpr='$self.get_timestamp_utc()')) # from line 28, col 14.
        write('''
''')
        if VFFSL(SL,"requires_typing",True): # generated from line 29, col 1
            write('''import typing
''')
        for imp in VFFSL(SL,"imports",True): # generated from line 32, col 1
            write('''import ''')
            _v = VFFSL(SL,"imp",True) # '$imp' on line 33, col 8
            if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 33, col 8.
            write('''
''')
        for frm, imp in VFFSL(SL,"from_imports",True): # generated from line 35, col 1
            write('''from ''')
            _v = VFFSL(SL,"frm",True) # '$frm' on line 36, col 6
            if _v is not None: write(_filter(_v, rawExpr='$frm')) # from line 36, col 6.
            write(''' import ''')
            _v = VFFSL(SL,"imp",True) # '$imp' on line 36, col 18
            if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 36, col 18.
            write('''
''')
        if len(VFFSL(SL,"from_imports_typing",True)) > 0: # generated from line 38, col 1
            write('''if typing.TYPE_CHECKING:
''')
            for frm, imp in VFFSL(SL,"from_imports_typing",True): # generated from line 40, col 1
                write('''    from ''')
                _v = VFFSL(SL,"frm",True) # '$frm' on line 41, col 10
                if _v is not None: write(_filter(_v, rawExpr='$frm')) # from line 41, col 10.
                write(''' import ''')
                _v = VFFSL(SL,"imp",True) # '$imp' on line 41, col 22
                if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 41, col 22.
                write('''
''')
        write('''

class ''')
        _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 46, col 7
        if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 46, col 7.
        write('''(''')
        _v = VFN(VFFSL(SL,"self",True),"lst_to_str",False)(VFFSL(SL,"inherits",True)) # '$self.lst_to_str($inherits)' on line 46, col 20
        if _v is not None: write(_filter(_v, rawExpr='$self.lst_to_str($inherits)')) # from line 46, col 20.
        write(''')''')
        _v = VFN(VFFSL(SL,"self",True),"get_class_end",False)() # '$self.get_class_end()' on line 46, col 48
        if _v is not None: write(_filter(_v, rawExpr='$self.get_class_end()')) # from line 46, col 48.
        write('''
''')
        if VFFSL(SL,"include_desc",True): # generated from line 47, col 1
            write('''    """
''')
            for line in VFN(VFFSL(SL,"self",True),"line_gen",False)(VFFSL(SL,"desc",True)): # generated from line 49, col 5
                write('''    ''')
                _v = VFFSL(SL,"line",True) # '$line' on line 50, col 5
                if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 50, col 5.
                write('''
''')
            if VFFSL(SL,"link",True): # generated from line 52, col 5
                write('''
    See Also:
        `API ''')
                _v = VFFSL(SL,"name",True) # '$name' on line 55, col 14
                if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 55, col 14.
                write(''' <''')
                _v = VFFSL(SL,"link",True) # '$link' on line 55, col 21
                if _v is not None: write(_filter(_v, rawExpr='$link')) # from line 55, col 21.
                write('''>`_
''')
            write('''    """

''')
        if VFFSL(SL,"is_properties",True): # generated from line 60, col 1
            properties = VFFSL(SL,"attribs",True)['properties']
            for property in VFFSL(SL,"properties",True): # generated from line 62, col 1
                p_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"property",True)['name'])
                p_type = VFFSL(SL,"property",True)['returns']
                p_desc = VFFSL(SL,"property",True)['desc']
                write('''    ''')
                _v = VFFSL(SL,"p_name",True) # '${p_name}' on line 66, col 5
                if _v is not None: write(_filter(_v, rawExpr='${p_name}')) # from line 66, col 5.
                write(''': ''')
                _v = VFN(VFFSL(SL,"self",True),"get_q_type",False)(VFFSL(SL,"p_type",True)) # '$self.get_q_type($p_type)' on line 66, col 16
                if _v is not None: write(_filter(_v, rawExpr='$self.get_q_type($p_type)')) # from line 66, col 16.
                write(''' = ...
''')
                if VFFSL(SL,"include_desc",True): # generated from line 67, col 5
                    write('''    """
''')
                    for line in VFN(VFFSL(SL,"self",True),"line_gen",False)(VFFSL(SL,"p_desc",True)): # generated from line 69, col 5
                        write('''    ''')
                        _v = VFFSL(SL,"line",True) # '$line' on line 70, col 5
                        if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 70, col 5.
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

    name = ""

    desc = []

    quote = set()

    typings = set()

    link = ""

    requires_typing = False

    include_desc = True

    inherits = []

    imports = []

    from_imports = []

    from_imports_typing = []

    namespace = ""

    attribs = {}

    _mainCheetahMethod_for_singleton = 'respond'

## END CLASS DEFINITION

if not hasattr(singleton, '_initCheetahAttributes'):
    templateAPIClass = getattr(singleton,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(singleton)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=singleton()).run()


