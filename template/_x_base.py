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
from _base_interface import BaseInterface

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post1'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 1)
__CHEETAH_genTime__ = 1684874606.1326563
__CHEETAH_genTimestamp__ = 'Tue May 23 16:43:26 2023'
__CHEETAH_src__ = '_x_base.tmpl'
__CHEETAH_srcLastModified__ = 'Tue May 23 16:43:06 2023'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class x_base(BaseInterface):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(x_base, self).__init__(*args, **KWs)
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
        _v = VFN(VFFSL(SL,"self",True),"load_data",False)() # '$self.load_data()' on line 23, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.load_data()')) # from line 23, col 1.
        self.using_future_annotations = True
        #  main Template
        safe_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"name",True))
        fullname = VFFSL(SL,"namespace",True) + '.' + VFFSL(SL,"safe_name",True)
        is_method = 'methods' in VFFSL(SL,"attribs",True)
        is_properties = 'properties' in VFFSL(SL,"attribs",True)
        is_types = 'types' in VFFSL(SL,"attribs",True)
        abc_imports = VFN(VFFSL(SL,"self",True),"get_abstract_imports",False)([VFFSL(SL,"is_method",True)],[VFFSL(SL,"is_properties",True), VFFSL(SL,"is_types",True)])
        write('''# coding: utf-8
''')
        self._handleCheetahInclude("resources/inc_lic.txt", trans=trans, includeFrom="file", raw=True)
        write('''# Interface Class
# this is a auto generated file generated by Cheetah
''')
        if VFFSL(SL,"libre_office_ver",True): # generated from line 36, col 1
            write('''# Libre Office Version: ''')
            _v = VFFSL(SL,"libre_office_ver",True) # '$libre_office_ver' on line 37, col 25
            if _v is not None: write(_filter(_v, rawExpr='$libre_office_ver')) # from line 37, col 25.
            write('''
''')
        write('''# Namespace: ''')
        _v = VFFSL(SL,"namespace",True) # '$namespace' on line 39, col 14
        if _v is not None: write(_filter(_v, rawExpr='$namespace')) # from line 39, col 14.
        write('''
from __future__ import annotations
''')
        if len(VFFSL(SL,"inherits",True)) == 0: # generated from line 41, col 1
            inherits = ['ABC']
            abc_imports = VFFSL(SL,"abc_imports",True) + ['ABC']
        if VFFSL(SL,"requires_typing",True): # generated from line 45, col 1
            write('''import typing
''')
        for imp in VFFSL(SL,"imports",True): # generated from line 48, col 1
            write('''import ''')
            _v = VFFSL(SL,"imp",True) # '$imp' on line 49, col 8
            if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 49, col 8.
            write('''
''')
        if len(VFFSL(SL,"abc_imports",True)) > 0: # generated from line 51, col 1
            write('''from abc import ''')
            _v = VFN(VFFSL(SL,"self",True),"lst_to_str",False)(VFFSL(SL,"abc_imports",True)) # '$self.lst_to_str($abc_imports)' on line 52, col 17
            if _v is not None: write(_filter(_v, rawExpr='$self.lst_to_str($abc_imports)')) # from line 52, col 17.
            write('''
''')
        for imp in VFFSL(SL,"from_imports",True): # generated from line 54, col 1
            _v = VFN(VFFSL(SL,"self",True),"get_from_import",False)(VFFSL(SL,"name",True), VFFSL(SL,"imp",True)) # '$self.get_from_import($name, $imp)' on line 55, col 1
            if _v is not None: write(_filter(_v, rawExpr='$self.get_from_import($name, $imp)')) # from line 55, col 1.
            write('''
''')
        if len(VFFSL(SL,"from_imports_typing",True)) > 0: # generated from line 57, col 1
            write('''if typing.TYPE_CHECKING:
''')
            for imp in VFFSL(SL,"from_imports_typing",True): # generated from line 59, col 1
                write('''    ''')
                _v = VFN(VFFSL(SL,"self",True),"get_from_import",False)(VFFSL(SL,"name",True), VFFSL(SL,"imp",True)) # '$self.get_from_import($name, $imp)' on line 60, col 5
                if _v is not None: write(_filter(_v, rawExpr='$self.get_from_import($name, $imp)')) # from line 60, col 5.
                write('''
''')
        write('''
''')
        if VFFSL(SL,"allow_db",True): # generated from line 64, col 1
            write('''class ''')
            _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 65, col 7
            if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 65, col 7.
            write('''(''')
            _v = VFN(VFFSL(SL,"self",True),"get_class_inherits_from_db",False)('ABC') # "$self.get_class_inherits_from_db('ABC')" on line 65, col 20
            if _v is not None: write(_filter(_v, rawExpr="$self.get_class_inherits_from_db('ABC')")) # from line 65, col 20.
            write('''):
''')
        else: # generated from line 66, col 1
            write('''class ''')
            _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 67, col 7
            if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 67, col 7.
            write('''(''')
            _v = VFN(VFFSL(SL,"self",True),"get_class_inherits",False)(VFFSL(SL,"name",True), VFFSL(SL,"inherits",True)) # '$self.get_class_inherits($name, $inherits)' on line 67, col 20
            if _v is not None: write(_filter(_v, rawExpr='$self.get_class_inherits($name, $inherits)')) # from line 67, col 20.
            write('''):
''')
        write('''    """
''')
        for line in VFN(VFFSL(SL,"self",True),"line_gen",False)(VFFSL(SL,"desc",True)): # generated from line 70, col 5
            write('''    ''')
            _v = VFFSL(SL,"line",True) # '$line' on line 71, col 5
            if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 71, col 5.
            write('''
''')
        if VFFSL(SL,"link",True): # generated from line 73, col 1
            write('''
    See Also:
        `API ''')
            _v = VFFSL(SL,"name",True) # '$name' on line 76, col 14
            if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 76, col 14.
            write(''' <''')
            _v = VFFSL(SL,"link",True) # '$link' on line 76, col 21
            if _v is not None: write(_filter(_v, rawExpr='$link')) # from line 76, col 21.
            write('''>`_
''')
        write('''    """
    __ooo_ns__: str = \'''')
        _v = VFFSL(SL,"namespace",True) # '$namespace' on line 79, col 24
        if _v is not None: write(_filter(_v, rawExpr='$namespace')) # from line 79, col 24.
        write("""'
    __ooo_full_ns__: str = '""")
        _v = VFFSL(SL,"fullname",True) # '$fullname' on line 80, col 29
        if _v is not None: write(_filter(_v, rawExpr='$fullname')) # from line 80, col 29.
        write("""'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = '""")
        _v = VFFSL(SL,"fullname",True) # '$fullname' on line 82, col 32
        if _v is not None: write(_filter(_v, rawExpr='$fullname')) # from line 82, col 32.
        write("""'

""")
        if VFFSL(SL,"is_method",True): # generated from line 84, col 1
            methods = VFFSL(SL,"attribs",True)['methods']
            for method in VFFSL(SL,"methods",True): # generated from line 86, col 5
                m_desc = VFFSL(SL,"method",True)['desc']
                out_args = VFN(VFFSL(SL,"self",True),"get_out_args",False)(VFFSL(SL,"method",True))
                raises = VFN(VFFSL(SL,"self",True),"get_raises_list",False)(VFFSL(SL,"method",True))
                write('''    @abstractmethod
    ''')
                _v = VFN(VFFSL(SL,"self",True),"get_formated_meth",False)(VFFSL(SL,"method",True)) # '$self.get_formated_meth($method)' on line 91, col 5
                if _v is not None: write(_filter(_v, rawExpr='$self.get_formated_meth($method)')) # from line 91, col 5.
                write('''
        """
''')
                for line in VFN(VFFSL(SL,"self",True),"line_gen",False)(VFFSL(SL,"m_desc",True)): # generated from line 93, col 9
                    write('''        ''')
                    _v = VFFSL(SL,"line",True) # '$line' on line 94, col 9
                    if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 94, col 9.
                    write('''
''')
                if len(VFFSL(SL,"out_args",True)) > 0: # generated from line 96, col 5
                    write('''
''')
                    for arg in VFFSL(SL,"out_args",True): # generated from line 98, col 9
                        write('''        * ``''')
                        _v = VFFSL(SL,"arg",True) # '${arg}' on line 99, col 13
                        if _v is not None: write(_filter(_v, rawExpr='${arg}')) # from line 99, col 13.
                        write('''`` is an out direction argument.
''')
                if len(VFFSL(SL,"raises",True)) > 0: # generated from line 102, col 5
                    write('''
        Raises:
''')
                    for itm in VFFSL(SL,"raises",True): # generated from line 105, col 9
                        write('''            ''')
                        _v = VFFSL(SL,"itm",True)[0] # '$itm[0]' on line 106, col 13
                        if _v is not None: write(_filter(_v, rawExpr='$itm[0]')) # from line 106, col 13.
                        write(''': ``''')
                        _v = VFFSL(SL,"itm",True)[1] # '$itm[1]' on line 106, col 24
                        if _v is not None: write(_filter(_v, rawExpr='$itm[1]')) # from line 106, col 24.
                        write('''``
''')
                write('''        """
        ...
''')
        if VFFSL(SL,"is_types",True): # generated from line 113, col 1
            properties = VFFSL(SL,"attribs",True)['types']
            for property in VFFSL(SL,"properties",True): # generated from line 115, col 1
                p_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"property",True)['name'])
                p_return = VFN(VFFSL(SL,"self",True),"get_property_return",False)(VFFSL(SL,"property",True))
                p_desc = VFFSL(SL,"property",True)['desc']
                write('''    @abstractproperty
    def ''')
                _v = VFFSL(SL,"p_name",True) # '${p_name}' on line 120, col 9
                if _v is not None: write(_filter(_v, rawExpr='${p_name}')) # from line 120, col 9.
                write('''(self) -> ''')
                _v = VFFSL(SL,"p_return",True) # '$p_return' on line 120, col 28
                if _v is not None: write(_filter(_v, rawExpr='$p_return')) # from line 120, col 28.
                write(''':
        """
''')
                for line in VFN(VFFSL(SL,"self",True),"line_gen",False)(VFFSL(SL,"p_desc",True)): # generated from line 122, col 5
                    write('''        ''')
                    _v = VFFSL(SL,"line",True) # '$line' on line 123, col 9
                    if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 123, col 9.
                    write('''
''')
                if VFN(VFFSL(SL,"self",True),"get_prop_has_errors",False)(VFFSL(SL,"property",True)): # generated from line 125, col 5
                    write('''
        Raises:

''')
                    for long, short in VFN(VFFSL(SL,"self",True),"get_prop_get_raises",False)(VFFSL(SL,"property",True)): # generated from line 129, col 5
                        write('''            ''')
                        _v = VFFSL(SL,"long",True) # '$long' on line 130, col 13
                        if _v is not None: write(_filter(_v, rawExpr='$long')) # from line 130, col 13.
                        write(''': get raises ``''')
                        _v = VFFSL(SL,"short",True) # '$short' on line 130, col 33
                        if _v is not None: write(_filter(_v, rawExpr='$short')) # from line 130, col 33.
                        write('''``
''')
                    for long, short in VFN(VFFSL(SL,"self",True),"get_prop_set_raises",False)(VFFSL(SL,"property",True)): # generated from line 132, col 5
                        write('''            ''')
                        _v = VFFSL(SL,"long",True) # '$long' on line 133, col 13
                        if _v is not None: write(_filter(_v, rawExpr='$long')) # from line 133, col 13.
                        write(''': set raises ``''')
                        _v = VFFSL(SL,"short",True) # '$short' on line 133, col 33
                        if _v is not None: write(_filter(_v, rawExpr='$short')) # from line 133, col 33.
                        write('''``
''')
                write('''        """
        ...

''')
        if VFFSL(SL,"is_properties",True): # generated from line 141, col 1
            properties = VFFSL(SL,"attribs",True)['properties']
            for property in VFFSL(SL,"properties",True): # generated from line 143, col 1
                p_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"property",True)['name'])
                p_return = VFN(VFFSL(SL,"self",True),"get_property_return",False)(VFFSL(SL,"property",True))
                p_desc = VFFSL(SL,"property",True)['desc']
                write('''    @abstractproperty
    def ''')
                _v = VFFSL(SL,"p_name",True) # '${p_name}' on line 148, col 9
                if _v is not None: write(_filter(_v, rawExpr='${p_name}')) # from line 148, col 9.
                write('''(self) -> ''')
                _v = VFFSL(SL,"p_return",True) # '$p_return' on line 148, col 28
                if _v is not None: write(_filter(_v, rawExpr='$p_return')) # from line 148, col 28.
                write(''':
        """
''')
                for line in VFN(VFFSL(SL,"self",True),"line_gen",False)(VFFSL(SL,"p_desc",True)): # generated from line 150, col 5
                    write('''        ''')
                    _v = VFFSL(SL,"line",True) # '$line' on line 151, col 9
                    if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 151, col 9.
                    write('''
''')
                if VFN(VFFSL(SL,"self",True),"get_prop_has_errors",False)(VFFSL(SL,"property",True)): # generated from line 153, col 5
                    write('''
        Raises:

''')
                    for long, short in VFN(VFFSL(SL,"self",True),"get_prop_get_raises",False)(VFFSL(SL,"property",True)): # generated from line 157, col 5
                        write('''            ''')
                        _v = VFFSL(SL,"long",True) # '$long' on line 158, col 13
                        if _v is not None: write(_filter(_v, rawExpr='$long')) # from line 158, col 13.
                        write(''': get raises ``''')
                        _v = VFFSL(SL,"short",True) # '$short' on line 158, col 33
                        if _v is not None: write(_filter(_v, rawExpr='$short')) # from line 158, col 33.
                        write('''``
''')
                    for long, short in VFN(VFFSL(SL,"self",True),"get_prop_set_raises",False)(VFFSL(SL,"property",True)): # generated from line 160, col 5
                        write('''            ''')
                        _v = VFFSL(SL,"long",True) # '$long' on line 161, col 13
                        if _v is not None: write(_filter(_v, rawExpr='$long')) # from line 161, col 13.
                        write(''': set raises ``''')
                        _v = VFFSL(SL,"short",True) # '$short' on line 161, col 33
                        if _v is not None: write(_filter(_v, rawExpr='$short')) # from line 161, col 33.
                        write('''``
''')
                write('''        """
        ...

''')
        write("""
__all__ = ['""")
        _v = VFFSL(SL,"name",True) # '$name' on line 170, col 13
        if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 170, col 13.
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

    _mainCheetahMethod_for_x_base = 'respond'

## END CLASS DEFINITION

if not hasattr(x_base, '_initCheetahAttributes'):
    templateAPIClass = getattr(x_base,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(x_base)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=x_base()).run()


