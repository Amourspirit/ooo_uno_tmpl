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
from _base_ex import BaseEx
import re

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post2'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 2)
__CHEETAH_genTime__ = 1644524937.1311197
__CHEETAH_genTimestamp__ = 'Thu Feb 10 15:28:57 2022'
__CHEETAH_src__ = '_ex.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Feb 10 15:28:54 2022'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class ex(BaseEx):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(ex, self).__init__(*args, **KWs)
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
        _v = VFN(VFFSL(SL,"self",True),"load_data",False)() # '$self.load_data()' on line 25, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.load_data()')) # from line 25, col 1.
        #  main Template
        re_underscore_hex = r"(_[0-9A-Fa-f]*)"
        safe_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"name",True))
        #  properties list of dict that combines properties and types with types first
        properties = VFN(VFFSL(SL,"self",True),"get_properties_all",False)()
        is_method = 'methods' in VFFSL(SL,"attribs",True)
        is_properties = len(VFFSL(SL,"properties",True)) > 0
        sorted = VFN(VFFSL(SL,"self",True),"get_sorted_names",False)()
        # set $is_types = 'types' in $attribs
        # set $abc_imports = $self.get_abstract_imports([$is_method],[$is_properties, $is_types])
        abc_imports = []
        write('''# coding: utf-8
''')
        self._handleCheetahInclude("resources/inc_lic.txt", trans=trans, includeFrom="file", raw=True)
        write('''# Exception Class
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
        write('''from ooo.oenv import UNO_NONE
''')
        if VFFSL(SL,"requires_typing",True) or len(VFFSL(SL,"sorted",True)) > 0: # generated from line 46, col 1
            write('''import typing
''')
        for imp in VFFSL(SL,"imports",True): # generated from line 49, col 1
            write('''import ''')
            _v = VFFSL(SL,"imp",True) # '$imp' on line 50, col 8
            if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 50, col 8.
            write('''
''')
        if len(VFFSL(SL,"abc_imports",True)) > 0: # generated from line 52, col 1
            write('''from abc import ''')
            _v = VFN(VFFSL(SL,"self",True),"lst_to_str",False)(VFFSL(SL,"abc_imports",True)) # '$self.lst_to_str($abc_imports)' on line 53, col 17
            if _v is not None: write(_filter(_v, rawExpr='$self.lst_to_str($abc_imports)')) # from line 53, col 17.
            write('''
''')
        for imp in VFFSL(SL,"from_imports",True): # generated from line 55, col 1
            _v = VFN(VFFSL(SL,"self",True),"get_from_import",False)(VFFSL(SL,"name",True), VFFSL(SL,"imp",True)) # '$self.get_from_import($name, $imp)' on line 56, col 1
            if _v is not None: write(_filter(_v, rawExpr='$self.get_from_import($name, $imp)')) # from line 56, col 1.
            write('''
''')
        if len(VFFSL(SL,"from_imports_typing",True)) > 0: # generated from line 58, col 1
            # if typing.TYPE_CHECKING:
            for imp in VFFSL(SL,"from_imports_typing",True): # generated from line 60, col 1
                _v = VFN(VFFSL(SL,"self",True),"get_from_import",False)(VFFSL(SL,"name",True), VFFSL(SL,"imp",True)) # '$self.get_from_import($name, $imp)' on line 61, col 1
                if _v is not None: write(_filter(_v, rawExpr='$self.get_from_import($name, $imp)')) # from line 61, col 1.
                write('''
''')
        write('''
''')
        if VFFSL(SL,"allow_db",True): # generated from line 65, col 1
            write('''class ''')
            _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 66, col 7
            if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 66, col 7.
            write('''(''')
            _v = VFN(VFFSL(SL,"self",True),"get_class_inherits_from_db",False)() # '$self.get_class_inherits_from_db()' on line 66, col 20
            if _v is not None: write(_filter(_v, rawExpr='$self.get_class_inherits_from_db()')) # from line 66, col 20.
            write(''')''')
            _v = VFN(VFFSL(SL,"self",True),"get_class_end",False)() # '$self.get_class_end()' on line 66, col 55
            if _v is not None: write(_filter(_v, rawExpr='$self.get_class_end()')) # from line 66, col 55.
            write('''
''')
        else: # generated from line 67, col 1
            write('''class ''')
            _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 68, col 7
            if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 68, col 7.
            write('''(''')
            _v = VFN(VFFSL(SL,"self",True),"get_class_inherits",False)(VFFSL(SL,"safe_name",True), VFFSL(SL,"inherits",True)) # '$self.get_class_inherits($safe_name, $inherits)' on line 68, col 20
            if _v is not None: write(_filter(_v, rawExpr='$self.get_class_inherits($safe_name, $inherits)')) # from line 68, col 20.
            write(''')''')
            _v = VFN(VFFSL(SL,"self",True),"get_class_end",False)() # '$self.get_class_end()' on line 68, col 68
            if _v is not None: write(_filter(_v, rawExpr='$self.get_class_end()')) # from line 68, col 68.
            write('''
''')
        if VFFSL(SL,"include_desc",True): # generated from line 70, col 1
            write('''    """
''')
            for line in VFN(VFFSL(SL,"self",True),"line_gen",False)(VFFSL(SL,"desc",True)): # generated from line 72, col 5
                write('''    ''')
                _v = VFFSL(SL,"line",True) # '$line' on line 73, col 5
                if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 73, col 5.
                write('''
''')
            if VFFSL(SL,"link",True): # generated from line 75, col 5
                write('''
    See Also:
        `API ''')
                _v = VFFSL(SL,"name",True) # '$name' on line 78, col 14
                if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 78, col 14.
                write(''' <''')
                _v = VFFSL(SL,"link",True) # '$link' on line 78, col 21
                if _v is not None: write(_filter(_v, rawExpr='$link')) # from line 78, col 21.
                write('''>`_
''')
            write('''    """

''')
        write("""    __ooo_ns__: str = '""")
        _v = VFFSL(SL,"namespace",True) # '$namespace' on line 83, col 24
        if _v is not None: write(_filter(_v, rawExpr='$namespace')) # from line 83, col 24.
        write("""'
    __ooo_full_ns__: str = '""")
        _v = VFFSL(SL,"fullname",True) # '$fullname' on line 84, col 29
        if _v is not None: write(_filter(_v, rawExpr='$fullname')) # from line 84, col 29.
        write("""'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = '""")
        _v = VFFSL(SL,"fullname",True) # '$fullname' on line 86, col 32
        if _v is not None: write(_filter(_v, rawExpr='$fullname')) # from line 86, col 32.
        write("""'
    __pyunostruct__: str = '""")
        _v = VFFSL(SL,"fullname",True) # '$fullname' on line 87, col 29
        if _v is not None: write(_filter(_v, rawExpr='$fullname')) # from line 87, col 29.
        write("""'

    typeName: str = '""")
        _v = VFFSL(SL,"fullname",True) # '$fullname' on line 89, col 22
        if _v is not None: write(_filter(_v, rawExpr='$fullname')) # from line 89, col 22.
        write('''\'
    """Literal Constant ``''')
        _v = VFFSL(SL,"fullname",True) # '$fullname' on line 90, col 27
        if _v is not None: write(_filter(_v, rawExpr='$fullname')) # from line 90, col 27.
        write('''``"""

    ''')
        _v = VFN(VFFSL(SL,"self",True),"get_constructor",False)() # '$self.get_constructor()' on line 92, col 5
        if _v is not None: write(_filter(_v, rawExpr='$self.get_constructor()')) # from line 92, col 5.
        write('''
        """
        Constructor

        Keyword Arguments:
''')
        for i, tpl in enumerate(VFFSL(SL,"sorted",True)): # generated from line 97, col 1
            index = tpl[1]
            itm = VFFSL(SL,"properties",True)[VFFSL(SL,"index",True)]
            itm_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"itm",True)['name'])
            itm_type = VFN(VFFSL(SL,"itm",True)['returns'],"removeprefix",False)('typing.')
            itm_type = re.sub(re_underscore_hex, '', VFFSL(SL,"itm_type",True), 1)
            write('''            ''')
            _v = VFFSL(SL,"itm_name",True) # '$itm_name' on line 103, col 13
            if _v is not None: write(_filter(_v, rawExpr='$itm_name')) # from line 103, col 13.
            write(''' (''')
            _v = VFFSL(SL,"itm_type",True) # '$itm_type' on line 103, col 24
            if _v is not None: write(_filter(_v, rawExpr='$itm_type')) # from line 103, col 24.
            write(''', optional): ''')
            _v = VFFSL(SL,"itm_name",True) # '$itm_name' on line 103, col 46
            if _v is not None: write(_filter(_v, rawExpr='$itm_name')) # from line 103, col 46.
            write(''' value.
''')
        write('''
            Other ``*args`` and ``**kwargs`` are passed to parent class.
        """

''')
        for i, tpl in enumerate(VFFSL(SL,"sorted",True)): # generated from line 109, col 1
            index = tpl[1]
            itm = VFFSL(SL,"properties",True)[VFFSL(SL,"index",True)]
            itm_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"itm.name",True))
            attrib_default = VFN(VFFSL(SL,"self",True),"get_attrib_default",False)(VFFSL(SL,"itm",True), True)
            if attrib_default == 'UNO_NONE': # generated from line 114, col 5
                write('''        if ''')
                _v = VFFSL(SL,"itm_name",True) # '$itm_name' on line 115, col 12
                if _v is not None: write(_filter(_v, rawExpr='$itm_name')) # from line 115, col 12.
                write(''' is UNO_NONE:
            self._''')
                _v = VFN(VFFSL(SL,"self",True),"camel_to_snake",False)(VFFSL(SL,"itm_name",True)) # '$self.camel_to_snake($itm_name)' on line 116, col 19
                if _v is not None: write(_filter(_v, rawExpr='$self.camel_to_snake($itm_name)')) # from line 116, col 19.
                write(''' = ''')
                _v = VFN(VFFSL(SL,"self",True),"get_attrib_default",False)(VFFSL(SL,"itm",True)) # '$self.get_attrib_default($itm)' on line 116, col 53
                if _v is not None: write(_filter(_v, rawExpr='$self.get_attrib_default($itm)')) # from line 116, col 53.
                write('''
        else:
            self._''')
                _v = VFN(VFFSL(SL,"self",True),"camel_to_snake",False)(VFFSL(SL,"itm_name",True)) # '$self.camel_to_snake($itm_name)' on line 118, col 19
                if _v is not None: write(_filter(_v, rawExpr='$self.camel_to_snake($itm_name)')) # from line 118, col 19.
                write(''' = ''')
                _v = VFFSL(SL,"itm_name",True) # '$itm_name' on line 118, col 53
                if _v is not None: write(_filter(_v, rawExpr='$itm_name')) # from line 118, col 53.
                write('''
''')
            else: # generated from line 119, col 5
                write('''        self._''')
                _v = VFN(VFFSL(SL,"self",True),"camel_to_snake",False)(VFFSL(SL,"itm_name",True)) # '$self.camel_to_snake($itm_name)' on line 120, col 15
                if _v is not None: write(_filter(_v, rawExpr='$self.camel_to_snake($itm_name)')) # from line 120, col 15.
                write(''' = ''')
                _v = VFFSL(SL,"itm_name",True) # '$itm_name' on line 120, col 49
                if _v is not None: write(_filter(_v, rawExpr='$itm_name')) # from line 120, col 49.
                write('''
''')
        write('''
''')
        if VFN(VFFSL(SL,"self",True),"has_uno_extends",False)(): # generated from line 124, col 1
            write('''
        super().__init__(*args, **kwargs)
''')
        else: # generated from line 127, col 1
            write('''
        super().__init__(*args)
''')
        write('''
''')
        if VFFSL(SL,"is_method",True): # generated from line 132, col 1
            methods = VFFSL(SL,"attribs",True)['methods']
            for method in VFFSL(SL,"methods",True): # generated from line 134, col 5
                m_desc = VFFSL(SL,"method",True)['desc']
                out_args = VFN(VFFSL(SL,"self",True),"get_out_args",False)(VFFSL(SL,"method",True))
                raises = VFN(VFFSL(SL,"self",True),"get_raises_list",False)(VFFSL(SL,"method",True))
                write('''    @abstractmethod
    ''')
                _v = VFN(VFFSL(SL,"self",True),"get_formated_meth",False)(VFFSL(SL,"method",True)) # '$self.get_formated_meth($method)' on line 139, col 5
                if _v is not None: write(_filter(_v, rawExpr='$self.get_formated_meth($method)')) # from line 139, col 5.
                write('''
        """
''')
                for line in VFN(VFFSL(SL,"self",True),"line_gen",False)(VFFSL(SL,"m_desc",True)): # generated from line 141, col 9
                    write('''        ''')
                    _v = VFFSL(SL,"line",True) # '$line' on line 142, col 9
                    if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 142, col 9.
                    write('''
''')
                if len(VFFSL(SL,"out_args",True)) > 0: # generated from line 144, col 5
                    write('''
''')
                    for arg in VFFSL(SL,"out_args",True): # generated from line 146, col 9
                        write('''        * ``''')
                        _v = VFFSL(SL,"arg",True) # '${arg}' on line 147, col 13
                        if _v is not None: write(_filter(_v, rawExpr='${arg}')) # from line 147, col 13.
                        write('''`` is an out direction argument.
''')
                if len(VFFSL(SL,"raises",True)) > 0: # generated from line 150, col 5
                    write('''
        Raises:
''')
                    for itm in VFFSL(SL,"raises",True): # generated from line 153, col 9
                        write('''            ''')
                        _v = VFFSL(SL,"itm",True)[0] # '$itm[0]' on line 154, col 13
                        if _v is not None: write(_filter(_v, rawExpr='$itm[0]')) # from line 154, col 13.
                        write(''': ``''')
                        _v = VFFSL(SL,"itm",True)[1] # '$itm[1]' on line 154, col 24
                        if _v is not None: write(_filter(_v, rawExpr='$itm[1]')) # from line 154, col 24.
                        write('''``
''')
                write('''        """
''')
        if VFFSL(SL,"is_properties",True): # generated from line 160, col 1
            for property in VFFSL(SL,"properties",True): # generated from line 161, col 1
                p_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"property",True)['name'])
                p_return = VFFSL(SL,"property",True)['returns']
                p_desc = VFFSL(SL,"property",True)['desc']
                write('''    @property
    def ''')
                _v = VFFSL(SL,"p_name",True) # '${p_name}' on line 166, col 9
                if _v is not None: write(_filter(_v, rawExpr='${p_name}')) # from line 166, col 9.
                write('''(self) -> ''')
                _v = VFFSL(SL,"property",True)['returns'] # "$property['returns']" on line 166, col 28
                if _v is not None: write(_filter(_v, rawExpr="$property['returns']")) # from line 166, col 28.
                write(''':
        """
''')
                for line in VFN(VFFSL(SL,"self",True),"line_gen",False)(VFFSL(SL,"p_desc",True)): # generated from line 168, col 5
                    write('''        ''')
                    _v = VFFSL(SL,"line",True) # '$line' on line 169, col 9
                    if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 169, col 9.
                    write('''
''')
                if VFN(VFFSL(SL,"self",True),"get_prop_has_errors",False)(VFFSL(SL,"property",True)): # generated from line 171, col 5
                    write('''
        Raises:

''')
                    for long, short in VFN(VFFSL(SL,"self",True),"get_prop_get_raises",False)(VFFSL(SL,"property",True)): # generated from line 175, col 5
                        write('''            ''')
                        _v = VFFSL(SL,"long",True) # '$long' on line 176, col 13
                        if _v is not None: write(_filter(_v, rawExpr='$long')) # from line 176, col 13.
                        write(''': get raises ``''')
                        _v = VFFSL(SL,"short",True) # '$short' on line 176, col 33
                        if _v is not None: write(_filter(_v, rawExpr='$short')) # from line 176, col 33.
                        write('''``
''')
                    for long, short in VFN(VFFSL(SL,"self",True),"get_prop_set_raises",False)(VFFSL(SL,"property",True)): # generated from line 178, col 5
                        write('''            ''')
                        _v = VFFSL(SL,"long",True) # '$long' on line 179, col 13
                        if _v is not None: write(_filter(_v, rawExpr='$long')) # from line 179, col 13.
                        write(''': set raises ``''')
                        _v = VFFSL(SL,"short",True) # '$short' on line 179, col 33
                        if _v is not None: write(_filter(_v, rawExpr='$short')) # from line 179, col 33.
                        write('''``
''')
                write('''        """
        return self._''')
                _v = VFN(VFFSL(SL,"self",True),"camel_to_snake",False)(VFFSL(SL,"p_name",True)) # '$self.camel_to_snake($p_name)' on line 183, col 22
                if _v is not None: write(_filter(_v, rawExpr='$self.camel_to_snake($p_name)')) # from line 183, col 22.
                write('''
    
    @''')
                _v = VFFSL(SL,"p_name",True) # '${p_name}' on line 185, col 6
                if _v is not None: write(_filter(_v, rawExpr='${p_name}')) # from line 185, col 6.
                write('''.setter
    def ''')
                _v = VFFSL(SL,"p_name",True) # '${p_name}' on line 186, col 9
                if _v is not None: write(_filter(_v, rawExpr='${p_name}')) # from line 186, col 9.
                write('''(self, value: ''')
                _v = VFFSL(SL,"property",True)['returns'] # "$property['returns']" on line 186, col 32
                if _v is not None: write(_filter(_v, rawExpr="$property['returns']")) # from line 186, col 32.
                write(''') -> None:
        self._''')
                _v = VFN(VFFSL(SL,"self",True),"camel_to_snake",False)(VFFSL(SL,"p_name",True)) # '$self.camel_to_snake($p_name)' on line 187, col 15
                if _v is not None: write(_filter(_v, rawExpr='$self.camel_to_snake($p_name)')) # from line 187, col 15.
                write(''' = value

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

    namespace = ""

    fullname = ""

    sort = False

    allow_db = True

    libre_office_ver = False

    include_desc = True

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

    _mainCheetahMethod_for_ex = 'respond'

## END CLASS DEFINITION

if not hasattr(ex, '_initCheetahAttributes'):
    templateAPIClass = getattr(ex,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(ex)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=ex()).run()


