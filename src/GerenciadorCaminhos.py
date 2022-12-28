from pathlib import Path

from config import DIRETORIO_DATA, DIRETORIO_PLANILHAS, DIRETORIO_MSG
from exceptions import ErroDiretorioDataNaoEncontrado, ErroDiretorioPlanilhasNaoEncontrado, ErroDiretorioMensagensNaoEncontrado

#TODO: Criar um método para verficar quais mensagens estão presentes no diretório mensagem
class GerenciadorCaminhos:
    """
    GerenciadorCaminhos
    ---
    Classe responsável por gerenciar os caminhos (`paths`) para os diretórios e arquivos importantes para o funcionamento do código. Carrega os `paths` presentes em `config.py` ou carrega os novos caminhos definidos pelo usuário.
    """

    def __init__(self) -> None:
        self.__dir_data = Path(DIRETORIO_DATA)
        self.__dir_planilhas = Path(DIRETORIO_DATA, DIRETORIO_PLANILHAS)
        self.__dir_mensagens = Path(DIRETORIO_DATA, DIRETORIO_MSG)

    def verificar_diretorios(self):
        """
        Método responsável por verificar se os diretórios `data/`, `data/planilhas/` ou `data/mensagens/` existem. Caso não existam, dispara uma `Exception`.
        """
        if not self.dir_data.exists():
            raise ErroDiretorioDataNaoEncontrado('ERRO: Diretório "data/" não foi encontrado')
        if not self.dir_planilhas.exists():
            raise ErroDiretorioPlanilhasNaoEncontrado('ERRO: Diretório "data/planilhas/" não foi encontrado')
        if not self.dir_mensagens.exists():
            raise ErroDiretorioMensagensNaoEncontrado('ERRO: Diretório "data/mensagens/" não foi encontrado')
        print('Todos os diretórios nos locais corretos!')

    def verificar_arquivos(self):
        pass

    """
    Métodos Getters e Setters
    ===
    Os métodos abaixo servem apenas para acessarmos (getters) e alterarmos (setters) os valores dos atributos privados da classe.
    """

    @property
    def dir_data(self):
        return self.__dir_data

    @dir_data.setter
    def dir_data(self, novo_caminho):
        self.__dir_data = Path(novo_caminho)
    
    @property
    def dir_planilhas(self):
        return self.__dir_planilhas

    @dir_planilhas.setter
    def dir_planilhas(self, novo_caminho):
        self.__dir_planilhas = Path(novo_caminho)
    
    @property
    def dir_mensagens(self):
        return self.__dir_mensagens

    @dir_mensagens.setter
    def dir_mensagens(self, novo_caminho):
        self.__dir_mensagens = Path(novo_caminho)