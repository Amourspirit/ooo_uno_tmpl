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
from _base_struct import BaseStruct
import re

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post2'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 2)
__CHEETAH_genTime__ = 1644630561.5292215
__CHEETAH_genTimestamp__ = 'Fri Feb 11 20:49:21 2022'
__CHEETAH_src__ = '_struct_base.tmpl'
__CHEETAH_srcLastModified__ = 'Fri Feb 11 20:46:28 2022'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class struct_base(BaseStruct):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(struct_base, self).__init__(*args, **KWs)
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
        _v = VFN(VFFSL(SL,"self",True),"load_data",False)() # '$self.load_data()' on line 25, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.load_data()')) # from line 25, col 1.
        #  Main Template
        re_underscore_hex = r"(_[0-9A-Fa-f]*)"
        safe_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"name",True))
        sorted = VFN(VFFSL(SL,"self",True),"get_sorted_names",False)()
        write('''# coding: utf-8
''')
        self._handleCheetahInclude("resources/inc_lic.txt", trans=trans, includeFrom="file", raw=True)
        write('''# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: ''')
        _v = VFFSL(SL,"namespace",True) # '$namespace' on line 34, col 14
        if _v is not None: write(_filter(_v, rawExpr='$namespace')) # from line 34, col 14.
        write('''
''')
        if VFFSL(SL,"libre_office_ver",True): # generated from line 35, col 1
            write('''# Libre Office Version: ''')
            _v = VFFSL(SL,"libre_office_ver",True) # '$libre_office_ver' on line 36, col 25
            if _v is not None: write(_filter(_v, rawExpr='$libre_office_ver')) # from line 36, col 25.
            write('''
''')
        if len(VFFSL(SL,"sorted",True)) > 0: # generated from line 38, col 1
            write('''from ooo.oenv import UNO_NONE
''')
        for imp in VFFSL(SL,"imports",True): # generated from line 41, col 1
            write('''import ''')
            _v = VFFSL(SL,"imp",True) # '$imp' on line 42, col 8
            if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 42, col 8.
            write('''
''')
        for imp in VFFSL(SL,"from_imports",True): # generated from line 44, col 1
            _v = VFN(VFFSL(SL,"self",True),"get_from_import",False)(VFFSL(SL,"name",True), VFFSL(SL,"imp",True)) # '$self.get_from_import($name, $imp)' on line 45, col 1
            if _v is not None: write(_filter(_v, rawExpr='$self.get_from_import($name, $imp)')) # from line 45, col 1.
            write('''
''')
        if VFFSL(SL,"requires_typing",True) or len(VFFSL(SL,"sorted",True)) > 0: # generated from line 47, col 1
            write('''import typing
''')
        if len(VFFSL(SL,"from_imports_typing",True)) > 0: # generated from line 50, col 1
            #  if typing.TYPE_CHECKING:
            for imp in VFFSL(SL,"from_imports_typing",True): # generated from line 52, col 1
                _v = VFN(VFFSL(SL,"self",True),"get_from_import",False)(VFFSL(SL,"name",True), VFFSL(SL,"imp",True)) # '$self.get_from_import($name, $imp)' on line 53, col 1
                if _v is not None: write(_filter(_v, rawExpr='$self.get_from_import($name, $imp)')) # from line 53, col 1.
                write('''
''')
        write('''

''')
        if VFFSL(SL,"allow_db",True): # generated from line 58, col 1
            write('''class ''')
            _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 59, col 7
            if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 59, col 7.
            write('''(''')
            _v = VFN(VFFSL(SL,"self",True),"get_class_inherits_from_db",False)() # '$self.get_class_inherits_from_db()' on line 59, col 20
            if _v is not None: write(_filter(_v, rawExpr='$self.get_class_inherits_from_db()')) # from line 59, col 20.
            write('''):
''')
        else: # generated from line 60, col 1
            write('''class ''')
            _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 61, col 7
            if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 61, col 7.
            write('''(''')
            _v = VFN(VFFSL(SL,"self",True),"get_class_inherits",False)(VFFSL(SL,"name",True), VFFSL(SL,"inherits",True)) # '$self.get_class_inherits($name, $inherits)' on line 61, col 20
            if _v is not None: write(_filter(_v, rawExpr='$self.get_class_inherits($name, $inherits)')) # from line 61, col 20.
            write('''):
''')
        if VFFSL(SL,"include_desc",True): # generated from line 63, col 1
            write('''    """
    Struct Class

''')
            if isinstance(VFFSL(SL,"desc",True), str): # generated from line 67, col 5
                write('''    ''')
                _v = VFFSL(SL,"desc",True) # '$desc' on line 68, col 5
                if _v is not None: write(_filter(_v, rawExpr='$desc')) # from line 68, col 5.
                write('''
''')
            else: # generated from line 69, col 5
                for line in VFFSL(SL,"desc",True): # generated from line 70, col 9
                    write('''    ''')
                    _v = VFFSL(SL,"line",True) # '$line' on line 71, col 5
                    if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 71, col 5.
                    write('''
''')
            if VFFSL(SL,"link",True): # generated from line 74, col 5
                write('''
    See Also:
        `API ''')
                _v = VFFSL(SL,"name",True) # '$name' on line 77, col 14
                if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 77, col 14.
                write(''' <''')
                _v = VFFSL(SL,"link",True) # '$link' on line 77, col 21
                if _v is not None: write(_filter(_v, rawExpr='$link')) # from line 77, col 21.
                write('''>`_
''')
            write('''    """
''')
        write("""    __ooo_ns__: str = '""")
        _v = VFFSL(SL,"namespace",True) # '$namespace' on line 81, col 24
        if _v is not None: write(_filter(_v, rawExpr='$namespace')) # from line 81, col 24.
        write("""'
    __ooo_full_ns__: str = '""")
        _v = VFFSL(SL,"fullname",True) # '$fullname' on line 82, col 29
        if _v is not None: write(_filter(_v, rawExpr='$fullname')) # from line 82, col 29.
        write("""'
    __ooo_type_name__: str = 'struct'
""")
        #  typeName: Literal requires python >= 3.8
        write("""    typeName: str = '""")
        _v = VFFSL(SL,"fullname",True) # '$fullname' on line 85, col 22
        if _v is not None: write(_filter(_v, rawExpr='$fullname')) # from line 85, col 22.
        write('''\'
    """Literal Constant ``''')
        _v = VFFSL(SL,"fullname",True) # '$fullname' on line 86, col 27
        if _v is not None: write(_filter(_v, rawExpr='$fullname')) # from line 86, col 27.
        write('''``"""

''')
        #     def __init__(self, *args, **kwargs):
        write('''    def __init__(self, *args, **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 94, col 50
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 94, col 50.
        write('''`` instance,
                if it is the only arg passed to contructor;
                Otherwise, postitional arguments are treated as ``''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 96, col 67
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 96, col 67.
        write('''``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
''')
        for i, tpl in enumerate(VFFSL(SL,"sorted",True)): # generated from line 100, col 1
            index = tpl[1]
            itm = VFFSL(SL,"attribs",True)[VFFSL(SL,"index",True)]
            itm_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"itm.name",True))
            itm_type = VFN(VFFSL(SL,"itm.type",True),"removeprefix",False)('typing.')
            itm_type = re.sub(re_underscore_hex, '', VFFSL(SL,"itm_type",True), 1)
            write('''            ''')
            _v = VFFSL(SL,"itm_name",True) # '$itm_name' on line 106, col 13
            if _v is not None: write(_filter(_v, rawExpr='$itm_name')) # from line 106, col 13.
            write(''' (''')
            _v = VFFSL(SL,"itm_type",True) # '$itm_type' on line 106, col 24
            if _v is not None: write(_filter(_v, rawExpr='$itm_type')) # from line 106, col 24.
            write(''', optional): ''')
            _v = VFFSL(SL,"itm_name",True) # '$itm_name' on line 106, col 46
            if _v is not None: write(_filter(_v, rawExpr='$itm_name')) # from line 106, col 46.
            write(''' value
''')
        write('''        """
''')
        if VFN(VFFSL(SL,"self",True),"has_uno_extends",False)(): # generated from line 109, col 1
            write('''        super().__init__(*args, **kwargs)
''')
        write('''
        if len(args) == 1 and isinstance(args[0], ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 113, col 51
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 113, col 51.
        write('''):
            oth: ''')
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 114, col 18
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 114, col 18.
        write(''' = args[0]
''')
        for i, tpl in enumerate(VFFSL(SL,"sorted",True)): # generated from line 115, col 1
            index = tpl[1]
            itm = VFFSL(SL,"attribs",True)[VFFSL(SL,"index",True)]
            itm_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"itm.name",True))
            attrib_default = VFN(VFFSL(SL,"self",True),"get_attrib_default",False)(VFFSL(SL,"itm",True))
            write('''            self._''')
            _v = VFN(VFFSL(SL,"self",True),"camel_to_snake",False)(VFFSL(SL,"itm_name",True)) # '$self.camel_to_snake($itm_name)' on line 120, col 19
            if _v is not None: write(_filter(_v, rawExpr='$self.camel_to_snake($itm_name)')) # from line 120, col 19.
            write(''' = oth.''')
            _v = VFFSL(SL,"itm_name",True) # '$itm_name' on line 120, col 57
            if _v is not None: write(_filter(_v, rawExpr='$itm_name')) # from line 120, col 57.
            write('''
''')
        write('''            return
        else:
''')
        for i, tpl in enumerate(VFFSL(SL,"sorted",True)): # generated from line 124, col 1
            index = tpl[1]
            itm = VFFSL(SL,"attribs",True)[VFFSL(SL,"index",True)]
            itm_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"itm.name",True))
            attrib_default = VFN(VFFSL(SL,"self",True),"get_attrib_default",False)(VFFSL(SL,"itm",True))
            write('''            self._''')
            _v = VFN(VFFSL(SL,"self",True),"camel_to_snake",False)(VFFSL(SL,"itm_name",True)) # '$self.camel_to_snake($itm_name)' on line 129, col 19
            if _v is not None: write(_filter(_v, rawExpr='$self.camel_to_snake($itm_name)')) # from line 129, col 19.
            write(''' = ''')
            _v = VFN(VFFSL(SL,"self",True),"get_attrib_default",False)(VFFSL(SL,"itm",True)) # '$self.get_attrib_default($itm)' on line 129, col 53
            if _v is not None: write(_filter(_v, rawExpr='$self.get_attrib_default($itm)')) # from line 129, col 53.
            write('''
''')
        write('''
        key_order = (''')
        _v = VFN(VFFSL(SL,"self",True),"get_nt_names_str",False)() # '$self.get_nt_names_str()' on line 132, col 22
        if _v is not None: write(_filter(_v, rawExpr='$self.get_nt_names_str()')) # from line 132, col 22.
        write(''')
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
''')
        #  use hasattrib some values may come from inherited struct
        write('''            if hasattr(self, k):
                setattr(self, k, v)

''')
        for i, tpl in enumerate(VFFSL(SL,"sorted",True)): # generated from line 140, col 1
            index = tpl[1]
            itm = VFN(VFFSL(SL,"self",True),"get_attrib_for_prop",False)(VFFSL(SL,"index",True))
            itm_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"itm",True)['name'])
            write('''
    @property
    def ''')
            _v = VFFSL(SL,"itm_name",True) # '${itm_name}' on line 146, col 9
            if _v is not None: write(_filter(_v, rawExpr='${itm_name}')) # from line 146, col 9.
            write('''(self) -> ''')
            _v = VFFSL(SL,"itm",True)['type'] # "$itm['type']" on line 146, col 30
            if _v is not None: write(_filter(_v, rawExpr="$itm['type']")) # from line 146, col 30.
            write(''':
''')
            if VFFSL(SL,"include_desc",True) and VFFSL(SL,"itm",True)['lines']: # generated from line 147, col 1
                write('''        """
''')
                if isinstance(VFFSL(SL,"itm",True)['lines'], str): # generated from line 149, col 5
                    write('''        ''')
                    _v = VFFSL(SL,"itm.lines",True) # '$itm.lines' on line 150, col 9
                    if _v is not None: write(_filter(_v, rawExpr='$itm.lines')) # from line 150, col 9.
                    write('''
''')
                else: # generated from line 151, col 5
                    for line in VFFSL(SL,"itm",True)['lines']: # generated from line 152, col 9
                        write('''        ''')
                        _v = VFFSL(SL,"line",True) # '$line' on line 153, col 9
                        if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 153, col 9.
                        write('''
''')
                write('''        """
''')
            write('''        return self._''')
            _v = VFN(VFFSL(SL,"self",True),"camel_to_snake",False)(VFFSL(SL,"itm_name",True)) # '$self.camel_to_snake($itm_name)' on line 158, col 22
            if _v is not None: write(_filter(_v, rawExpr='$self.camel_to_snake($itm_name)')) # from line 158, col 22.
            write('''
    
    @''')
            _v = VFFSL(SL,"itm_name",True) # '${itm_name}' on line 160, col 6
            if _v is not None: write(_filter(_v, rawExpr='${itm_name}')) # from line 160, col 6.
            write('''.setter
    def ''')
            _v = VFFSL(SL,"itm_name",True) # '${itm_name}' on line 161, col 9
            if _v is not None: write(_filter(_v, rawExpr='${itm_name}')) # from line 161, col 9.
            write('''(self, value: ''')
            _v = VFFSL(SL,"itm",True)['type'] # "$itm['type']" on line 161, col 34
            if _v is not None: write(_filter(_v, rawExpr="$itm['type']")) # from line 161, col 34.
            write(''') -> None:
        self._''')
            _v = VFN(VFFSL(SL,"self",True),"camel_to_snake",False)(VFFSL(SL,"itm_name",True)) # '$self.camel_to_snake($itm_name)' on line 162, col 15
            if _v is not None: write(_filter(_v, rawExpr='$self.camel_to_snake($itm_name)')) # from line 162, col 15.
            write(''' = value
''')
        write("""

__all__ = ['""")
        _v = VFFSL(SL,"safe_name",True) # '$safe_name' on line 166, col 13
        if _v is not None: write(_filter(_v, rawExpr='$safe_name')) # from line 166, col 13.
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

    _mainCheetahMethod_for_struct_base = 'respond'

## END CLASS DEFINITION

if not hasattr(struct_base, '_initCheetahAttributes'):
    templateAPIClass = getattr(struct_base,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(struct_base)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=struct_base()).run()


