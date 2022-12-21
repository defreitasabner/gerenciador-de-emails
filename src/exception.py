class ErroColunasEsperadas(Exception):
    """
    Erro que ocorre quando as colunas presentes no arquivo `.csv` não correspondem às colunas presentes na propriedade `coluna_esperada` do objeto `Planilha`.
    """
    pass