class ErroColunasEsperadas(Exception):
    """
    Erro que ocorre quando as colunas presentes no arquivo `.csv` não correspondem às colunas presentes na propriedade `coluna_esperada` do objeto `Planilha`.
    """
    pass

# Exceptions relativas à classe GerenciadorCaminhos
class ErroDiretorioDataNaoEncontrado(Exception):
    """
    Erro disparado quando o diretório `data/` não é encontrado na raiz do projeto.
    """
    pass

class ErroDiretorioPlanilhasNaoEncontrado(Exception):
    """
    Erro disparado quando o diretório `data/planilhas/` não é encontrado na raiz do projeto.
    """
    pass

class ErroDiretorioMensagensNaoEncontrado(Exception):
    """
    Erro disparado quando o diretório `data/mensagens/` não é encontrado na raiz do projeto.
    """
    pass