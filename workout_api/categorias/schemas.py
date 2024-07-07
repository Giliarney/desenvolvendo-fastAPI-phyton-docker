from typing import Annotated

from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchema


class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description = 'Nome da Categoria', example = 'Musculação', max_length = 20)]


class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description = 'Identificador da Categoria')]
