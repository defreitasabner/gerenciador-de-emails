import smtplib
import email.message

from Planilha import Planilha

def main():

    planilha = Planilha('planilha_teste.csv')

    # credenciais do email da equipe
    email_minervabots = {
        'username': 'defreitasabner@gmail.com',
        'password': 'ytidnugcydqtmvdr'
    }


    # lista de emails de candidatos - talvez possa ser substituído por dados de uma planilha
    lista_de_candidatos = [
        {
            'nome_candidato': 'Abner Silveira de Freitas',
            'email_candidato': 'defreitasabner@gmail.com'
        },
        {
            'nome_candidato': 'Destinatário',
            'email_candidato': 'defreitasabner@gmail.com'
        }
    ]

    # configuração do email
    tipo_email = 'resultado_entrevista'
    assunto_email = '[PROCESSO SELETIVO] - RESULTADO ENTREVISTA'

    # Talvez tirar a imagem de um outro local seja mais prático
    def gerar_corpo_email_resultado_entrevista(nome_candidato):
        
        return f'''
        Boa dia/tarde/noite, {nome_candidato},

        De acordo com a sua disponibilidade, separamos o seguinte horário: XXhXX do dia XXXX. Por favor, responda este email confirmando a sua presença.
        Caso confirme, iremos mandar um outro email, alguns minutos antes, com a sala no meet para a reunião. Lembrando que será necessário o uso de câmera.
        Atenciosamente,
        MinervaBots.
        '''

    # Configurações para enviar o email
    msg = email.message.Message() # objeto email
    msg['Subject'] = '[PROCESSO SELETIVO] - RESULTADO ENTREVISTA' # assunto do email
    msg['From'] = email_minervabots['username'] # nosso email
    msg['To'] = None # iterar todos os candidatos na lista de candidatos
    password = email_minervabots['password'] # nossa senha de app do google - ver tutorial na Wiki
    msg.add_header('Content-Type', 'text/plain') # tipo de mensagem que será enviada

    # fazendo conexões
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()

    # Crendenciais para enviar o e-mail
    server.login(msg['From'], password)
    
    for candidato in lista_de_candidatos:
        nome_candidato = candidato['nome_candidato']
        msg.set_payload(gerar_corpo_email_resultado_entrevista(nome_candidato))
        server.sendmail(msg['From'], candidato['email_candidato'], msg.as_string().encode('utf-8'))
        print(f'Email enviado para {nome_candidato}!')

if __name__ == '__main__':
    main()