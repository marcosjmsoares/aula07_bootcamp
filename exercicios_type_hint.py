# Exercícios
# Vamos revisar funções adicionando type hints e Pydantic
from pydantic import BaseModel, field_validator, ValidationError
from typing import List, Dict, Optional
import csv

#####LER CSV
def ler_csv(nome_do_Arquivo_csv: str) -> list[dict]:
    """
    Funcao que le um arquivo csv e retorna uma lista de
    dicionarios"""

    lista = []
    with open(nome_do_Arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista


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

