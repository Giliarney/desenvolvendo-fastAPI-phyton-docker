from typing import Annotated
from pydantic import UUID4, BaseModel, Field
from datetime import datetime


class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from_atributte = True


class OutMixIn(BaseSchema):
    id: Annotated[UUID4, Field(description = 'Identificador')]
    created_at: Annotated[datetime, Field(description = 'Data de Criação')]

