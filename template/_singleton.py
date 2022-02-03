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
__CHEETAH_genTime__ = 1643911497.1892388
__CHEETAH_genTimestamp__ = 'Thu Feb  3 13:04:57 2022'
__CHEETAH_src__ = '_singleton.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Feb  3 13:04:52 2022'
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
        _v = VFN(VFFSL(SL,"self",True),"load_data",False)() # '$self.load_data()' on line 24, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.load_data()')) # from line 24, col 1.
        #  main Template
        safe_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"name",True))
        is_method = 'methods' in VFFSL(SL,"attribs",True)
        is_properties = 'properties' in VFFSL(SL,"attribs",True)
        abc_imports = VFN(VFFSL(SL,"self",True),"get_abstract_imports",False)([VFFSL(SL,"is_method",True)],[VFFSL(SL,"is_properties",True)])
        write('''# coding: utf-8
''')
        self._handleCheetahInclude("resources/inc_lic.txt", trans=trans, includeFrom="file", raw=True)
        write('''# Singleton Class
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
        if VFFSL(SL,"requires_typing",True): # generated from line 38, col 1
            write('''import typing
''')
        for imp in VFFSL(SL,"imports",True): # generated from line 41, col 1
            write('''import ''')
            _v = VFFSL(SL,"imp",True) # '$imp' on line 42, col 8
            if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 42, col 8.
            write('''
''')
        if len(VFFSL(SL,"abc_imports",True)) > 0: # generated from line 44, col 1
            write('''from abc import ''')
            _v = VFN(VFFSL(SL,"self",True),"lst_to_str",False)(VFFSL(SL,"abc_imports",True)) # '$self.lst_to_str($abc_imports)' on line 45, col 17
            if _v is not None: write(_filter(_v, rawExpr='$self.lst_to_str($abc_imports)')) # from line 45, col 17.
            write('''
''')
        for imp in VFFSL(SL,"from_imports",True): # generated from line 47, col 1
            _v = VFN(VFFSL(SL,"self",True),"get_from_import",False)(VFFSL(SL,"name",True), VFFSL(SL,"imp",True)) # '$self.get_from_import($name, $imp)' on line 48, col 1
            if _v is not None: write(_filter(_v, rawExpr='$self.get_from_import($name, $imp)')) # from line 48, col 1.
            write('''
''')
        if len(VFFSL(SL,"from_imports_typing",True)) > 0: # generated from line 50, col 1
            write('''if typing.TYPE_CHECKING:
''')
            for imp in VFFSL(SL,"from_imports_typing",True): # generated from line 52, col 1
                write('''    ''')
                _v = VFN(VFFSL(SL,"self",True),"get_from_import",False)(VFFSL(SL,"name",True), VFFSL(SL,"imp",True)) # '$self.get_from_import($name, $imp)' on line 53, col 5
                if _v is not None: write(_filter(_v, rawExpr='$self.get_from_import($name, $imp)')) # from line 53, col 5.
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
    Singleton Class

''')
            for line in VFN(VFFSL(SL,"self",True),"line_gen",False)(VFFSL(SL,"desc",True)): # generated from line 67, col 5
                write('''    ''')
                _v = VFFSL(SL,"line",True) # '$line' on line 68, col 5
                if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 68, col 5.
                write('''
''')
            if VFFSL(SL,"link",True): # generated from line 70, col 5
                write('''
    See Also:
        `API ''')
                _v = VFFSL(SL,"name",True) # '$name' on line 73, col 14
                if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 73, col 14.
                write(''' <''')
                _v = VFFSL(SL,"link",True) # '$link' on line 73, col 21
                if _v is not None: write(_filter(_v, rawExpr='$link')) # from line 73, col 21.
                write('''>`_
''')
            write('''    """

''')
        write('''    _instance = None

    def __new__(cls, *args, **kwargs):
        # single instance only allowed
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

''')
        if VFFSL(SL,"is_properties",True): # generated from line 86, col 1
            properties = VFFSL(SL,"attribs",True)['properties']
            for property in VFFSL(SL,"properties",True): # generated from line 88, col 1
                p_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"property",True)['name'])
                p_return = VFN(VFFSL(SL,"self",True),"get_q_type",False)(VFFSL(SL,"property",True)['returns'])
                p_desc = VFFSL(SL,"property",True)['desc']
                write('''    @abstractproperty
    def ''')
                _v = VFFSL(SL,"p_name",True) # '${p_name}' on line 93, col 9
                if _v is not None: write(_filter(_v, rawExpr='${p_name}')) # from line 93, col 9.
                write('''(self) -> ''')
                _v = VFFSL(SL,"p_return",True) # '$p_return' on line 93, col 28
                if _v is not None: write(_filter(_v, rawExpr='$p_return')) # from line 93, col 28.
                write(''':
        """
''')
                for line in VFN(VFFSL(SL,"self",True),"line_gen",False)(VFFSL(SL,"p_desc",True)): # generated from line 95, col 5
                    write('''        ''')
                    _v = VFFSL(SL,"line",True) # '$line' on line 96, col 9
                    if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 96, col 9.
                    write('''
''')
                if VFN(VFFSL(SL,"self",True),"get_prop_has_errors",False)(VFFSL(SL,"property",True)): # generated from line 98, col 5
                    write('''
        Raises:

''')
                    for long, short in VFN(VFFSL(SL,"self",True),"get_prop_get_raises",False)(VFFSL(SL,"property",True)): # generated from line 102, col 5
                        write('''            ''')
                        _v = VFFSL(SL,"long",True) # '$long' on line 103, col 13
                        if _v is not None: write(_filter(_v, rawExpr='$long')) # from line 103, col 13.
                        write(''': get raises ``''')
                        _v = VFFSL(SL,"short",True) # '$short' on line 103, col 33
                        if _v is not None: write(_filter(_v, rawExpr='$short')) # from line 103, col 33.
                        write('''``
''')
                    for long, short in VFN(VFFSL(SL,"self",True),"get_prop_set_raises",False)(VFFSL(SL,"property",True)): # generated from line 105, col 5
                        write('''            ''')
                        _v = VFFSL(SL,"long",True) # '$long' on line 106, col 13
                        if _v is not None: write(_filter(_v, rawExpr='$long')) # from line 106, col 13.
                        write(''': set raises ``''')
                        _v = VFFSL(SL,"short",True) # '$short' on line 106, col 33
                        if _v is not None: write(_filter(_v, rawExpr='$short')) # from line 106, col 33.
                        write('''``
''')
                write('''        """
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


