# coding: utf-8
from typing import Dict, List, cast
from _base_interface import BaseInterface
from _base_json import EventArgs

from _base_interface import MethodArgsTyped, MethodTyped


class BaseInterfacePyi(BaseInterface):
    def on_after_init_data(self, args: EventArgs) -> None:
        super().on_after_init_data(args=args)

    # region Overrides
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

        if arg_type == "object":
            arg_type = "typing.Any"
        return f"{self.get_safe_word(arg['name'])}: {arg_type}"

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
                    q_type = self.get_q_type(ret)
                    if q_type == "object":
                        q_type = "typing.Any"
                    result += f" -> {q_type}"

        result += ":"
        return result

    # endregion Overrides
