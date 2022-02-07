# coding: utf-8
from typing import List, Optional, Tuple, Union
import uno
StarDesktop=None
# The ServiceManager of the running OOo.
# It is cached in a global variable.
# go_service_manager: Optional[XMultiComponentFactory] = None
go_service_manager = None

# The CoreReflection object.
# It is cached in a global variable.
go_core_reflection = False

def get_service_manager() -> object:
    """
    Get the ServiceManager from the running OpenOffice.org. 
    Then retain it in the global variable go_service_manager for future use. 
    This is similar to the GetProcessServiceManager() in OOo Basic. 
    
    Returns:
        XMultiComponentFactory: Service Manager
    """
    global go_service_manager
    if not go_service_manager:
        # Get the uno component context from the PyUNO runtime
        ctx = uno.getComponentContext()
        go_service_manager = ctx.getServiceManager()
    return go_service_manager


#------------------------------------------------------------
#   Uno convenience functions
#   The stuff in this section is just to make
#    python progrmaming of OOo more like using OOo Basic.
#------------------------------------------------------------


def create_uno_service(clazz: Union[str, object], ctx: object = None, args: Optional[Tuple[object]] = None) -> object:
    """A handy way to create a global objects within the running OOo. 
    Similar to the function of the same name in OOo Basic. 
    
    Args:
        clazz (str, object): name of the service to be instanciated or object that contains __ooo_full_ns__ attribute.
        ctx (XComponentContext, optional): the context if required.
        args (Typle[object], optional): the arguments when needed.
    
    Returns:
        object: component instance

    Notes:
        A service signals that it expects parameters during instantiation by supporting the com.sun.star.lang.XInitialization interface.
        There maybe services which can only be instantiated with parameters
    """
    is_class = False
    if isinstance(clazz, str):
        _cls = clazz
    elif hasattr(clazz, '__ooo_full_ns__'):
        # _cls = 'com.sun.star.io.SequenceInputStream'
        _cls = clazz.__ooo_full_ns__
        is_class = True
    else:
        raise TypeError('create_uno_service() cClass incorrect type')
    return _create_uno_service(clazz=_cls, ctx=ctx, args=args)

# This is the same as ServiceManager.createInstance( ... )


def _create_uno_service(clazz: str, ctx: obj = None, args: tuple = None) -> object:
    """Creates a global objects within the running OOo. 
    Similar to the function of the same name in OOo Basic. 
    
    Args:
        clazz (str): name of the service to be instanciated.
        ctx (XComponentContext, optional): the context if required.
        args (List[object], optional): the arguments when needed.
    
    Returns:
        object: component instance

    Notes:
        A service signals that it expects parameters during instantiation by supporting the com.sun.star.lang.XInitialization interface.
        There maybe services which can only be instantiated with parameters
    """
    # https://wiki.openoffice.org/wiki/Documentation/DevGuide/ProUNO/Service_Manager
    # In case the service manager does not provide an implementation for a request,
    # a null reference is returned, so it is mandatory to check.
    # Every UNO exception may be thrown during instantiation.
    smgr = get_service_manager()
    if ctx and args:
        oObj = smgr.createInstanceWithArgumentsAndContext(clazz, args, ctx)
    elif args:
        oObj = smgr.createInstanceWithArguments(clazz, args)
    elif ctx:
        oObj = smgr.createInstanceWithContext(clazz, ctx)
    else:
        oObj = smgr.createInstance(clazz)
    return oObj

def get_desktop() -> object:
    """An easy way to obtain the Desktop object from a running OOo.
    
    Returns:
        object: com.sun.star.frame.Desktop
    
    See Also:
        `LibreOffice 7.2 SDK API Desktop Reference <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1Desktop.html>`_
    
    Warning:
        Method uses "com.sun.star.frame.Desktop" and the
        `Desktop API <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1Desktop.html>`_
        states that it is deprecated.
        The api suggest; Rather use the 'theDesktop' singleton.
    
    Todo:
        Test if this method would work with 'theDesktop'
    """
    global StarDesktop
    if StarDesktop == None:
        StarDesktop = create_uno_service("com.sun.star.frame.Desktop")
    return StarDesktop


# preload the StarDesktop variable.
# get_desktop()


def get_core_reflection() -> object:
    '''
    This service is the implementation of the reflection API.
    
    Returns:
        object: com.sun.star.reflection.CoreReflection
    
    See Also:
        `LibreOffice 7.2 SDK CoreReflection API Reference <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1reflection_1_1CoreReflection.html>`_
    
    Warning:
        Method uses "com.sun.star.reflection.CoreReflection" and the
        `CoreReflection API <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1reflection_1_1CoreReflection.html>`_
        states that it is deprecated.
        The api suggest; Rather use the 'theCoreReflection' singleton.
    
    Todo:
        Test if this method would work with 'theCoreReflection'
    '''
    # https://stackoverflow.com/questions/67527942/why-cant-an-annotated-variable-be-global
    global go_core_reflection
    if not go_core_reflection:
        go_core_reflection = create_uno_service(
            "com.sun.star.reflection.CoreReflection")
    return go_core_reflection


def create_uno_struct(cTypeName: str):
    """Create a UNO struct and return it. 
    Similar to the function of the same name in OOo Basic. 
    
    Returns:
        object: uno struct
    """
    oCoreReflection = get_core_reflection()
    # Get the IDL class for the type name
    oXIdlClass = oCoreReflection.forName(cTypeName)
    # Create the struct.
    oReturnValue, oStruct = oXIdlClass.createObject(None)
    return oStruct



#------------------------------------------------------------
#   High level general purpose functions
#------------------------------------------------------------


def make_property_value(cName: Optional[str] = None, uValue: object = None, nHandle: Optional[int] = None, nState: Optional[object] = None) -> object:
    """
    Create a com.sun.star.beans.PropertyValue.
    
    Args:
        cName (:obj:`str`, optional): Specifies the name of the property.
        uValue (:obj:`any`, optional): Contains the value of the property or ``None``, if no value is available.
        nHandle (:obj:`int`, optional): Contains an implementation-specific handle for the property.
        nState (:obj:`com::sun::star::beans::PropertyState`, optional): Determines if the value comes from the object itself or from a default and if the value cannot be determined exactly.
    
    Returns:
        object: ``com.sun.star.beans.PropertyValue`` struct.
    
    See Also:
        `LibreOffice API - PropertyValue Struct Reference <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1PropertyValue.html>`_
    """
    oPropertyValue = create_uno_struct(
        "com.sun.star.beans.PropertyValue")

    if cName != None:
        oPropertyValue.Name = cName
    if uValue != None:
        oPropertyValue.Value = uValue
    if nHandle != None:
        oPropertyValue.Handle = nHandle
    if nState != None:
        oPropertyValue.State = nState

    return oPropertyValue






