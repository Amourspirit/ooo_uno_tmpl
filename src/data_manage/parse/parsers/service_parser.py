from ....model.service.model_service import ModelService
class ServiceParser:
    
    
    def __init__(self, json_data: dict, file: str) -> None:
        self._mod = ModelService(**json_data)
        self._file = file
        self._extends = []
        