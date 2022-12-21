import os
from dotenv import load_dotenv

from Planilha import Planilha
from GerenciadorEmails import GerenciadorEmails

def main():

    load_dotenv()

    # informações
    caminho_csv = 'data/planilhas/planilha_teste.csv'
    etapa_ps = 'formulario'

    # Classes que fazem as coisas
    planilha = Planilha(caminho_csv)
    gerenciador_emails = GerenciadorEmails(os.getenv('USUARIO'), os.getenv('SENHA'))
    
    # envia os emails
    gerenciador_emails.enviar_emails(etapa_ps, planilha.dados)



if __name__ == '__main__':
    main()