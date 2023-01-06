import os
from dotenv import load_dotenv

from PlanilhaPS import PlanilhaPS
from GerenciadorEmails import GerenciadorEmails

def main():

    load_dotenv()

    # informações
    caminho_csv = 'data/planilhas/planilha_teste.csv'
    etapa_ps = 'formulario'

    # Classes que fazem as coisas
    planilha = PlanilhaPS(caminho_csv)
    gerenciador_emails = GerenciadorEmails(os.getenv('USUARIO'), os.getenv('SENHA'))
    
    # envia os emails
    gerenciador_emails.enviar_emails_ps(etapa_ps, planilha.dados)



if __name__ == '__main__':
    main()