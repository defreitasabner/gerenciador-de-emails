import os
from tkinter import filedialog
from dotenv import load_dotenv

from InterfaceGrafica import InterfaceGrafica
from Planilha import Planilha
from Candidatos import Candidatos
from GerenciadorCaminhos import GerenciadorCaminhos
from GerenciadorEmails import GerenciadorEmails
from GeradorMensagem import GeradorMensagem

from exceptions import ErroColunasEsperadas, ErroDiretorioDataNaoEncontrado, ErroDiretorioMensagensNaoEncontrado, ErroDiretorioPlanilhasNaoEncontrado
from constantes import COLUNAS_ESPERADAS_PLANILHA_PS, ETAPAS_PS
from caminhos import DIRETORIO_PLANILHAS

#TODO: Criar visualização das mensagens carregadas
#TODO: Inserir lógica que trave os botões caso não exista planilha, candidatos ou mensagens carregadas
class App(InterfaceGrafica):

    def __init__(self):
        """
        Classe Principal. Agrega todas as outras classes e integra suas lógicas de funcionamento com a interface gráfica.
        """

        # Herdando todas as características da InterfaceGrafica
        super().__init__()

        # Atributos referentes as demais classes
        self.planilha = None
        self.candidatos = None
        self.gerador_mensagens = GeradorMensagem()
        self.gerenciador_email = None
        self.gerenciador_caminhos = GerenciadorCaminhos()

        # Exibe a mensagem inicial do programa
        self.mensagem_inicial()
        self.verificar_diretorios()
        self.verificar_arquivos_mensagens()
        self.login_automatico()

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

    def verificar_arquivos_mensagens(self) -> None:
        try:
            self.gerenciador_caminhos.verificar_existencia_arquivos_mensagem_etapas_ps()
            self.sistema_msg_sucesso('Todos os arquivos de mensagens de resultado de PS foram encontrados.')
        except Exception as erro_inesperado:
            self.sistema_msg_erro(erro_inesperado, 'verificar existência de arquivos de mensagens de PS')

    def login_automatico(self):
        """
        Método responsável por fazer o login automaticamente caso exista um arquivo `.env` com as especificações corretas das variáveis de ambiente: `USUARIO` e `SENHA`.
        """
        try:
            # Tenta realizar o login instanciando a classe GerenciadorEmail puxando info do .env
            load_dotenv()
            self.gerenciador_email = GerenciadorEmails(str(os.getenv('USUARIO')), str(os.getenv('SENHA')))
            self.sistema_msg_sucesso('Login automático realizado com sucesso!')
            self.sistema_msg_padrao(self.gerenciador_email)
        except Exception as erro_inesperado:
            # Informa ao usuário que não foi possível realizar o login automático e pede para logar
            self.sistema_msg_erro(erro_inesperado, 'login automático')

    def carregar_planilha_ps(self) -> None:
        try:
            caminho_arquivo_csv = filedialog.askopenfilename(
                initialdir = DIRETORIO_PLANILHAS,
                title = 'Selecione a Planilha de Processo Seletivo (.csv)',
                filetypes = (('CSV Files', '*.csv'),)
            )
            self.planilha = Planilha(caminho_arquivo_csv)
            self.sistema_msg_sucesso('Planilha PS carregada com sucesso!')
            self.candidatos = Candidatos(self.planilha.dados)
            self.sistema_msg_sucesso('Dados dos Candidatos extraídos com sucesso!')
        except ErroColunasEsperadas as erro:
            self.sistema_msg_erro(erro, 'carregar Planilha de PS')
        except Exception as erro_inesperado:
            self.sistema_msg_erro(erro_inesperado, 'carregar Planilhas de PS')
    
    def salvar_dados_email(self) -> None:
        try:
            # Executa a salvar dados do email da interface gráfica
            dados_email = super().salvar_dados_email() # retorna um dicionário com email e senha digitados nos inputs
            # Verifica se os inputs não estão vazios
            if len(dados_email['email']) != 0 and len(dados_email['senha']) != 0:
                self.gerenciador_email = GerenciadorEmails(
                    email_usuario = dados_email['email'],
                    senha = dados_email['senha']
                )
                self.sistema_msg_sucesso('E-mail salvo com sucesso! Agora é possível enviar mensagens.')
            else:
                raise Exception('Faltam dados para operação! Por favor, preencha os dois inputs (email e senha).')
        except Exception as erro_inesperado:
            self.sistema_msg_erro(erro_inesperado, 'salvar dados do email')

    def carregar_mensagens_ps(self, botao_clicado: str):
        try:
            etapa_selecionada = ETAPAS_PS[botao_clicado] # Extrai o valor da etapa do PS para uso no código
            self.sistema_msg_alerta(f'Etapa de {botao_clicado} selecionada:')
            self.sistema_msg_padrao(f'Carregando mensagens para etapa {botao_clicado}...')
            self.gerador_mensagens.carregar_msg_resultado_etapa_ps(etapa_selecionada)
            self.sistema_msg_sucesso(f'Mensagens de aprovado/reprovado da etapa {botao_clicado} foram carregadas com sucesso!')
        except Exception as erro_inesperado:
            self.sistema_msg_erro(erro_inesperado, 'carregar mensagens da etapa do PS')

    def verificar_candidatos(self):
        try:
            if self.candidatos != None:
                self.sistema_msg_padrao(self.candidatos)
            else:
                self.sistema_msg_alerta('Nenhum candidato carregado ainda. Por favor, abra uma Planilha de PS para carregar os candidatos.')
        except Exception as erro_inesperado:
            self.sistema_msg_erro(erro_inesperado, 'verificar Candidatos')

    def evento_verificar_mensagens(self):
        try:
            if self.gerador_mensagens.mensagem_carregada != None:
                self.sistema_msg_alerta('Mensagem de Aprovado:')
                self.sistema_msg_padrao(self.gerador_mensagens.mensagem_carregada.msg_aprovado)
                self.sistema_msg_alerta('Mensagem de Reprovado:')
                self.sistema_msg_padrao(self.gerador_mensagens.mensagem_carregada.msg_reprovado)
            else:
                self.sistema_msg_alerta('Nenhuma mensagem foi carregada ainda. Selecione uma etapa para carregar uma mensagem.')
        except Exception as erro_inesperado:
            self.sistema_msg_erro(erro_inesperado, 'verificar mensagens')
    
    def evento_enviar_emails(self):
        try:
            self.gerenciador_email.enviar_emails_ps(self.gerador_mensagens, self.candidatos.lista_candidatos)
            self.sistema_msg_sucesso('Todos e-mails foram enviados com sucesso!')
        except Exception as erro_inesperado:
            self.sistema_msg_erro(erro_inesperado, 'enviar e-mails')

if __name__ == '__main__':
    app = App()
    app.mainloop()