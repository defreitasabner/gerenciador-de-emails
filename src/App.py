from tkinter import filedialog

from InterfaceGrafica import InterfaceGrafica
from Planilha import Planilha
from GerenciadorCaminhos import GerenciadorCaminhos

from exception import ErroColunasEsperadas, ErroDiretorioDataNaoEncontrado, ErroDiretorioMensagensNaoEncontrado, ErroDiretorioPlanilhasNaoEncontrado
from constantes import COLUNAS_ESPERADAS_PLANILHA_PS

class App(InterfaceGrafica):

    def __init__(self):
        """
        Classe Principal. Agrega todas as outras classes e integra suas lógicas de funcionamento com a interface gráfica.
        """

        # Herdando todas as características da InterfaceGrafica
        super().__init__()

        # Atributos referentes as demais classes
        self.planilha = None
        self.gerenciador_mensagem = None
        self.gerenciador_email = None
        self.gerenciador_caminhos = GerenciadorCaminhos()

        # Exibe a mensagem inicial do programa
        self.mensagem_inicial()
        self.verificar_diretorios()

    def mensagem_inicial(self) -> None:
        self.sistema_msg_padrao('Bem-vindo(a) ao Gerenciador de E-mails!')
        self.sistema_msg_padrao('Para Começar, execute os seguintes passos:')
        self.sistema_msg_padrao('1 - Verifique se o e-mail está configurado (e-mail e senha)')
        self.sistema_msg_padrao('2 - Carregue uma Planilha Padronizada')
        self.sistema_msg_padrao('====================================================================')
        self.sistema_msg_alerta('Planilha de PS (colunas obrigatórias):')
        for coluna in COLUNAS_ESPERADAS_PLANILHA_PS:
            if COLUNAS_ESPERADAS_PLANILHA_PS.index(coluna) != len(COLUNAS_ESPERADAS_PLANILHA_PS) - 1:
                self.sistema_msg_padrao(f'{coluna} | ', pula_linha= False)
            else:
                self.sistema_msg_padrao(f'{coluna}')
        self.sistema_msg_alerta('Obs. 1: Utilize apenas "aprovado" ou "reprovado" para indicar a situação do candidato.')
        self.sistema_msg_alerta('Obs. 2: Células de etapas ou candidatos não-avaliados devem permanecer vazias.')
        self.sistema_msg_padrao('====================================================================')

    def verificar_diretorios(self) -> None:
        try:
            self.gerenciador_caminhos.verificar_diretorios()
            self.sistema_msg_sucesso('Todos os diretórios necessários foram encontrados.')
        except ErroDiretorioDataNaoEncontrado or ErroDiretorioPlanilhasNaoEncontrado or ErroDiretorioMensagensNaoEncontrado as erro:
            self.sistema_msg_erro(erro, 'verificar existência de diretórios')

    def carregar_planilha_ps(self) -> None:
        try:
            caminho_arquivo_csv = filedialog.askopenfilename(
                initialdir = './data/planilhas/',
                title = 'Selecione a Planilha de Processo Seletivo (.csv)',
                filetypes = (('CSV Files', '*.csv'),)
            )
            self.planilha = Planilha(caminho_arquivo_csv)
            self.sistema_msg_sucesso('Planilha PS carregada com sucesso!')
        except ErroColunasEsperadas as erro:
            self.sistema_msg_erro(erro, 'carregar Planilha de PS')
        except Exception as erro_inesperado:
            self.sistema_msg_erro(erro_inesperado, 'carregar Planilhas de PS')


if __name__ == '__main__':
    app = App()
    app.mainloop()