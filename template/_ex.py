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

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post2'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 2)
__CHEETAH_genTime__ = 1641596431.6264787
__CHEETAH_genTimestamp__ = 'Fri Jan  7 18:00:31 2022'
__CHEETAH_src__ = '_ex.tmpl'
__CHEETAH_srcLastModified__ = 'Fri Jan  7 18:00:15 2022'
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
        _v = VFN(VFFSL(SL,"self",True),"init_data",False)() # '$self.init_data()' on line 5, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.init_data()')) # from line 5, col 1.
        _v = VFN(VFFSL(SL,"self",True),"load_data",False)() # '$self.load_data()' on line 21, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.load_data()')) # from line 21, col 1.
        #  main Template
        safe_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"name",True))
        is_properties = 'properties' in VFFSL(SL,"attribs",True)
        write('''# coding: utf-8
# Exception Class
# this is a auto generated file generated by Cheetah
''')
        if VFFSL(SL,"libre_office_ver",True): # generated from line 28, col 1
            write('''# Libre Office Version: ''')
            _v = VFFSL(SL,"libre_office_ver",True) # '$libre_office_ver' on line 29, col 25
            if _v is not None: write(_filter(_v, rawExpr='$libre_office_ver')) # from line 29, col 25.
            write('''
''')
        if VFFSL(SL,"requires_typing",True): # generated from line 31, col 1
            write('''import typing
''')
        for imp in VFFSL(SL,"imports",True): # generated from line 34, col 1
            write('''import ''')
            _v = VFFSL(SL,"imp",True) # '$imp' on line 35, col 8
            if _v is not None: write(_filter(_v, rawExpr='$imp')) # from line 35, col 8.
            write('''
''')
        for imp in VFFSL(SL,"from_imports",True): # generated from line 37, col 1
            _v = VFN(VFFSL(SL,"self",True),"get_from_import",False)(VFFSL(SL,"name",True), VFFSL(SL,"imp",True)) # '$self.get_from_import($name, $imp)' on line 38, col 1
            if _v is not None: write(_filter(_v, rawExpr='$self.get_from_import($name, $imp)')) # from line 38, col 1.
            write('''
''')
        if len(VFFSL(SL,"from_imports_typing",True)) > 0: # generated from line 40, col 1
            write('''if typing.TYPE_CHECKING:
''')
            for imp in VFFSL(SL,"from_imports_typing",True): # generated from line 42, col 1
                write('''    ''')
                _v = VFN(VFFSL(SL,"self",True),"get_from_import",False)(VFFSL(SL,"name",True), VFFSL(SL,"imp",True)) # '$self.get_from_import($name, $imp)' on line 43, col 5
                if _v is not None: write(_filter(_v, rawExpr='$self.get_from_import($name, $imp)')) # from line 43, col 5.
                write('''
''')
        write('''

class ''')
        _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 48, col 7
        if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 48, col 7.
        write('''(''')
        _v = VFN(VFFSL(SL,"self",True),"get_class_inherits",False)(VFFSL(SL,"name",True), VFFSL(SL,"inherits",True)) # '$self.get_class_inherits($name, $inherits)' on line 48, col 20
        if _v is not None: write(_filter(_v, rawExpr='$self.get_class_inherits($name, $inherits)')) # from line 48, col 20.
        write(''')''')
        _v = VFN(VFFSL(SL,"self",True),"get_class_end",False)() # '$self.get_class_end()' on line 48, col 63
        if _v is not None: write(_filter(_v, rawExpr='$self.get_class_end()')) # from line 48, col 63.
        write('''
''')
        if VFFSL(SL,"include_desc",True): # generated from line 49, col 1
            write('''    """
''')
            for line in VFN(VFFSL(SL,"self",True),"line_gen",False)(VFFSL(SL,"desc",True)): # generated from line 51, col 5
                write('''    ''')
                _v = VFFSL(SL,"line",True) # '$line' on line 52, col 5
                if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 52, col 5.
                write('''
''')
            if VFFSL(SL,"link",True): # generated from line 54, col 5
                write('''
    See Also:
        `API ''')
                _v = VFFSL(SL,"name",True) # '$name' on line 57, col 14
                if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 57, col 14.
                write(''' <''')
                _v = VFFSL(SL,"link",True) # '$link' on line 57, col 21
                if _v is not None: write(_filter(_v, rawExpr='$link')) # from line 57, col 21.
                write('''>`_
''')
            write('''    """

''')
        if VFFSL(SL,"is_properties",True): # generated from line 62, col 1
            properties = VFFSL(SL,"attribs",True)['properties']
            for property in VFFSL(SL,"properties",True): # generated from line 64, col 1
                p_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"property",True)['name'])
                p_type = VFFSL(SL,"property",True)['returns']
                p_desc = VFFSL(SL,"property",True)['desc']
                write('''    ''')
                _v = VFFSL(SL,"p_name",True) # '${p_name}' on line 68, col 5
                if _v is not None: write(_filter(_v, rawExpr='${p_name}')) # from line 68, col 5.
                write(''': ''')
                _v = VFN(VFFSL(SL,"self",True),"get_q_type",False)(VFFSL(SL,"p_type",True)) # '$self.get_q_type($p_type)' on line 68, col 16
                if _v is not None: write(_filter(_v, rawExpr='$self.get_q_type($p_type)')) # from line 68, col 16.
                write(''' = ...
''')
                if VFFSL(SL,"include_desc",True): # generated from line 69, col 5
                    write('''    """
''')
                    for line in VFN(VFFSL(SL,"self",True),"line_gen",False)(VFFSL(SL,"p_desc",True)): # generated from line 71, col 5
                        write('''    ''')
                        _v = VFFSL(SL,"line",True) # '$line' on line 72, col 5
                        if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 72, col 5.
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

    namespace = ""

    libre_office_ver = False

    desc = []

    link = ""

    requires_typing = False

    include_desc = True

    quote = set()

    typings = set()

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


