from typing import List, Dict
import email.message
import smtplib

from GeradorMensagem import GeradorMensagem

#TODO: Adicionar validação de mensagens que serão enviadas
class GerenciadorEmails:

    def __init__(self, email_usuario: str, senha: str) -> None:
        self.__email_usuario = email_usuario
        self.__senha = senha


    def enviar_emails_ps(self, etapa_ps: str, lista_candidatos: List[Dict[str, str]]) -> None:

        # Gerador de mensagem preparando as mensagens
        gerador_mensagem = GeradorMensagem()
        gerador_mensagem.carregar_msg_resultado_etapa_ps(etapa_ps)

        # Configurações para enviar o email
        objeto_email = email.message.Message() # objeto email
        objeto_email['Subject'] = f'[PROCESSO SELETIVO] - RESULTADO {etapa_ps.upper()}' # assunto do email
        objeto_email['From'] = self.email_usuario # nosso email
        objeto_email['To'] = None # iterar todos os candidatos na lista de candidatos
        password = self.senha # nossa senha de app do google - ver tutorial na Wiki
        objeto_email.add_header('Content-Type', 'text/plain') # tipo de mensagem que será enviada

        # fazendo conexões
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()

        # Crendenciais para enviar o e-mail
        server.login(objeto_email['From'], password)
        
        for candidato in lista_candidatos:
            objeto_email.set_payload(gerador_mensagem.gerar_mensagem_ps(etapa_ps, candidato))
            server.sendmail(objeto_email['From'], candidato['email'], objeto_email.as_string().encode('utf-8'))
            print('Email enviado para' + candidato['nome'])

    """
    Métodos Getters e Setters
    ===
    Os métodos abaixo servem apenas para acessarmos (getters) e alterarmos (setters) os valores dos atributos privados da classe.
    """

    @property
    def email_usuario(self) -> str:
        return self.__email_usuario

    @email_usuario.setter
    def email_usuario(self, novo_email) -> None:
        self.__email_usuario = novo_email

    @property
    def senha(self) -> str:
        return self.__senha

    @senha.setter
    def senha(self, nova_senha) -> None:
        self.__senha = nova_senha