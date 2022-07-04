# coding: utf-8
from typing import Union
from kwhelp.decorator import AcceptedTypes, DecFuncEnum
from .api_proto_block import ApiProtoBlock
from .api_namespace import ApiNamespace
from .api_public_members import ApiPublicMembers
from .api_desc import ApiDesc
from .api_name import ApiName
from .api_properties_block import ApiPropertiesBlock
from .api_functions_block import ApiFunctionsBlock
from .api_interface_block import ApiInterfacesBlock
from .api_types_block import ApiTypesBlock
from .api_summary_rows import ApiSummaryRows
from .api_summaries import ApiSummaries
from .api_inherited import ApiInherited
from .api_detail_block import ApiDetailBlock
from .api_desc_detail import ApiDescDetail
from .api_method_prams_info import ApiMethodPramsInfo
from .api_method_exception import ApiMethodException
from .api_desc_block import ApiDescBlock
from ..web.soup_obj import SoupObj
from ..web.url_obj import UrlObj
from ..rules.area.i_rules_area import IRulesArea
from ..rules.area.rule_area_multi import RuleAreaMulti
from ..rules.area.rule_area_vertical import RuleAreaVertical
from ..rules.area.rule_area_single import RuleAreaSingle
from ..rules.area.rules_area import RulesArea
from ..rules.name.i_rules_name import IRulesName
from ..dataclass.import_info import ImportInfo


class APIData:
    """Class the brings together parts for scraping API Html pages"""
    # region Constructor

    def __init__(self, url_soup: Union[str, SoupObj], allow_cache: bool, long_names: bool = False, remove_parent_inherited: bool = True):
        """
        Constructor

        Args:
            url_soup (Union[str, SoupObj]): Soup Object
            allow_cache (bool): Determines if cache is used
            long_names (bool, optional): Determsin if name are short or long in various components.
                Short name may look like ``XInterface`` whereas a long name might look like
                ``uno.XInterface``. Defaults to ``False``.
        """
        if isinstance(url_soup, str):
            self.__url = url_soup
            self.__soup_obj = SoupObj(
                url=url_soup, allow_cache=allow_cache)
        else:
            self.__url = url_soup.url
            self.__soup_obj = url_soup
            self.__soup_obj.allow_cache = allow_cache
        self.__allow_cache = allow_cache
        self.__ns: ApiNamespace = None
        self.__long_names = long_names
        self.__api_data_public_members: ApiPublicMembers = None
        self.__api_data_name: ApiName = None
        self.__desc: ApiDesc = None
        self.__properties_block: ApiPropertiesBlock = None
        self.__func_block: ApiFunctionsBlock = None
        self.__interfaces_block: ApiInterfacesBlock = None
        self.__types_block: ApiTypesBlock = None
        self.__func_summary_rows: ApiSummaryRows = None
        self.__property_summary_rows: ApiSummaryRows = None
        self.__export_summary_rows: ApiSummaryRows = None
        self.__func_summaries: ApiSummaries = None
        self.__property_summaries: ApiSummaries = None
        self.__exported_summaries: ApiSummaries = None
        self.__type_summaries: ApiSummaries = None
        self.__type_summary_rows: ApiSummaryRows = None
        self.__inherited: ApiInherited = None
        self.__area_filter_rules_engine: IRulesArea = None
        self.__remove_parent_inherited = remove_parent_inherited

    # endregion Constructor

    # region Methods
    def _get_name_rules_engine(self) -> Union[IRulesName, None]:
        """
        Gets name rules engine instance or None.
        Can be overrides in subclasses.

        Returns:
            [type]: None
        """
        return None

    def _set_area_filter_rules_engine_rules(self, rules_engine: IRulesArea) -> None:
        """
        Registers rules for Area Filter Rules Engine.
        Can be overriden in subclasses.

        Args:
            rules_engine (IRulesArea): Area Rules Engine
        """
        # order of rules matter here.
        # RuleAreaSingle would also match if it were RuleAreaVertical
        rules_engine.register_rule(rule=RuleAreaMulti)
        rules_engine.register_rule(rule=RuleAreaVertical)
        rules_engine.register_rule(rule=RuleAreaSingle)

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_import_info_method(self, a_id: str) -> ImportInfo:
        """
        Gets imports for method params and return type

        Args:
            si_id (str): Function summary Info

        Returns:
            base.ImportInfo: Import info
        """
        key = 'get_import_info_method_' + a_id
        info = ImportInfo()
        params_info = self.get_prams_info(a_id=a_id)
        fn_info = self.func_summaries
        # ensure data is primed
        fn_info.get_obj()
        params_info.get_obj()

        info.requires_typing = params_info.requires_typing or fn_info.requires_typing
        info.from_imports.update(params_info.from_imports)
        info.from_imports.update(fn_info.from_imports)
        info.imports.update(fn_info.imports)
        return info

    def get_import_info_property(self) -> ImportInfo:
        """
        Gets imports for properties

        Args:
            si_id (str): Property summary Info

        Returns:
            base.ImportInfo: Import info
        """
        info = ImportInfo()
        p_info = self.property_summaries
        # ensure data is primed
        p_info.get_obj()
        info.requires_typing = p_info.requires_typing
        info.from_imports.update(p_info.from_imports)
        info.imports.update(p_info.imports)
        return info

    def get_import_info_type(self) -> ImportInfo:
        """
        Gets imports for typedefs

        Args:
            si_id (str): Types summary Info

        Returns:
            base.ImportInfo: Import info
        """
        info = ImportInfo()
        p_info = self.types_summaries
        # ensure data is primed
        p_info.get_obj()
        info.requires_typing = p_info.requires_typing
        info.from_imports.update(p_info.from_imports)
        info.imports.update(p_info.imports)
        return info

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_detail_block(self, a_id: str) -> ApiDetailBlock:
        """
        Gets detail block of a function.
        Gets the 

        Args:
            a_id (str): id of block such as ``aa1d747451151fbd244196e6305348dbc``

        Returns:
            ApiDetailBlock: object
        """
        return ApiDetailBlock(soup=self.soup_obj, a_id=a_id)

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_desc_detail(self, a_id: str) -> ApiDescDetail:
        """Gets Description obj for method or property"""
        block = self.get_desc_block(a_id=a_id)
        return ApiDescDetail(block=block)

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_prams_info(self, a_id: str) -> ApiMethodPramsInfo:
        """Gets parameter info for all parameters of a a method"""
        block = self.get_proto_block(a_id=a_id)
        result = ApiMethodPramsInfo(
            block=block,
            name_info=self.name.get_obj(),
            ns=self.ns.namespace_str,
            long_names=self.__long_names
        )
        return result

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_method_ex(self, a_id: str) -> ApiMethodException:
        """Gets raises info for method"""
        block = self.get_proto_block(a_id=a_id)
        result = ApiMethodException(block=block)
        return result

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_proto_block(self, a_id: str) -> ApiProtoBlock:
        """Gets the block for a method information"""

        detail_block = self.get_detail_block(a_id=a_id)
        return ApiProtoBlock(block=detail_block)

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_desc_block(self, a_id: str) -> ApiDescBlock:
        """Gets the block for a method description"""
        detail_block = self.get_detail_block(a_id=a_id)
        return ApiDescBlock(block=detail_block)

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_desc_detail(self, a_id: str) -> ApiDescDetail:
        """Gets Description obj for method or property"""
        block = self.get_desc_block(a_id=a_id)
        return ApiDescDetail(block=block)
    # endregion Methods

    # region Properties
    @property
    def name(self) -> ApiName:
        if self.__api_data_name is None:
            self.__api_data_name = ApiName(
                soup=self.__soup_obj,
                rules_engine=self._get_name_rules_engine()
            )
        return self.__api_data_name

    @property
    def public_members(self) -> ApiPublicMembers:
        if self.__api_data_public_members is None:
            self.__api_data_public_members = ApiPublicMembers(self.soup_obj)
        return self.__api_data_public_members

    @property
    def func_block(self) -> ApiFunctionsBlock:
        """Gets Summary Functions block"""
        if self.__func_block is None:
            self.__func_block = ApiFunctionsBlock(
                self.public_members)
        return self.__func_block

    @property
    def properties_block(self) -> ApiPropertiesBlock:
        """Gets Summary Properties block"""
        if self.__properties_block is None:
            self.__properties_block = ApiPropertiesBlock(
                self.public_members)
        return self.__properties_block

    @property
    def interfaces_block(self) -> ApiInterfacesBlock:
        """Gets Summary Exported Interfaces block"""
        if self.__interfaces_block is None:
            self.__interfaces_block = ApiInterfacesBlock(
                self.public_members)
        return self.__interfaces_block

    @property
    def types_block(self) -> ApiTypesBlock:
        """Gets Summary Properties block"""
        if self.__types_block is None:
            self.__types_block = ApiTypesBlock(
                self.public_members)
        return self.__types_block

    @property
    def func_summary_rows(self) -> ApiSummaryRows:
        """Get Summary rows for functions"""
        if self.__func_summary_rows is None:
            self.__func_summary_rows = ApiSummaryRows(
                self.func_block)
        return self.__func_summary_rows

    @property
    def property_summary_rows(self) -> ApiSummaryRows:
        """Get Summary rows for Properties"""
        if self.__property_summary_rows is None:
            self.__property_summary_rows = ApiSummaryRows(
                self.properties_block)
        return self.__property_summary_rows

    @property
    def export_summary_rows(self) -> ApiSummaryRows:
        """Get Summary rows for Exported Interfaces"""
        if self.__export_summary_rows is None:
            self.__export_summary_rows = ApiSummaryRows(
                self.interfaces_block)
        return self.__export_summary_rows

    @property
    def func_summaries(self) -> ApiSummaries:
        """Get Summary info list for functions"""
        if self.__func_summaries is None:
            self.__func_summaries = ApiSummaries(
                block=self.func_summary_rows,
                name_info=self.name.get_obj(),
                ns=self.ns.namespace_str,
                long_names=self.__long_names)
        return self.__func_summaries

    @property
    def property_summaries(self) -> ApiSummaries:
        """Get Summary info list for Properties"""
        if self.__property_summaries is None:
            self.__property_summaries = ApiSummaries(
                block=self.property_summary_rows,
                name_info=self.name.get_obj(),
                ns=self.ns.namespace_str,
                long_names=self.__long_names)
        return self.__property_summaries

    @property
    def exported_summaries(self) -> ApiSummaries:
        """Get Summary info list for Exported Interfaces"""
        if self.__exported_summaries is None:
            self.__exported_summaries = ApiSummaries(
                block=self.export_summary_rows,
                name_info=self.name.get_obj(),
                ns=self.ns.namespace_str,
                long_names=self.__long_names)
        return self.__exported_summaries

    @property
    def inherited(self) -> 'ApiInherited':
        """Gets class that get all inherited value"""
        if self.__inherited is None:
            ni = self.name.get_obj()
            self.__inherited = ApiInherited(
                soup=self.soup_obj,
                area_filter_rules_engine=self.area_filter_rules_engine,
                class_name=ni.name,
                ns=self.ns.namespace_str,
                raise_error=False,
                allow_cache=self.allow_cache
            )
        return self.__inherited

    @property
    def types_summary_rows(self) -> ApiSummaryRows:
        """Get Summary rows for Properties"""
        if self.__type_summary_rows is None:
            self.__type_summary_rows = ApiSummaryRows(
                block=self.types_block)
        return self.__type_summary_rows

    @property
    def types_summaries(self) -> ApiSummaries:
        """Get Summary info list for Properties"""
        if self.__type_summaries is None:
            self.__type_summaries = ApiSummaries(
                block=self.types_summary_rows,
                name_info=self.name.get_obj(),
                ns=self.ns.namespace_str,
                long_names=self.__long_names)
        return self.__type_summaries

    @property
    def desc(self) -> ApiDesc:
        """Gets the interface Description object"""
        if self.__desc is None:
            self.__desc = ApiDesc(self.soup_obj)
        return self.__desc

    @property
    def ns(self) -> ApiNamespace:
        """Gets the interface Description object"""
        if self.__ns is None:
            self.__ns = ApiNamespace(
                self.soup_obj)
        return self.__ns

    @property
    def soup_obj(self) -> SoupObj:
        """Gets soup_obj value"""
        return self.__soup_obj

    @property
    def url_obj(self) -> UrlObj:
        return self.__soup_obj.url_obj

    @property
    def area_filter_rules_engine(self) -> IRulesArea:
        if self.__area_filter_rules_engine is None:
            self.__area_filter_rules_engine = RulesArea(
                remove_parent_inherited=self.remove_parent_inherited)
            self._set_area_filter_rules_engine_rules(
                rules_engine=self.__area_filter_rules_engine
            )
        return self.__area_filter_rules_engine

    @property
    def allow_cache(self) -> bool:
        """Specifies allow_cache

            :getter: Gets allow_cache value.
            :setter: Sets allow_cache value.
        """
        return self.__allow_cache

    @allow_cache.setter
    def allow_cache(self, value: bool):
        self.__allow_cache = value

    @property
    def remove_parent_inherited(self) -> bool:
        """Gets remove_parent_inherited value"""
        return self.__remove_parent_inherited
    # endregion Properties
