# coding: utf-8
import hashlib
from .db_module_json import DbModuleJson
from ..data_class.component import Component


class ParserBase:
    def __init__(self, db: DbModuleJson, component: Component) -> None:
        self._db = db
        self._component = component

    def get_id(self, ns: str) -> str:
        """
        Creates and unique id for current component based upon component id and ``ns``.

        Args:
            ns (str): namespace

        Returns:
            str: mdf hashed id
        """
        key = self._component.id_component + ns
        result = hashlib.md5(key.encode('utf-8')).hexdigest()
        return result

    # region Properties
    @property
    def db(self) -> DbModuleJson:
        return self._db
    
    @property
    def component(self) -> Component:
        return self._component
    # endregion Properties