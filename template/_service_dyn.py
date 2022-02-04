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
from _base_service_dyn import BaseServiceDyn

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post2'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 2)
__CHEETAH_genTime__ = 1643936506.6625347
__CHEETAH_genTimestamp__ = 'Thu Feb  3 20:01:46 2022'
__CHEETAH_src__ = '_service_dyn.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Feb  3 19:53:57 2022'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class service_dyn(BaseServiceDyn):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(service_dyn, self).__init__(*args, **KWs)
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
        #   following attr will get values from BaseServiceDyn class
        _v = VFN(VFFSL(SL,"self",True),"load_data",False)() # '$self.load_data()' on line 23, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.load_data()')) # from line 23, col 1.
        #  main Template
        safe_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"name",True))
        fullname = VFFSL(SL,"namespace",True) + '.' + VFFSL(SL,"safe_name",True)
        uno_obj_ns = VFFSL(SL,"dyn",True) + VFN(VFN(VFFSL(SL,"fullname",True),"removeprefix",False)('com.sun.star'),"rsplit",False)(sep='.', maxsplit=1)[0]
        uno_obj_in = VFFSL(SL,"uno_obj",True) + VFN(VFFSL(SL,"fullname",True),"removeprefix",False)('com.sun.star')
        write('''# coding: utf-8
''')
        self._handleCheetahInclude("resources/inc_lic.txt", trans=trans, includeFrom="file", raw=True)
        write('''# Service Class
# this is a auto generated file generated by Cheetah
''')
        if VFFSL(SL,"libre_office_ver",True): # generated from line 33, col 1
            write('''# Libre Office Version: ''')
            _v = VFFSL(SL,"libre_office_ver",True) # '$libre_office_ver' on line 34, col 25
            if _v is not None: write(_filter(_v, rawExpr='$libre_office_ver')) # from line 34, col 25.
            write('''
# Namespace: ''')
            _v = VFFSL(SL,"namespace",True) # '$namespace' on line 35, col 14
            if _v is not None: write(_filter(_v, rawExpr='$namespace')) # from line 35, col 14.
            write('''
''')
        write('''
from typing import TYPE_CHECKING, Optional, Iterable, Union
''')
        _v = VFN(VFFSL(SL,"self",True),"get_rel_import",False)(in_str=VFFSL(SL,"uno_obj_in",True), ns=VFFSL(SL,"uno_obj_ns",True)) # '$self.get_rel_import(in_str=$uno_obj_in, ns=$uno_obj_ns)' on line 39, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.get_rel_import(in_str=$uno_obj_in, ns=$uno_obj_ns)')) # from line 39, col 1.
        write(''' as ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 39, col 61
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 39, col 61.
        write('''
''')
        #  from ...uno_obj.accessibility.accessible_context import AccessibleContext as AccessibleContext
        write('''from ooo_uno.helper import uno_helper
if TYPE_CHECKING:
''')
        #  from ...uno_obj.uno.x_component_context import XComponentContext
        write('''    ''')
        _v = VFN(VFFSL(SL,"self",True),"get_rel_import",False)(in_str='uno_obj.uno.XComponentContext', ns=VFFSL(SL,"uno_obj_ns",True)) # "$self.get_rel_import(in_str='uno_obj.uno.XComponentContext', ns=$uno_obj_ns)" on line 44, col 5
        if _v is not None: write(_filter(_v, rawExpr="$self.get_rel_import(in_str='uno_obj.uno.XComponentContext', ns=$uno_obj_ns)")) # from line 44, col 5.
        write(""" as XComponentContext

def create_service(ctx: 'Optional[XComponentContext]' = None, args: Optional[Iterable[object]] = None) -> Union[""")
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 46, col 113
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 46, col 113.
        write(''', None]:
    """
    Create ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 48, col 12
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 48, col 12.
        write(''' service using ServiceManager Factory

    Args:
        ctx (XComponentContext, optional): context used to create service. Defaults to ``None``.
        args (Iterable[object], optional): args that are passed to ServiceManager . Defaults to ``None``.

    Returns:
        Union[''')
        _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 55, col 15
        if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 55, col 15.
        write(''', None]: Service if it is available; Otherwise, ``None``
    """
    return uno_helper.create_uno_service(cClass=\'''')
        _v = VFFSL(SL,"fullname",True) # '${fullname}' on line 57, col 50
        if _v is not None: write(_filter(_v, rawExpr='${fullname}')) # from line 57, col 50.
        write("""', ctx=ctx, args=args)

__all__ = ['""")
        _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 59, col 13
        if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 59, col 13.
        write("""', 'create_service']
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

    name = ""

    namespace = ""

    allow_db = True

    libre_office_ver = False

    desc = []

    quote = set()

    typings = set()

    link = ""

    requires_typing = False

    inherits = []

    extends_map = {}

    imports = []

    from_imports = []

    from_imports_typing = []

    attribs = {}

    uno_obj = 'uno_obj'

    dyn = 'dyn'

    _mainCheetahMethod_for_service_dyn = 'respond'

## END CLASS DEFINITION

if not hasattr(service_dyn, '_initCheetahAttributes'):
    templateAPIClass = getattr(service_dyn,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(service_dyn)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=service_dyn()).run()


