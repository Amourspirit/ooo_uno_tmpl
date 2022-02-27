# coding: utf-8
from typing import List
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw
from kwhelp import rules
from ..common.constants import URL_SPLIT
from ..common.log_load import Log
log = Log()

class UrlObj:
    """Properties of url"""
    @RuleCheckAllKw(
        arg_info={
            "url": rules.RuleStrNotNullEmptyWs,
            "has_name": rules.RuleBool
        },
        ftype=DecFuncEnum.METHOD
    )
    def __init__(self, url: str, **kwargs):
        """
        Constructor

        Args:
            url (str): Url

        Keyword Arguments:
            has_name (bool, optional): If ``True`` name is extracted from
                url and namespace excludes name. Default ``True``
        """
        self._url = url
        self._has_name = kwargs.get('has_name', True)
        u_parts = self._url.rsplit('/', 1)
        # similar to: namespacecom_1_1sun_1_1star_1_1style.html#a3ae28cb49c180ec160a0984600b2b925
        self._page_link = u_parts[1]
        self._url_base = u_parts[0]
        f_parts = self._url.split(sep='#', maxsplit=1)
        if len(f_parts) > 1:
            self._url_only = f_parts[0]
            self._fragment = f_parts[1]
            self._is_frag = True
        else:
            self._url_only = self._url
            self._fragment = ''
            self._is_frag = False
        self._name = None if self._has_name else ''

        self._ns = None
        self._ns_str = None
        self._ext = None

    def get_split_ns(self) -> List[str]:
        result = []
        try:
            ns_part = self._page_link.split('.')[0]
            s = ns_part.replace(URL_SPLIT, '.').lstrip('.')

            # in some cases such as generics the name can have _3_01 and or _01_4 in the last part of the name
            # best guess _3 is < and _4 is > and _01 is space.
            # just split _3 dropping the end
            s = s.rsplit(sep='_3', maxsplit=1)[0]

            # https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1Pair_3_01T_00_01U_01_4.html
            # the frist part on the str usually is prefixed with namespace, interface or whatever.
            # namespace always start with com so just drop the first part to clean it up.
            s = 'com.' + s.split('.', maxsplit=1)[1]
            result = s.split('.')
        except Exception as e:
            log.logger.error(e)
            log.logger.info('UrlObj._get_ns() returning empty list.')
        return result

    def _get_ns(self) -> List[str]:
        try:
            result = self.get_split_ns()

            # get that last item
            self._name = result[-1:][0]
            # Drop the component from the result
            if self._has_name:
                self._ns = result[:-1]
            else:
                self._ns = result
        except Exception as e:
            log.logger.error(e)
            log.logger.info('UrlObj._get_ns() returning empty list.')
        return result

    @property
    def page_link(self) -> str:
        """
        Gets page link similar to ``namespacecom_1_1sun_1_1star_1_1style.html#a3ae28cb49c180ec160a0984600b2b925``
        """
        return self._page_link

    @property
    def fragment(self) -> str:
        """
        Gets fragment simalar to a3ae28cb49c180ec160a0984600b2b925
        """
        return self._fragment

    @property
    def name(self) -> str:
        """
        Get name portion of html link such as SpinningProgressControlModel
        """
        if self._name is None:
            self._get_ns()
        return self._name

    @property
    def is_fragment(self) -> bool:
        """
        Gets if there is a fragment
        """
        return self._is_frag

    @property
    def namespace(self) -> List[str]:
        """
        Gets Namespace in format of ['com', 'sun', 'star', 'style']
        """
        if self._ns is None:
            self._get_ns()
        return self._ns

    @property
    def namespace_str(self) -> str:
        """
        Gets namespace in format of 'com.sun.star.style'
        """
        if not self._ns_str:
            self._ns_str = '.'.join(self.namespace)
        return self._ns_str

    @property
    def url(self) -> str:
        """Gets url value"""
        return self._url

    @property
    def url_base(self) -> str:
        """
        Gets url base value such as:
        ``https://api.libreoffice.org/docs/idl/ref``
        """
        return self._url_base

    @property
    def url_only(self) -> str:
        """
        Gets full url without fragment
        """
        return self._url_only

    @property
    def ext(self) -> str:
        """Gets ext value such as ``.html`` or ``.png``"""
        if self._ext is None:
            parts = self.url_only.rsplit(sep='.', maxsplit=1)
            self._ext = '' if len(parts) == 1 else ('.' + parts[1])
        return self._ext

