from typing import List, Dict, Type, Union
import os

from config import DIRETORIO_DATA, DIRETORIO_MSG
from MensagemPS import MensagemPS
from GerenciadorCaminhos import GerenciadorCaminhos

#TODO: tornar o gerador de mensagem um classe normal, com método construtor recebendo diretório
#TODO: Criar um método para verficar quais mensagens estão presentes no diretório mensagem
class GeradorMensagem:

    def __init__(self) -> None:
        self.__mensagem_carregada: Union[MensagemPS, None] = None


    def carregar_mensagem(self, caminho: str) -> str:

        msg = ''

        with open(caminho, 'r', encoding='utf-8') as arquivo_txt:
                
            for linha in arquivo_txt:
                msg += linha

        return msg

    def carregar_mensagens_ps(self, etapa_ps: str) -> None:
        
        caminho_msg_aprovado = os.path.join(DIRETORIO_DATA, DIRETORIO_MSG, f'{etapa_ps}_aprovado.txt')
        caminho_msg_reprovado = os.path.join(DIRETORIO_DATA, DIRETORIO_MSG, f'{etapa_ps}_reprovado.txt')

        msg_aprovado = self.carregar_mensagem(caminho_msg_aprovado)
        msg_reprovado = self.carregar_mensagem(caminho_msg_reprovado)

        self.mensagem_carregada = MensagemPS(msg_aprovado, msg_reprovado)

    def gerar_mensagem_ps(self, etapa_ps: str, candidato: Dict[str, str]) -> str:

        if self.mensagem_carregada == None:
            raise Exception('Nenhuma mensagem foi carregada. Por favor, utilize o método carregar mensagem.')
        else:
            mensagem_resultado = ''

        nome_candidato = candidato['nome']

        if candidato[etapa_ps] == 'aprovado':
            mensagem_tratada = self.mensagem_carregada.msg_aprovado.replace('$candidato', nome_candidato)
            mensagem_resultado = mensagem_tratada

        elif candidato[etapa_ps] == 'reprovado':
            mensagem_tratada = self.mensagem_carregada.msg_reprovado.replace('$candidato', nome_candidato)
            mensagem_resultado = mensagem_tratada

        else:
            Exception('Candidato ainda não foi avaliado nessa etapa')

        return mensagem_resultado


    @property
    def mensagem_carregada(self) -> Union[MensagemPS, None]:
        return self.__mensagem_carregada

    @mensagem_carregada.setter
    def mensagem_carregada(self, nova_mensagem: MensagemPS) -> None:
        self.__mensagem_carregada = nova_mensagem