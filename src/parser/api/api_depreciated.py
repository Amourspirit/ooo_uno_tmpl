# coding: utf-8
from ..web.soup_obj import SoupObj
from ..web.block_obj import BlockObj


class ApiDepreciated(BlockObj):
    """Gets if block is deprecated"""
    # eg: https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XVclContainerPeer.html

    def __init__(self, soup: SoupObj):
        super().__init__(soup)
        self._data = None

    def get_obj(self) -> bool:
        """
        Gets See alos of Interface

        Returns:
            str: See also. if it exist; Otherwise empty string.
        """
        if not self._data is None:
            return self._data
        soup = self.soup.soup
        tag = soup.select_one('div.textblock > dl.deprecated')
        if tag:
            self._data = True
        else:
            self._data = False
        return self._data
