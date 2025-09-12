# Exercícios
# Vamos revisar funções adicionando type hints e Pydantic
from pydantic import BaseModel, field_validator, ValidationError
from typing import List, Dict, Optional
import csv

class ItemVenda(BaseModel):
    Produto: str
    Categoria: str
    Quantidade: int
    Venda: int

    # Validador para garantir valores positivos
    @field_validator('Quantidade', 'Venda')
    def valores_positivos(cls, v):
        assert v >= 0, 'deve ser positivo'
        return v

class CategoriaDados(BaseModel):
    Categoria: str
    Itens: List[ItemVenda]
    TotalVendas: Optional[int] = 0


#####LER CSV
def ler_csv(nome_do_Arquivo_csv: str) -> List[ItemVenda]:
    dados_validados = []
    with open(nome_do_Arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            try:
                item = ItemVenda(**linha)
                dados_validados.append(item)
            except ValidationError as e:
                print(f"Erro de validação: {e.json()}")
    return dados_validados




# 1-Calcular Média de Valores em uma Lista
def calcular_media_dos_valores(lista: list[dict]) -> float:
    """
    Funcao que calcula a media dos valores de uma lista
    """
    valor_media = 0
    quantidade_itens = 0
    for produto in lista:
        valor_media += float(produto.get("preco"))
        quantidade_itens += 1
    return valor_media/quantidade_itens



# 2-Filtrar Dados Acima de um Limite


# 3-Contar Valores Únicos em uma Lista


# 4-Converter Celsius para Fahrenheit em uma Lista


# 5-Calcular Desvio Padrão de uma Lista


# 6-Encontrar Valores Ausentes em uma Sequência

