# coding: utf-8
from _base_interface import BaseInterface
from pathlib import Path

class ExtBaseInterface(BaseInterface):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

