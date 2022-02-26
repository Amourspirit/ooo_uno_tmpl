# coding: utf-8
from .api_summary_block import ApiSummaryBlock


class ApiTypesBlock(ApiSummaryBlock):
    def _get_match_name(self) -> str:
        return 'pub-types'
