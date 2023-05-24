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
from _base_singleton_dyn import BaseSingletonDyn

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post1'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 1)
__CHEETAH_genTime__ = 1684880550.688086
__CHEETAH_genTimestamp__ = 'Tue May 23 18:22:30 2023'
__CHEETAH_src__ = '_singleton_dyn.tmpl'
__CHEETAH_srcLastModified__ = 'Tue May 23 18:16:54 2023'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class singleton_dyn(BaseSingletonDyn):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(singleton_dyn, self).__init__(*args, **KWs)
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
        #   following attr will get values from BaseInterfaceDyn class
        _v = VFN(VFFSL(SL,"self",True),"load_data",False)() # '$self.load_data()' on line 28, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.load_data()')) # from line 28, col 1.
        #  main Template
        safe_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"name",True))
        fullname = VFFSL(SL,"namespace",True) + '.' + VFFSL(SL,"safe_name",True)
        uno_obj_ns = VFFSL(SL,"dyn",True) + VFN(VFN(VFFSL(SL,"fullname",True),"removeprefix",False)('com.sun.star'),"rsplit",False)(sep='.', maxsplit=1)[0]
        uno_obj_in = VFFSL(SL,"uno_obj",True) + VFN(VFFSL(SL,"fullname",True),"removeprefix",False)('com.sun.star')
        # 
        # The following singleton service is not found in ctx
        # '/singletons/com.sun.star.script.theServiceDocumenter'
        # 
        # However the following is found:
        # '/singletons/com.sun.star.util.theServiceDocumenter'
        # 
        # SupportedServiceNames for this class however does include
        # 'com.sun.star.script.ServiceDocumenter'
        # 
        # This is the only case that pattern does not follow: '/singletons/' + $fullname
        if VFFSL(SL,"fullname",True) == 'com.sun.star.script.theServiceDocumenter': # generated from line 46, col 1
            name_value = '/singletons/com.sun.star.util.theServiceDocumenter'
        else: # generated from line 48, col 1
            name_value = '/singletons/' + VFFSL(SL,"fullname",True)
        write('''# coding: utf-8
''')
        self._handleCheetahInclude("resources/inc_lic.txt", trans=trans, includeFrom="file", raw=True)
        write('''# Singleton Class
# this is a auto generated file generated by Cheetah
''')
        if VFFSL(SL,"libre_office_ver",True): # generated from line 55, col 1
            write('''# Libre Office Version: ''')
            _v = VFFSL(SL,"libre_office_ver",True) # '$libre_office_ver' on line 56, col 25
            if _v is not None: write(_filter(_v, rawExpr='$libre_office_ver')) # from line 56, col 25.
            write('''
''')
        write('''# Namespace: ''')
        _v = VFFSL(SL,"namespace",True) # '$namespace' on line 58, col 14
        if _v is not None: write(_filter(_v, rawExpr='$namespace')) # from line 58, col 14.
        write('''
from typing import TYPE_CHECKING
from ''')
        _v = VFFSL(SL,"oenv",True) # '$oenv' on line 60, col 6
        if _v is not None: write(_filter(_v, rawExpr='$oenv')) # from line 60, col 6.
        write(''' import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False

if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_singleton() -> None:
        # Dynamically create uno singleton using component context
        import uno
        global ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 70, col 16
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 70, col 16.
        write("""

        def _singleton_init():
            ctx = uno.getComponentContext()
            key = '""")
        _v = VFFSL(SL,"name_value",True) # '$name_value' on line 74, col 20
        if _v is not None: write(_filter(_v, rawExpr='$name_value')) # from line 74, col 20.
        write("""'
            singleton = ctx.getByName(key)
            return singleton
        """)
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 77, col 9
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 77, col 9.
        write(''' = _singleton_init
    _dynamic_singleton()
else:
    if TYPE_CHECKING
        from ''')
        _v = VFFSL(SL,"namespace",True) # '$namespace' on line 81, col 14
        if _v is not None: write(_filter(_v, rawExpr='$namespace')) # from line 81, col 14.
        write(''' import ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 81, col 32
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 81, col 32.
        write(''' as ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 81, col 46
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 81, col 46.
        write('''
    else:
        ''')
        _v = VFN(VFFSL(SL,"self",True),"get_rel_import",False)(in_str=VFFSL(SL,"uno_obj_in",True), ns=VFFSL(SL,"uno_obj_ns",True)) # '$self.get_rel_import(in_str=$uno_obj_in, ns=$uno_obj_ns)' on line 83, col 9
        if _v is not None: write(_filter(_v, rawExpr='$self.get_rel_import(in_str=$uno_obj_in, ns=$uno_obj_ns)')) # from line 83, col 9.
        write(''' as ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 83, col 69
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 83, col 69.
        write("""

__all__ = ['""")
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 85, col 13
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 85, col 13.
        write("""']""")
        
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

    namespace = ""

    allow_db = True

    libre_office_ver = False

    desc = []

    quote = set()

    typings = set()

    link = ""

    requires_typing = False

    include_desc = True

    inherits = []

    imports = []

    extends_map = {}

    from_imports = []

    from_imports_typing = []

    attribs = {}

    uno_obj = ''

    dyn = ''

    oenv = ''

    _mainCheetahMethod_for_singleton_dyn = 'respond'

## END CLASS DEFINITION

if not hasattr(singleton_dyn, '_initCheetahAttributes'):
    templateAPIClass = getattr(singleton_dyn,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(singleton_dyn)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=singleton_dyn()).run()


