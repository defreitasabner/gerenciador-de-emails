import os
import config

#TODO: tornar o gerador de mensagem um classe normal, com método construtor recebendo diretório
#TODO: Criar um método para verficar quais mensagens estão presentes no diretório mensagem
class GeradorMensagem:

    @staticmethod
    def gerar_mensagem_ps(etapa_ps: str, candidato: str) -> str:
        
        arquivo = None
        nome_candidato = candidato['nome']

        if etapa_ps == 'formulario':
            if candidato[etapa_ps] == 'aprovado':
                arquivo = config.MSG_FORMULARIO_APROVADO
            elif candidato[etapa_ps] == 'reprovado':
                arquivo = config.MSG_FORMULARIO_REPROVADO
        else:
            raise Exception(f'O candidato {nome_candidato} ainda não foi avaliado nessa etapa!')

        caminho = os.path.join(config.DIRETORIO_DATA, config.DIRETORIO_MSG, arquivo)

        mensagem = ''
        
        with open(caminho, 'r', encoding='utf-8') as arquivo_txt:
            
            for linha in arquivo_txt:
                mensagem += linha

        mensagem_tratada = mensagem.replace('$candidato', nome_candidato)

        return mensagem_tratada