# coding: utf-8
from verr import Version
from typing import Dict, Iterable, Set, Tuple, List, Union, TypedDict
from _base_json import BaseJson
from _base_tmpl import SqlComponent
from src.model.interface.model_interface import ModelInterface
from src.data_manage.data_class.component import Component
from src.data_manage.data_class.component_kind import ComponentKind

# region TypedDict

class MethodArgsTyped(TypedDict):
    name: str
    type: str
    direction: str
    origin: str


class MethodTyped(TypedDict):
    name: str
    type: str
    desc: List[str]
    returns: str
    returns_origin: str
    raises: List[str]
    args: List[MethodArgsTyped]


class PropertyTyped(TypedDict):
    name: str
    returns: str
    origin: str
    origtype: Union[str, None]
    desc: List[str]
    raises_get: str
    raises_set: str

# endregion TypedDict

class BaseInterface(BaseJson):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quote: Set[str]
        self.namespace: str
        self.allow_db: bool
        self.desc: List[str]
        self.typings: Set[str]
        self.link: str
        self.requires_typing: bool
        self.inherits: List[str]
        self.extends_map: Dict[str, str]
        self.imports: List[str]
        self.attribs: dict

    def _hydrate_data(self, json_data: dict):
        try:
            self._model = ModelInterface(**json_data)
        except Exception as e:
            msg = f"Error occurred in interface {json_data['namespace']}.{json_data['name']}"
            self._lerr(f"{msg}\n{e}")
            raise Exception(msg) from e
        # self._validate_data(json_data)
        mdata = self._model.data
        self.name = self.get_safe_word(mdata.name)
        self.namespace = mdata.namespace
        self.allow_db = mdata.allow_db
        self.desc = mdata.desc
        self.link = mdata.url
        self.libre_office_ver = self._model.libre_office_ver
        self.include_desc = self._model.writer_args.include_desc
        self.requires_typing = mdata.requires_typing
        self.inherits = mdata.extends
        self.imports = mdata.imports
        self.extends_map.update(mdata.extends_map)

        sort = self._model.parser_args.sort
        self.attribs = self._get_attribs(json_data=json_data, sort=sort)
        self.from_imports = [x.as_tuple() for x in mdata.from_imports]
        self.from_imports_typing = [x.as_tuple() for x in mdata.from_imports_typing]
        self.quote.update(mdata.quote)
        self.typings.update(mdata.typings)

        # if a method or property has a enum type then we need to import `com.sun.star.UnoEnumProto`.
        # Also the enum that was to be imported needs to removed from the imports list.
        if self.allow_db:
            self.enum_methods_args = self.get_methods_arg_enum_components()
            self.enum_methods_return = self.get_methods_return_enum_components()
            self.enum_properties = self.get_properties_enum_components()
            self.remove_enum_imports()
            self.add_enum_imports()
        else:
            self.enum_methods_args = {}
            self.enum_methods_return = {}
            self.enum_properties = {}

    # region Adjust for Enums
    @property
    def has_enums(self) -> bool:
        """
        Returns True if the interface has enums.
        """
        try:
            return self._has_enum_prop_method_arg
        except AttributeError:
            self._has_enum_prop_method_arg = self.enum_methods_args or self.enum_methods_return or self.enum_properties
            return self._has_enum_prop_method_arg

    def add_enum_imports(self):
        """
        Adds the enum imports to the list of imports.
        """

        def add_to_imports(comp: Component):
            for imp in self.from_imports_typing:
                if imp[0] == comp.id_component and imp[1] == f"{comp.name}Proto":
                    return
            self.from_imports_typing.append((comp.id_component, f"{comp.name}Proto"))

        if not self.has_enums:
            return
        # from com.sun.star import UnoEnumProto
        if self.enum_properties:
            for comp in self.enum_properties.values():
                add_to_imports(comp)
        if self.enum_methods_return:
            for comp in self.enum_methods_return.values():
                add_to_imports(comp)
        if self.enum_methods_args:
            for method_args in self.enum_methods_args.values():
                for comp in method_args.values():
                    add_to_imports(comp)

    def remove_enum_imports(self) -> None:
        """
        Removes the enum imports from the list of imports.
        """

        def remove_from_imports(comps: Iterable[Component]):
            for comp in comps:
                for imp in self.from_imports[:]:  # iterate over copy to we can remove from the list
                    if imp[1] == comp.name:
                        self.from_imports.remove(imp)

        def remove_from_imports_typing(comps: Iterable[Component]):
            for comp in comps:
                for imp in self.from_imports_typing[:]:  # iterate over copy to we can remove from the list
                    if imp[1] == comp.name:
                        self.from_imports_typing.remove(imp)

        if not self.has_enums:
            return
        # remove from imports
        if self.enum_properties:
            remove_from_imports(self.enum_properties.values())
            remove_from_imports_typing(self.enum_properties.values())

        if self.enum_methods_return:
            remove_from_imports(self.enum_methods_return.values())
            remove_from_imports_typing(self.enum_methods_return.values())

        if self.enum_methods_args:
            for method_args in self.enum_methods_args.values():
                for comp in method_args.values():
                    remove_from_imports([comp])
                    remove_from_imports_typing([comp])

    # endregion Adjust for Enums

    # region Enum Components
    def get_methods_arg_enum_components(self) -> Dict[str, Dict[str, Component]]:
        """
        Returns a dictionary of components that are enums and are used as method argument types.

        The key is the method name and the value is a dictionary of argument name and component.
        """
        methods = self._model.data.items.methods
        if not methods:
            return {}
        qry = SqlComponent()
        result: Dict[str, Dict[str, Component]] = {}
        for method in methods:
            for m_arg in method.args:
                if m_arg.origin:
                    comp = qry.get_component(m_arg.origin, ComponentKind.ENUM)
                    if comp:
                        if result.get(method.name) is None:
                            result[method.name] = {}
                        result[method.name][m_arg.name] = comp
        return result

    def get_methods_return_enum_components(self) -> Dict[str, Component]:
        """
        Returns a dictionary of components that are enums and are used as method return types.

        The key is the method name and the value is the component.
        """
        methods = self._model.data.items.methods
        if not methods:
            return {}
        qry = SqlComponent()
        result: Dict[str, Component] = {}
        for method in methods:
            if method.returns_origin:
                comp = qry.get_component(method.returns_origin, ComponentKind.ENUM)
                if comp:
                    result[method.name] = comp

        return result

    def get_properties_enum_components(self) -> Dict[str, Component]:
        """
        Returns a dictionary of components that are enums and are used as property types.

        The key is the property name and the value is the component.
        """
        properties = self._model.data.items.properties
        if not properties:
            return {}
        qry = SqlComponent()
        result: Dict[str, Component] = {}
        for prop in properties:
            if prop.origin:
                comp = qry.get_component(prop.origin, ComponentKind.ENUM)
                if comp:
                    result[prop.name] = comp
        return result

    # endregion Enum Components

    def _get_attribs(self, json_data: dict, sort: bool) -> dict:
        items: dict = json_data["data"]["items"]
        if not sort:
            return items

        def sort_lst_dict(_key: str, sort_key: str) -> List[dict]:
            key_index: List[Tuple[str, int]] = []
            lst = items[_key]  # methods
            if len(lst) == 0:
                return lst
            for i, itm in enumerate(lst):
                key_index.append((itm[sort_key], i))
            key_index.sort()
            sorted_lst = []
            for k_i in key_index:
                sorted_lst.append(lst[k_i[1]])
            return sorted_lst

        keys = items.keys()
        result = {}
        for k in keys:
            result[k] = sort_lst_dict(k, "name")
        return result

    def _validate_data(self, data: dict) -> bool:
        super()._validate_data(data=data)

        if not data["type"] == "interface":
            raise Exception(f"Invalid Data: Expected type to be 'interface' got '{data['type']}'")

        if not data["name"]:
            raise Exception("Invalid Data: name attribute is not valid")
        min_ver = Version(0, 1, 1)
        ver = Version.parse(data.get("version", None))
        if ver < min_ver:
            raise Exception("Invalid Data: Expected version to be at least '{min_ver}' got {ver}")

    # region Get Formatted Method
    def _get_formatted_arg(self, method_name: str, arg: MethodArgsTyped) -> str:
        arg_type = self.get_q_type(arg["type"])

        if self.allow_db and self.enum_methods_args:
            # self.enum_methods_args is a dictionary of method name and a dictionary of arg name and a list of components
            method_info = self.enum_methods_args.get(method_name)
            if method_info:
                # method_info is a dictionary of arg name and a list of components
                # we have a dictionary of arg name and a list of components
                method_arg_comp = method_info.get(arg["name"])
                if method_arg_comp:
                    arg_type = f"{method_arg_comp.name}Proto"

        return f"{self.get_safe_word(arg['name'])}: {arg_type}"

    def get_args(self, method_name: str, args: List[MethodArgsTyped]) -> str:
        result = ""
        for i, arg in enumerate(args):
            if i > 0:
                result += ", "
            result += self._get_formatted_arg(method_name=method_name, arg=arg)
        return result

    def get_out_args(self, meth: MethodTyped) -> List[str]:
        args = meth["args"]
        results: List[str] = []
        for arg in args:
            direction = arg["direction"]
            if self.is_out_arg(direction):
                results.append(arg["name"])
        return results

    def _get_raises_list(self, d: dict, key: str) -> List[Tuple[str, str]]:
        """
        Converts any raises into a list of tuple.
        First part full name.
        Second Part Short name
        """
        results = []
        if key in d:
            lst = d[key]
            for r in lst:
                results.append((r, self.get_last_part(r)))
        return results

    def get_raises_list(self, meth: dict) -> List[Tuple[str, str]]:
        """
        Converts any raises into a list of tuple.
        First part full name.
        Second Part Short name
        """
        return self._get_raises_list(d=meth, key="raises")

    def get_prop_get_raises(self, prop: dict) -> List[Tuple[str, str]]:
        """
        Converts any raises into a list of tuple.
        First part full name.
        Second Part Short name
        """
        return self._get_raises_list(d=prop, key="raises_get")

    def get_prop_set_raises(self, prop: dict) -> List[Tuple[str, str]]:
        """
        Converts any raises into a list of tuple.
        First part full name.
        Second Part Short name
        """
        return self._get_raises_list(d=prop, key="raises_set")

    def get_prop_get_has_errors(self, prop: dict) -> bool:
        if "raises_get" in prop:
            if len(prop["raises_get"]) > 0:
                return True
        return False

    def get_prop_set_has_errors(self, prop: dict) -> bool:
        if "raises_set" in prop:
            if len(prop["raises_set"]) > 0:
                return True
        return False

    def get_prop_has_errors(self, prop: dict) -> bool:
        if self.get_prop_get_has_errors(prop):
            return True
        if self.get_prop_set_has_errors(prop):
            return True
        return False

    def get_formated_meth(self, meth: MethodTyped) -> str:
        def get_enum_return_type(method_name: str) -> str:
            ret_val = ""
            method_comp = self.enum_methods_return.get(method_name)
            if method_comp:
                # method_info is a list of components
                # we have a list of components
                ret_val = f"{method_comp.name}Proto"
            return ret_val

        name = meth["name"]
        iter_args: list = meth["args"]
        if len(iter_args) > 0:
            args = "self, " + self.get_args(method_name=name, args=meth["args"])
        else:
            args = "self"
        result = f"def {name}({args})"
        key = "returns"
        if key in meth:
            ret = meth[key]
            if ret:
                enum_name = ""
                if self.allow_db and self.enum_methods_return:
                    enum_name = get_enum_return_type(method_name=name)
                if enum_name:
                    result += f" -> {enum_name}"
                else:
                    result += f" -> {self.get_q_type(ret)}"
        result += ":"
        return result

    # endregion Get Formatted Method
    
    # region Get Formatted Property
    def get_property_return(self, prop: PropertyTyped) -> str:
        # $self.get_q_type($property['returns'])
        name = prop["name"]
        returns = prop["returns"]
        result = self.get_q_type(returns)
        if self.allow_db and self.enum_properties:
            comp = self.enum_properties.get(name)
            if comp:
                result = f"{comp.name}Proto"
        return result
        
    # endregion Get Formatted Property