import os
import config

class GeradorMensagem:

    @staticmethod
    def gerar_mensagem(etapa_mensagem: str, status_candidato: str, nome_candidato: str) -> str:
        
        arquivo = os.path.join(config.DIRETORIO_MSG)

        if status_candidato == 'aprovado':
            if etapa_mensagem == 'formulario':
                arquivo = config.MSG_FORMULARIO_APROVADO
        elif status_candidato == 'reprovado':
            if etapa_mensagem == 'formulario':
                arquivo = config.MSG_FORMULARIO_REPROVADO
        else:
            raise Exception(f'O candidato {nome_candidato} ainda não foi avaliado nessa etapa!')

        caminho = os.path.join(config.DIRETORIO_MSG, arquivo)

        with open(caminho, 'r', encoding='utf-8') as arquivo_txt:
            
            mensagem = ''

            for linha in arquivo_txt:
                mensagem += linha

            mensagem_tratada = mensagem.replace('$candidato', nome_candidato)

            return mensagem_tratada