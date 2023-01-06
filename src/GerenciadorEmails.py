from typing import List
import email.message
import smtplib

from Candidato import Candidato
from GeradorMensagem import GeradorMensagem

#TODO: REFATORAR ENVIAR EMAIL PARA QUE ELA RETORNE UM FEEDBACK PARA O USUÁRIO PARA CADA EMAIL ENVIADO
#TODO: Implementar __str__ e __repr__ para essa classe ficar apresentável no terminal
#TODO: Melhorar validação do campo email
#TODO: Implementar validação do campo senha
#TODO: Adicionar validação de mensagens que serão enviadas
class GerenciadorEmails:

    def __init__(self, email_usuario: str, senha: str) -> None:
        self.__email_usuario = self.__validar_email(email_usuario)
        self.__senha = self.__validar_senha(senha)

    def __str__(self) -> str:
        return f'E-mail configurado: {self.email_usuario}'

    def verifica_se_todos_foram_avaliados(self, etapa_ps: str, lista_candidatos: List[Candidato]):
        """
        Método responsável por verificar se todos os candidatos possuem valores de `aprovado` ou `reprovado` para a etapa do PS selecionada. Caso alguma candidato possua um valor diferente do esperado, retorna um erro e não executa o procedimento.
        """        
        for candidato in lista_candidatos:
            if getattr(candidato, etapa_ps) == 'aprovado':
                pass
            elif getattr(candidato, etapa_ps) == 'reprovado':
                pass
            else:
                raise Exception(f'O Candidato {candidato.id} ainda não foi avaliado como aprovado/reprovado.')

    def verificar_se_todos_emails_sao_validos(self, lista_candidatos: List[Candidato]):
        """
        Método verifica se todos os emails dos candidatos são válidos antes de começar a enviar os emails.
        """
        for candidato in lista_candidatos:
            self.__validar_email(candidato.email)

    #TODO: Criar um método que mande uma mensagem por vez para retornar feedback para o usuário
    def enviar_email_ps(self, gerador_mensagem: GeradorMensagem, candidato: Candidato):
        pass

    def enviar_emails_ps(self, gerador_mensagem: GeradorMensagem, lista_candidatos: List[Candidato]) -> None:

        # Verifica se existe alguma mensagem carregada
        if gerador_mensagem.mensagem_carregada == None:
            raise Exception('Nenhuma mensagem foi carregada até o momento.')

        # Verifica se existe uma lista de candidatos
        if lista_candidatos == None:
            raise Exception('Não existe uma lista de candidatos carregada.')
        
        # Extrai a etapa da mensagem que será enviada
        etapa_ps = gerador_mensagem.mensagem_carregada.etapa_msg

        # Verifica se todos os candidatos já foram avaliados na etapa selecionada
        self.verifica_se_todos_foram_avaliados(etapa_ps, lista_candidatos)
        

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
            objeto_email.set_payload(gerador_mensagem.gerar_msg_resultado_etapa_ps(candidato))
            server.sendmail(objeto_email['From'], candidato.email, objeto_email.as_string().encode('utf-8'))
            print('Email enviado para' + candidato.nome)

    # Melhorar essa validação usando regex
    def __validar_email(self, email: str) -> str:

        if (email != None) and ('@' in email):
            return email
        else:
            raise Exception('E-mail inválido')

    def __validar_senha(self, senha: str) -> str:

        if (senha != None) and senha != '':
            return senha
        else:
            raise Exception('Senha nula é inválida')

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
        self.__email_usuario = self.__validar_email(novo_email)

    @property
    def senha(self) -> str:
        return self.__senha

    @senha.setter
    def senha(self, nova_senha) -> None:
        self.__senha = nova_senha