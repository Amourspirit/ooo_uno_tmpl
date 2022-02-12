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
from _base_struct_dyn import BaseStructDyn

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post2'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 2)
__CHEETAH_genTime__ = 1644703040.111799
__CHEETAH_genTimestamp__ = 'Sat Feb 12 16:57:20 2022'
__CHEETAH_src__ = '_struct_dyn.tmpl'
__CHEETAH_srcLastModified__ = 'Sat Feb 12 16:57:12 2022'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class struct_dyn(BaseStructDyn):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(struct_dyn, self).__init__(*args, **KWs)
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
        #   following attr will get values from BaseStructDyn class
        _v = VFN(VFFSL(SL,"self",True),"load_data",False)() # '$self.load_data()' on line 27, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.load_data()')) # from line 27, col 1.
        #  Main Template
        safe_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"name",True))
        fullname = VFFSL(SL,"namespace",True) + '.' + VFFSL(SL,"safe_name",True)
        uno_obj_ns = VFFSL(SL,"dyn",True) + VFN(VFN(VFFSL(SL,"fullname",True),"removeprefix",False)('com.sun.star'),"rsplit",False)(sep='.', maxsplit=1)[0]
        uno_obj_in = VFFSL(SL,"uno_obj",True) + VFN(VFFSL(SL,"fullname",True),"removeprefix",False)('com.sun.star')
        sorted = VFN(VFFSL(SL,"self",True),"get_sorted_names",False)()
        if False:
            _
        _, first_index = VFFSL(SL,"sorted",True)[0]
        first_itm = VFFSL(SL,"attribs",True)[VFFSL(SL,"first_index",True)]
        first_itm_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"first_itm",True)['name'])
        write('''# coding: utf-8
''')
        self._handleCheetahInclude("resources/inc_lic.txt", trans=trans, includeFrom="file", raw=True)
        write('''# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: ''')
        _v = VFFSL(SL,"namespace",True) # '$namespace' on line 41, col 14
        if _v is not None: write(_filter(_v, rawExpr='$namespace')) # from line 41, col 14.
        write('''
''')
        if VFFSL(SL,"libre_office_ver",True): # generated from line 42, col 1
            write('''# Libre Office Version: ''')
            _v = VFFSL(SL,"libre_office_ver",True) # '$libre_office_ver' on line 43, col 25
            if _v is not None: write(_filter(_v, rawExpr='$libre_office_ver')) # from line 43, col 25.
            write('''
''')
        write('''from typing import TYPE_CHECKING
from ''')
        _v = VFFSL(SL,"oenv",True) # '$oenv' on line 46, col 6
        if _v is not None: write(_filter(_v, rawExpr='$oenv')) # from line 46, col 6.
        write(''' import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from ''')
        _v = VFFSL(SL,"namespace",True) # '$namespace' on line 54, col 14
        if _v is not None: write(_filter(_v, rawExpr='$namespace')) # from line 54, col 14.
        write(''' import ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 54, col 32
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 54, col 32.
        write(''' as U''')
        _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 54, col 47
        if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 54, col 47.
        write('''
        # Dynamically create uno ''')
        _v = VFFSL(SL,"fullname",True) # '$fullname' on line 55, col 34
        if _v is not None: write(_filter(_v, rawExpr='$fullname')) # from line 55, col 34.
        write(''' using uno
        global ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 56, col 16
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 56, col 16.
        write("""

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = '""")
        _v = VFFSL(SL,"namespace",True) # '$namespace' on line 59, col 46
        if _v is not None: write(_filter(_v, rawExpr='$namespace')) # from line 59, col 46.
        write("""'
            struct.__dict__['__ooo_full_ns__'] = '""")
        _v = VFFSL(SL,"fullname",True) # '$fullname' on line 60, col 51
        if _v is not None: write(_filter(_v, rawExpr='$fullname')) # from line 60, col 51.
        write("""'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        """)
        _v = VFN(VFFSL(SL,"self",True),"get_dyn_fn",False)() # '$self.get_dyn_fn()' on line 63, col 9
        if _v is not None: write(_filter(_v, rawExpr='$self.get_dyn_fn()')) # from line 63, col 9.
        write("""
            ns = '""")
        _v = VFFSL(SL,"fullname",True) # '${fullname}' on line 64, col 19
        if _v is not None: write(_filter(_v, rawExpr='${fullname}')) # from line 64, col 19.
        write("""'
            if isinstance(""")
        _v = VFFSL(SL,"first_itm_name",True) # '$first_itm_name' on line 65, col 27
        if _v is not None: write(_filter(_v, rawExpr='$first_itm_name')) # from line 65, col 27.
        write(''', U''')
        _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 65, col 45
        if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 65, col 45.
        write('''):
                inst = uno.createUnoStruct(ns, ''')
        _v = VFFSL(SL,"first_itm_name",True) # '$first_itm_name' on line 66, col 48
        if _v is not None: write(_filter(_v, rawExpr='$first_itm_name')) # from line 66, col 48.
        write(''')
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

''')
        for i, tpl in enumerate(VFFSL(SL,"sorted",True)): # generated from line 71, col 1
            index = tpl[1]
            itm = VFFSL(SL,"attribs",True)[VFFSL(SL,"index",True)]
            itm_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"itm",True)['name'])
            attrib_default = VFN(VFFSL(SL,"self",True),"get_attrib_default",False)(VFFSL(SL,"itm",True), True)
            write('''            if not ''')
            _v = VFFSL(SL,"itm_name",True) # '$itm_name' on line 76, col 20
            if _v is not None: write(_filter(_v, rawExpr='$itm_name')) # from line 76, col 20.
            write(""" is UNO_NONE:
                setattr(struct, '""")
            _v = VFFSL(SL,"itm_name",True) # '$itm_name' on line 77, col 34
            if _v is not None: write(_filter(_v, rawExpr='$itm_name')) # from line 77, col 34.
            write("""', """)
            _v = VFFSL(SL,"itm_name",True) # '$itm_name' on line 77, col 46
            if _v is not None: write(_filter(_v, rawExpr='$itm_name')) # from line 77, col 46.
            write(''')
''')
            #  if getattr(struct, '$itm_name') != $itm_name:
            #      setattr(struct, '$itm_name', $itm_name)
        write('''            _set_attr(struct)
            return struct
        ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 83, col 9
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 83, col 9.
        write(''' = _struct_init

    _dynamic_struct()
else:
    ''')
        _v = VFN(VFFSL(SL,"self",True),"get_rel_import",False)(in_str=VFFSL(SL,"uno_obj_in",True), ns=VFFSL(SL,"uno_obj_ns",True)) # '$self.get_rel_import(in_str=$uno_obj_in, ns=$uno_obj_ns)' on line 87, col 5
        if _v is not None: write(_filter(_v, rawExpr='$self.get_rel_import(in_str=$uno_obj_in, ns=$uno_obj_ns)')) # from line 87, col 5.
        write(''' as ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 87, col 65
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 87, col 65.
        write("""

__all__ = ['""")
        _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 89, col 13
        if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 89, col 13.
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

    dynamic_struct = True

    sort = True 

    name = ""

    namespace = ''

    allow_db = True

    libre_office_ver = False

    desc = "" 

    include_desc = True

    link = ""

    requires_typing = False

    inherits = []

    imports = []

    extends_map = {}

    from_imports = []

    from_imports_typing = []

    quote = set()

    typings = set()

    attribs = {}

    uno_obj = ''

    dyn = ''

    oenv = ''

    _mainCheetahMethod_for_struct_dyn = 'respond'

## END CLASS DEFINITION

if not hasattr(struct_dyn, '_initCheetahAttributes'):
    templateAPIClass = getattr(struct_dyn,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(struct_dyn)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=struct_dyn()).run()


