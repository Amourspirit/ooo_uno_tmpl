# coding: utf-8
from .api_summary_block import ApiSummaryBlock


class ApiInterfacesBlock(ApiSummaryBlock):
    """Gets Block object for Exported Interfaces"""

    def _get_match_name(self) -> str:
        return 'interfaces'
