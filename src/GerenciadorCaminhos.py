import os
from pathlib import Path

from caminhos import *
from exceptions import ErroDiretorioDataNaoEncontrado, ErroDiretorioPlanilhasNaoEncontrado, ErroDiretorioMensagensNaoEncontrado

#TODO: Melhorar verificação de arquivo, informar quais arquivos não foram encontrados
class GerenciadorCaminhos:
    """
    GerenciadorCaminhos
    ---
    Classe responsável por gerenciar os caminhos (`paths`) para os diretórios e arquivos importantes para o funcionamento do código. Carrega os `paths` presentes em `config.py` ou carrega os novos caminhos definidos pelo usuário.
    """

    def __init__(self) -> None:
        self.__dir_data = Path(DIRETORIO_DATA)
        self.__dir_planilhas = Path(DIRETORIO_PLANILHAS)
        self.__dir_mensagens = Path(DIRETORIO_MSG)

    def verificar_diretorios(self):
        """
        Método responsável por verificar se os diretórios `data/`, `data/planilhas/` ou `data/mensagens/` existem. Caso não existam, dispara uma `Exception`.
        """
        if not self.dir_data.exists():
            raise ErroDiretorioDataNaoEncontrado('Diretório "data/" não foi encontrado')
        if not self.dir_planilhas.exists():
            raise ErroDiretorioPlanilhasNaoEncontrado('Diretório "data/planilhas/" não foi encontrado')
        if not self.dir_mensagens.exists():
            raise ErroDiretorioMensagensNaoEncontrado('Diretório "data/mensagens/" não foi encontrado')

    def verificar_existencia_arquivos_mensagem_etapas_ps(self):
        if not os.path.exists(MSG_FORMULARIO_APROVADO) and not os.path.exists(MSG_FORMULARIO_REPROVADO):
            raise Exception('Não existem arquivos de mensagens de "aprovado" e "reprovado" para etapa Formulário. Por favor, crie os arquivos necessários (formulario_aprovado.txt e formulario_reprovado.txt) e adicione as mensagens adequadas.')
        if not os.path.exists(MSG_DINAMICA_APROVADO) and not os.path.exists(MSG_DINAMICA_REPROVADO):
            raise Exception('Não existem arquivos de mensagens de "aprovado" e "reprovado" para etapa Dinâmica. Por favor, crie os arquivos necessários (dinamica_aprovado.txt e dinamica_reprovado.txt) e adicione as mensagens adequadas.')
        if not os.path.exists(MSG_ENTREVISTA_APROVADO) and not os.path.exists(MSG_ENTREVISTA_REPROVADO):
            raise Exception('Não existem arquivos de mensagens de "aprovado" e "reprovado" para etapa Entrevista. Por favor, crie os arquivos necessários (entrevista_aprovado.txt e entrevista_reprovado.txt) e adicione as mensagens adequadas.')
        if not os.path.exists(MSG_CAPACITACAO_APROVADO) and not os.path.exists(MSG_CAPACITACAO_REPROVADO):
            raise Exception('Não existem arquivos de mensagens de "aprovado" e "reprovado" para etapa Capacitação. Por favor, crie os arquivos necessários (capacitacao_aprovado.txt e capacitacao_reprovado.txt) e adicione as mensagens adequadas.')
        if not os.path.exists(MSG_TRAINEE_APROVADO) and not os.path.exists(MSG_TRAINEE_REPROVADO):
            raise Exception('Não existem arquivos de mensagens de "aprovado" e "reprovado" para etapa Trainee. Por favor, crie os arquivos necessários (trainee_aprovado.txt e trainee_reprovado.txt) e adicione as mensagens adequadas.')

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