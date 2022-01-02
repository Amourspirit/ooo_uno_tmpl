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
from _base_service import BaseService

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post2'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 2)
__CHEETAH_genTime__ = 1641158806.9985175
__CHEETAH_genTimestamp__ = 'Sun Jan  2 16:26:46 2022'
__CHEETAH_src__ = '_service.tmpl'
__CHEETAH_srcLastModified__ = 'Sun Jan  2 16:26:32 2022'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class service(BaseService):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(service, self).__init__(*args, **KWs)
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
        _v = VFN(VFFSL(SL,"self",True),"load_data",False)() # '$self.load_data()' on line 17, col 1
        if _v is not None: write(_filter(_v, rawExpr='$self.load_data()')) # from line 17, col 1.
        #  main Template
        safe_name = VFN(VFFSL(SL,"self",True),"get_safe_word",False)(VFFSL(SL,"name",True))
        write('''# coding: utf-8
# Service Class
# this is a auto generated file generated by Cheetah
# Generated: ''')
        _v = VFN(VFFSL(SL,"self",True),"get_timestamp_utc",False)() # '$self.get_timestamp_utc()' on line 23, col 14
        if _v is not None: write(_filter(_v, rawExpr='$self.get_timestamp_utc()')) # from line 23, col 14.
        write('''
''')
        for imp in VFFSL(SL,"from_imports",True): # generated from line 24, col 1
            _v = VFN(VFFSL(SL,"self",True),"get_from_import",False)(VFFSL(SL,"name",True), VFFSL(SL,"imp",True)) # '$self.get_from_import($name, $imp)' on line 25, col 1
            if _v is not None: write(_filter(_v, rawExpr='$self.get_from_import($name, $imp)')) # from line 25, col 1.
            write('''
''')
        write('''
class ''')
        _v = VFFSL(SL,"safe_name",True) # '${safe_name}' on line 28, col 7
        if _v is not None: write(_filter(_v, rawExpr='${safe_name}')) # from line 28, col 7.
        write('''(''')
        _v = VFN(VFFSL(SL,"self",True),"get_class_inherits",False)(VFFSL(SL,"name",True), VFFSL(SL,"inherits",True)) # '$self.get_class_inherits($name, $inherits)' on line 28, col 20
        if _v is not None: write(_filter(_v, rawExpr='$self.get_class_inherits($name, $inherits)')) # from line 28, col 20.
        write(''')''')
        _v = VFN(VFFSL(SL,"self",True),"get_class_end",False)() # '$self.get_class_end()' on line 28, col 63
        if _v is not None: write(_filter(_v, rawExpr='$self.get_class_end()')) # from line 28, col 63.
        write('''
''')
        if VFFSL(SL,"include_desc",True): # generated from line 29, col 1
            write('''    """
''')
            for line in VFN(VFFSL(SL,"self",True),"line_gen",False)(VFFSL(SL,"desc",True)): # generated from line 31, col 5
                write('''    ''')
                _v = VFFSL(SL,"line",True) # '$line' on line 32, col 5
                if _v is not None: write(_filter(_v, rawExpr='$line')) # from line 32, col 5.
                write('''
''')
            if VFFSL(SL,"link",True): # generated from line 34, col 5
                write('''
    See Also:
        `API ''')
                _v = VFFSL(SL,"name",True) # '$name' on line 37, col 14
                if _v is not None: write(_filter(_v, rawExpr='$name')) # from line 37, col 14.
                write(''' <''')
                _v = VFFSL(SL,"link",True) # '$link' on line 37, col 21
                if _v is not None: write(_filter(_v, rawExpr='$link')) # from line 37, col 21.
                write('''>`_
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

    link = ""

    quote = set()

    typings = set()

    inherits = []

    include_desc = True

    requires_typing = False

    from_imports = []

    namespace = ""

    attribs = {}

    _mainCheetahMethod_for_service = 'respond'

## END CLASS DEFINITION

if not hasattr(service, '_initCheetahAttributes'):
    templateAPIClass = getattr(service,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(service)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=service()).run()


