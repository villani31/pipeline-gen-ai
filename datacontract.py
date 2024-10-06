from datetime import datetime
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, Field
from enum import Enum

class ProductEnum(str, Enum):
    produto1 = "Produto 01"
    produto2 = "Produto 02"
    produto3 = "Produto 03"

class Vendas(BaseModel):
    """
    Modelo de dados para as vendas.

    Args:
        nome (str, min 3, max 50) nome do vendedor
        email (EmailStr): email do vendedor
        data (datetime): data da venda
        valor (PositiveFloat): valor da venda
        produto (PositiveInt): nome do produto
        quantidade (PositiveInt): quantidade de produtos vendido
        produto (ProdutoEnum): categoria do produto
    """

    nome: str = Field(min_length=3, max_length=50, pattern=r"^[a-zA-Z\s]+$")
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProductEnum
    