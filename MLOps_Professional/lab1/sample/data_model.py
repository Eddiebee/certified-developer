from pydantic import BaseModel

from typing import Union

class MaintenancePayload(BaseModel):
    temperature: Union[int, None] = None
    pressure: Union[int, None] = None