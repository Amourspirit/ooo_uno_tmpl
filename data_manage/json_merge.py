# coding: utf-8
"""
Manages merging of component json files
"""
import os
import json
from pathlib import Path
from typing import List
from config import AppConfig


class JsonMerge:
    def __init__(self, config: AppConfig, files: List[str]) -> None:
        self._config = config
        self._files = files
        project_root = os.environ.get('project_root', None)
        if project_root is None:
            raise Exception("project_root environment variable not set")
        self._project_root = Path(project_root)

    def _get_file_json(self, file: str) -> dict:
        file_path = self._project_root.joinpath(file)

        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    def get_merged_data(self) -> dict:
        requires_typing = False

        result_data = {
            "quote": [],
            "typings": [],
            "requires_typing": False,
            "full_imports": {
                "general": [],
                "typing": []
            },
            "items": {}
        }

        # region SETS
        quotes = set()
        typings = set()
        full_imp_general = set()
        full_imp_typing = set()
        itm_methods = set()
        itm_types = set()
        itm_properties = set()
        # endregion SETS

        # region process Methods
        def process_quote_data(data: dict) -> None:
            lst = data.get('quote', [])
            quotes.update(lst)

        def process_typings_data(data: dict) -> None:
            lst = data.get('typings', [])
            typings.update(lst)

        def process_full_imp_gen_data(data: dict) -> None:
            lst = data['full_imports'].get('general', [])
            full_imp_general.update(lst)

        def process_full_imp_typing_data(data: dict) -> None:
            lst = data['full_imports'].get('typing', [])
            full_imp_typing.update(lst)

        def process_itm_methods(data: dict) -> None:
            lst = data['items'].get('methods', [])
            is_init = False
            for d in lst:
                name = d['name']
                if name in itm_methods:
                    continue
                itm_methods.add(name)

                if not is_init:
                    is_init = True
                    if not 'methods' in result_data['items']:
                        result_data['items']['methods'] = []
                result_data['items']['methods'].append(d)

        def process_itm_types(data: dict) -> None:
            lst = data['items'].get('types', [])
            is_init = False
            for d in lst:
                name = d['name']
                if name in itm_types:
                    continue
                itm_types.add(name)

                if not is_init:
                    is_init = True
                    if not 'types' in result_data['items']:
                        result_data['items']['types'] = []
                result_data['items']['types'].append(d)

        def process_itm_properties(data: dict) -> None:
            lst = data['items'].get('types', [])
            is_init = False
            for d in lst:
                name = d['name']
                if name in itm_properties:
                    continue
                itm_properties.add(name)

                if not is_init:
                    is_init = True
                    if not 'properties' in result_data['items']:
                        result_data['items']['properties'] = []
                result_data['items']['properties'].append(d)

        def process_requires_typing(data: dict) -> None:
            nonlocal requires_typing
            req = bool(data.get('requires_typing', False))
            if req:
                requires_typing = True
        # endregion process Methods

        for file in self._files:
            j_data_dict = self._get_file_json(file)
            j_data: dict = j_data_dict['data']
            process_quote_data(j_data)
            process_typings_data(j_data)
            process_full_imp_gen_data(j_data)
            process_full_imp_typing_data(j_data)
            process_itm_methods(j_data)
            process_requires_typing(j_data)
            process_itm_types(j_data)
            process_itm_properties(j_data)

        if len(quotes) > 0:
            result_data['quote'].extend(quotes)

        if len(typings) > 0:
            result_data['typings'].extend(quotes)

        if len(full_imp_general) > 0:
            result_data['full_imports']['general'].extend(full_imp_general)

        if len(full_imp_typing) > 0:
            result_data['full_imports']['typing'].extend(full_imp_typing)

        result_data['requires_typing'] = requires_typing

        return result_data
