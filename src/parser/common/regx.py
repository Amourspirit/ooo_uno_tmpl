# coding: utf-8
import re

pattern_http = re.compile(r"^https?:\/\/")

pattern_id = re.compile(r'[a-z0-9]{28,38}')
