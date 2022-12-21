from pathlib import Path

from config import DIRETORIO_DATA, DIRETORIO_PLANILHAS, DIRETORIO_MSG
from exception import ErroDiretorioDataNaoEncontrado, ErroDiretorioPlanilhasNaoEncontrado, ErroDiretorioMensagensNaoEncontrado

class GerenciadorCaminhos:
    """
    Classe responsável por gerenciar os caminhos (`paths`) para os diretórios e arquivos importantes para o funcionamento do código. Carrega os `paths` presentes em `config.py` ou carrega os novos caminhos definidos pelo usuário.
    """

    def __init__(self) -> None:
        self.dir_data = Path(DIRETORIO_DATA)
        self.dir_planilhas = Path(DIRETORIO_DATA, DIRETORIO_PLANILHAS)
        self.dir_mensagens = Path(DIRETORIO_DATA, DIRETORIO_MSG)

    def verifica_diretorios(self):
        """
        Método responsável por verificar se os diretórios `data/`, `data/planilhas/` ou `data/mensagens/` existem. Caso não existam, dispara uma `Exception`.
        """
        if not self.dir_data.exists():
            raise ErroDiretorioDataNaoEncontrado('ERRO: Diretório "data/" não foi encontrado')
        if not self.dir_planilhas.exists():
            raise ErroDiretorioPlanilhasNaoEncontrado('ERRO: Diretório "data/planilhas/" não foi encontrado')
        if not self.dir_mensagens.exists():
            raise ErroDiretorioMensagensNaoEncontrado('ERRO: Diretório "data/mensagens/" não foi encontrado')

    def verifica_arquivos(self):
        pass