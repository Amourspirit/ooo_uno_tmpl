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
from _base_struct_pyi import BaseStructPyi
import re

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post2'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 2)
__CHEETAH_genTime__ = 1649893414.7212512
__CHEETAH_genTimestamp__ = 'Wed Apr 13 19:43:34 2022'
__CHEETAH_src__ = '_struct_pyi.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr 13 19:43:28 2022'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class struct_pyi(BaseStructPyi):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(struct_pyi, self).__init__(*args, **KWs)
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
        
        _v = VFN(VFFSL(SL,"self",True),"init_data",False)() # '$self.init_data()' on line 5, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.init_data()')) # from line 5, col 1.
        #  set is attribs is sorted
        #   following attr will get values from Base class
        _v = VFN(VFFSL(SL,"self",True),"load_data",False)() # '$self.load_data()' on line 27, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.load_data()')) # from line 27, col 1.
        #  Main Template
        re_underscore_hex = r"(_[0-9A-Fa-f]*)"
        safe_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"name",True))
        sorted = VFN(VFFSL(SL,"self",True),"get_sorted_names",False)()
        is_parent = VFN(VFFSL(SL,"self",True),"has_uno_extends",False)()
        is_local_args = VFN(VFFSL(SL,"self",True),"is_inst_args",False)()
        is_non_local_args = VFN(VFFSL(SL,"self",True),"is_parent_args",False)()
        args_all = VFN(VFFSL(SL,"self",True),"get_class_args_all",False)()
        args_local = VFN(VFFSL(SL,"self",True),"get_class_args_inst",False)()
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
        write('''from typing_extensions import Literal
''')
        for imp in VFFSL(SL,"imports",True): # generated from line 46, col 1
            write('''import ''')
            _v = VFFSL(SL,"imp",True) # '$imp' on line 47, col 8
            if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 47, col 8.
            write('''
''')
        for imp in VFFSL(SL,"from_imports",True): # generated from line 49, col 1
            _v = VFN(VFFSL(SL,"self",True),"get_from_import",False)(VFFSL(SL,"name",True), VFFSL(SL,"imp",True)) # '$self.get_from_import($name, $imp)' on line 50, col 1
            if _v is not None: write(_filter(_v, rawExpr='$self.get_from_import($name, $imp)')) # from line 50, col 1.
            write('''
''')
        if VFFSL(SL,"requires_typing",True) or len(VFFSL(SL,"sorted",True)) > 0: # generated from line 52, col 1
            write('''import typing
''')
        if len(VFFSL(SL,"from_imports_typing",True)) > 0: # generated from line 55, col 1
            #  if typing.TYPE_CHECKING:
            for imp in VFFSL(SL,"from_imports_typing",True): # generated from line 57, col 1
                _v = VFN(VFFSL(SL,"self",True),"get_from_import",False)(VFFSL(SL,"name",True), VFFSL(SL,"imp",True)) # '$self.get_from_import($name, $imp)' on line 58, col 1
                if _v is not None: write(_filter(_v, rawExpr='$self.get_from_import($name, $imp)')) # from line 58, col 1.
                write('''
''')
        write('''

''')
        if VFFSL(SL,"allow_db",True): # generated from line 63, col 1
            write('''class ''')
            _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 64, col 7
            if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 64, col 7.
            write('''(''')
            _v = VFN(VFFSL(SL,"self",True),"get_class_inherits_from_db",False)() # '$self.get_class_inherits_from_db()' on line 64, col 20
            if _v is not None: write(_filter(_v, rawExpr='$self.get_class_inherits_from_db()')) # from line 64, col 20.
            write('''):
''')
        else: # generated from line 65, col 1
            write('''class ''')
            _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 66, col 7
            if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 66, col 7.
            write('''(''')
            _v = VFN(VFFSL(SL,"self",True),"get_class_inherits",False)(VFFSL(SL,"name",True), VFFSL(SL,"inherits",True)) # '$self.get_class_inherits($name, $inherits)' on line 66, col 20
            if _v is not None: write(_filter(_v, rawExpr='$self.get_class_inherits($name, $inherits)')) # from line 66, col 20.
            write('''):
''')
        if VFFSL(SL,"include_desc",True): # generated from line 68, col 1
            write('''    """
    Struct Class

''')
            if isinstance(VFFSL(SL,"desc",True), str): # generated from line 72, col 5
                write('''    ''')
                _v = VFFSL(SL,"desc",True) # '$desc' on line 73, col 5
                if _v is not None: write(_filter(_v, rawExpr='$desc')) # from line 73, col 5.
                write('''
''')
            else: # generated from line 74, col 5
                for line in VFFSL(SL,"desc",True): # generated from line 75, col 9
                    write('''    ''')
                    _v = VFFSL(SL,"line",True) # '$line' on line 76, col 5
                    if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 76, col 5.
                    write('''
''')
            if VFFSL(SL,"link",True): # generated from line 79, col 5
                write('''
    See Also:
        `API ''')
                _v = VFFSL(SL,"name",True) # '$name' on line 82, col 14
                if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 82, col 14.
                write(''' <''')
                _v = VFFSL(SL,"link",True) # '$link' on line 82, col 21
                if _v is not None: write(_filter(_v, rawExpr='$link')) # from line 82, col 21.
                write('''>`_
''')
            write('''    """
''')
        write("""    typeName: Literal['""")
        _v = VFFSL(SL,"fullname",True) # '$fullname' on line 86, col 24
        if _v is not None: write(_filter(_v, rawExpr='$fullname')) # from line 86, col 24.
        write("""']

""")
        if False:
            _
        _, first_index = VFFSL(SL,"sorted",True)[0]
        first_itm = VFFSL(SL,"attribs",True)[VFFSL(SL,"first_index",True)]
        first_itm_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"first_itm",True)['name'])
        write('''    ''')
        _v = VFN(VFFSL(SL,"self",True),"get_constructor",False)() # '$self.get_constructor()' on line 91, col 5
        if _v is not None: write(_filter(_v, rawExpr='$self.get_constructor()')) # from line 91, col 5.
        write('''
        """
        Constructor

        Arguments:
''')
        for arg in VFFSL(SL,"args_all",True): # generated from line 96, col 1
            arg_type = re.sub(re_underscore_hex, '', VFFSL(SL,"arg.type",True), 1)
            write('''            ''')
            _v = VFFSL(SL,"arg.name",True) # '$arg.name' on line 98, col 13
            if _v is not None: write(_filter(_v, rawExpr='$arg.name')) # from line 98, col 13.
            write(''' (''')
            _v = VFFSL(SL,"arg_type",True) # '$arg_type' on line 98, col 24
            if _v is not None: write(_filter(_v, rawExpr='$arg_type')) # from line 98, col 24.
            write(''', optional): ''')
            _v = VFFSL(SL,"arg.name",True) # '$arg.name' on line 98, col 46
            if _v is not None: write(_filter(_v, rawExpr='$arg.name')) # from line 98, col 46.
            write(''' value.
''')
        write('''        """

''')
        for i, tpl in enumerate(VFFSL(SL,"sorted",True)): # generated from line 102, col 1
            index = tpl[1]
            itm = VFN(VFFSL(SL,"self",True),"get_attrib_for_prop",False)(VFFSL(SL,"index",True))
            itm_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"itm",True)['name'])
            write('''
    @property
    def ''')
            _v = VFFSL(SL,"itm_name",True) # '${itm_name}' on line 108, col 9
            if _v is not None: write(_filter(_v, rawExpr='${itm_name}')) # from line 108, col 9.
            write('''(self) -> ''')
            _v = VFFSL(SL,"itm",True)['type'] # "$itm['type']" on line 108, col 30
            if _v is not None: write(_filter(_v, rawExpr="$itm['type']")) # from line 108, col 30.
            write(''':
''')
            if VFFSL(SL,"include_desc",True) and VFFSL(SL,"itm",True)['desc']: # generated from line 109, col 1
                write('''        """
''')
                if isinstance(VFFSL(SL,"itm",True)['desc'], str): # generated from line 111, col 5
                    write('''        ''')
                    _v = VFFSL(SL,"itm",True)['desc'] # "$itm['desc']" on line 112, col 9
                    if _v is not None: write(_filter(_v, rawExpr="$itm['desc']")) # from line 112, col 9.
                    write('''
''')
                else: # generated from line 113, col 5
                    for line in VFFSL(SL,"itm",True)['desc']: # generated from line 114, col 9
                        write('''        ''')
                        _v = VFFSL(SL,"line",True) # '$line' on line 115, col 9
                        if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 115, col 9.
                        write('''
''')
                write('''        """
''')
            write('''
''')
        write("""

__all__ = ['""")
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 124, col 13
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 124, col 13.
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

    dynamic_struct = False

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

    attribs = []

    fullname = ''

    oenv = 'ooo.oenv.env_const'

    _mainCheetahMethod_for_struct_pyi = 'respond'

## END CLASS DEFINITION

if not hasattr(struct_pyi, '_initCheetahAttributes'):
    templateAPIClass = getattr(struct_pyi,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(struct_pyi)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=struct_pyi()).run()


