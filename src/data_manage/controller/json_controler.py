# coding: utf-8
from typing import Any, Union
from ...cfg.config import AppConfig
from ..json_merge import JsonMerge
from ..util import Util


class JsonController:
    def __init__(self, config: AppConfig, **kwargs) -> None:
        self._config = config
        self._namespace: Union[str, None] = kwargs.get('namespace', None)

    def results(self) -> Any:
        if self._namespace:
            return Util.get_formated_dict_list_str(self._get_data())

    def _get_data(self) -> dict:
        j_merge = JsonMerge(
            config=self._config,
            full_ns=self._namespace)

        return j_merge.get_merged()
