from typing import Dict, Union
import os

from caminhos import DIRETORIO_MSG
from MensagemPS import MensagemPS
from Candidato import Candidato

#TODO: Informar qual mensagem está com problema no método __validar_mensagem
#TODO: criar validação de entrada do parâmetro etapa_ps com as colunas
class GeradorMensagem:

    def __init__(self) -> None:
        self.__mensagem_carregada: Union[MensagemPS, None] = None


    def __carregar_mensagem(self, caminho: str) -> str:
        """
        Método privado (Não deve ser chamado diretamente)
        --- 
        Responsável por extrair o conteúdo de uma única mensagem. É chamado dentro do método `carregar_mensagens_ps()`.
        """

        msg = ''

        with open(caminho, 'r', encoding='utf-8') as arquivo_txt:
                
            for linha in arquivo_txt:
                msg += linha
        
        self.__validar_conteudo_msg_resultado_etapa_ps(msg)
        
        return msg

    def __validar_conteudo_msg_resultado_etapa_ps(self, mensagem: str) -> None:
        """
        Método privado chamado no momento de carregar uma mensagem de resultado de PS. Esse método verifica se o conteúdo da mensagem está vazio, caso esteja, retorna uma exceção. Também verifica se a expressão `$candidato` está presente na mensagem para substituição do nome do candidato, caso não esteja, retorna uma exceção.
        """
        if len(mensagem) == 0:
            raise Exception('O arquivo de mensagem foi encontrado, mas seu conteúdo está vazio. Por favor, adicione algum conteúdo no arquivo.')
        if '$candidato' not in mensagem:
            raise Exception('Não foi possível encontrar o template "$candidato" na mensagem. Por favor, adicione essa expressão no local adequado para que o nome do candidato possa ser incluído na mensagem.')

    def carregar_msg_resultado_etapa_ps(self, etapa_ps: str) -> None:
        """
        Método responsável por receber uma `etapa` do processo seletivo e carregar as mensagens de `aprovado` e `reprovaado` referentes àquela etapa. A mensagem carregada é guardada dentro do atributo privado `mensagem_carregada` da classe `GeradorMensagem`.
        """
        
        caminho_msg_aprovado = os.path.join(DIRETORIO_MSG, f'{etapa_ps}_aprovado.txt')
        caminho_msg_reprovado = os.path.join(DIRETORIO_MSG, f'{etapa_ps}_reprovado.txt')

        msg_aprovado = self.__carregar_mensagem(caminho_msg_aprovado)
        msg_reprovado = self.__carregar_mensagem(caminho_msg_reprovado)

        self.mensagem_carregada = MensagemPS(etapa_ps, msg_aprovado, msg_reprovado)

    def gerar_msg_resultado_etapa_ps(self, candidato: Candidato) -> str:

        if self.mensagem_carregada == None:
            raise Exception('Nenhuma mensagem foi carregada. Por favor, utilize o método carregar mensagem.')
        
        # Extraindo o primeiro nome do candidato para adicionar à mensagem
        primeiro_nome_candidato = candidato.nome.split(sep=" ")[0]

        # Mensagem resultada iniciada vazia para receber a mensagem tratada
        mensagem_resultado = ''

        # Verifica se o Objeto candidato tem o valor aprovado ou reprovado na etapa da mensagem que está sendo gerada

        if getattr(candidato, self.mensagem_carregada.etapa_msg) == 'aprovado':
            mensagem_tratada = self.mensagem_carregada.msg_aprovado.replace('$candidato', primeiro_nome_candidato)
            mensagem_resultado = mensagem_tratada

        elif getattr(candidato, self.mensagem_carregada.etapa_msg) == 'reprovado':
            mensagem_tratada = self.mensagem_carregada.msg_reprovado.replace('$candidato', primeiro_nome_candidato)
            mensagem_resultado = mensagem_tratada

        else:
            Exception(f'O Candidato {candidato.nome} ainda não foi avaliado na etapa de {self.mensagem_carregada.etapa_msg}')

        return mensagem_resultado


    @property
    def mensagem_carregada(self) -> Union[MensagemPS, None]:
        return self.__mensagem_carregada

    @mensagem_carregada.setter
    def mensagem_carregada(self, nova_mensagem: MensagemPS) -> None:
        self.__mensagem_carregada = nova_mensagem