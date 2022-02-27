# coding: utf-8
from pydantic import BaseModel
from typing import List
from .from_import import FromImport

class FromImports(BaseModel):
    from_imports: List[FromImport]
