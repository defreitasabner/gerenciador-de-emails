from typing import List, Dict
import email
import smtplib

from GeradorMensagem import GeradorMensagem


class GerenciadorEmails:

    def __init__(self, usuario: str, senha: str) -> None:
        self.usuario = usuario
        self.senha = senha


    def enviar_emails(self, etapa_ps: str, lista_candidatos: List[Dict[str, str]]) -> None:

        # Configurações para enviar o email
        objeto_email = email.message.Message() # objeto email
        objeto_email['Subject'] = f'[PROCESSO SELETIVO] - RESULTADO {etapa_ps.capitalize()}' # assunto do email
        objeto_email['From'] = self.usuario # nosso email
        objeto_email['To'] = None # iterar todos os candidatos na lista de candidatos
        password = self.senha # nossa senha de app do google - ver tutorial na Wiki
        objeto_email.add_header('Content-Type', 'text/plain') # tipo de mensagem que será enviada

        # fazendo conexões
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()

        # Crendenciais para enviar o e-mail
        server.login(objeto_email['From'], password)
        
        for candidato in lista_candidatos:
            objeto_email.set_payload(GeradorMensagem.gerar_mensagem_ps(etapa_ps, candidato))
            server.sendmail(objeto_email['From'], candidato['email'], objeto_email.as_string().encode('utf-8'))
            print('Email enviado para' + candidato['nome'])