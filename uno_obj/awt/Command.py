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
from _const_base import const_base as c_base

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.6.post2'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 2)
__CHEETAH_genTime__ = 1638331125.4161685
__CHEETAH_genTimestamp__ = 'Tue Nov 30 22:58:45 2021'
__CHEETAH_src__ = '/home/paul/Documents/Projects/Python/Cheeta3/ooo_uno_tmpl/uno_obj/awt/Command.tmpl'
__CHEETAH_srcLastModified__ = 'Tue Nov 30 21:23:18 2021'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class Command(c_base):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(Command, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def writeBody(self, **KWS):



        ## CHEETAH: main method generated for this template
        trans = KWS.get("trans")
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

    hex = False

    sort = True

    flags = False

    name = "Command"

    desc = """these values specify the different command types available."""

    imports = []

    from_imports = []

    link = "https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1Command.html"

    const_dict = {    "CONTEXTMENU": ["1", [        "specifies a requests for a context menu."    ]],    "STARTDRAG": ["2", [        "specifies the beginning of a drag operation."    ]],    "WHEEL": ["3", [        "specifies a mouse wheel operation."    ]],    "STARTAUTOSCROLL": ["4", [        "specifies the beginning of an auto scroll operation."    ]],    "AUTOSCROLL": ["5", [        "specifies an auto scroll operation."    ]],    "VOICE": ["6", [        "specifies a request for a voice operation."    ]],    "STARTEXTTEXTINPUT": ["7", [        "specifies the beginning of an extended text input operation."    ]],    "EXTTEXTINPUT": ["8", [        "specifies an extended text input operation."    ]],    "ENDEXTTEXTINPUT": ["9", [        "specifies the end of an extended text input operation."    ]],    "INPUTCONTEXTCHANGE": ["10", [        "specifies that the input context has been changed."    ]],    "CURSORPOS": ["11", [        "specifies the cursor position."    ]],    "PASTESELECTION": ["12", [        "specifies a paste selection command."    ]],    "MODKEYCHANGE": ["13", [        "specifies that the state of a key modifier has changed."    ]],    "HANGUL_HANJA_CONVERSION": ["14", [        "specifies a Hangul hanja conversion command."    ]],    "USER": ["4096", [        "specifies a user-defined command."    ]]}

    _mainCheetahMethod_for_Command = 'writeBody'

## END CLASS DEFINITION

if not hasattr(Command, '_initCheetahAttributes'):
    templateAPIClass = getattr(Command,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(Command)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=Command()).run()


