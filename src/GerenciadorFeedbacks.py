import os
from typing import List, Dict

from Feedback import Feedback
from constantes import COLUNAS_ESPERADAS_PLANILHA_180
from caminhos import DIRETORIO_FEEDBACKS

class GerenciadorFeedbacks:

    """
    Classe responsável por gerenciar os feedbacks. Recebe dados vindos da propriedade `dados` de uma `Planilha180`. Todos os dados vindos da planilha são convertidos em objetos `Feedback` ficam armazenados na propriedade `lista_feedbacks`.
    """

    def __init__(self, dados_planilha_180: List[Dict[str,str]]) -> None:
        self.__lista_destinatarios: List[str] = []
        self.__lista_feedbacks: List[Feedback] = self.__adicionar_feedbacks(dados_planilha_180)

    def __str__(self) -> str:
        return f'Total de feedbacks: {self.lista_feedbacks}'

    def __adicionar_feedbacks(self, dados_planilha_180: List[Dict[str,str]]) -> List[Feedback]:
        """
        Método privado responsável por receber os dados vindos de uma classe `Planilha180`, instanciar objetos `Feedback` e adicioná-los à `lista_feedbacks`.
        """
        lista_feedbacks = []

        for dado in dados_planilha_180:

            # Extraindo os dados da planilha para variáveis para ficar semântico
            remetente = dado[COLUNAS_ESPERADAS_PLANILHA_180[2]]
            destinario = dado[COLUNAS_ESPERADAS_PLANILHA_180[3]]
            mensagem = dado[COLUNAS_ESPERADAS_PLANILHA_180[4]]

            # Instanciando um objeto Feedback para representar a info do feedback
            feedback = Feedback(
                remetente= remetente,       # Quem é você?
                destinatario= destinario,   # Pra quem quer dar Feedback?
                mensagem= mensagem          # Feedback:
            )

            # Adiciona o objeto a lista de feedbacks
            lista_feedbacks.append(feedback)

            # Caso o destinatário ainda não esteja na lista, adiciona ele à lista
            if destinario not in self.lista_destinatarios: 
                self.lista_destinatarios.append(destinario)

        # Retorna a lista de feedback
        return lista_feedbacks

    def extrair_feedbacks_por_pessoa(self) -> None:
        """
        Método responsável por extrair os feedbacks de uma pessoa e adicionar à arquivos `.txt` para serem posteriormente enviados como emails.
        """
        for destinario in self.lista_destinatarios:
            # Caminho para o arquivo onde serão salvos os feedbacks
            caminho_arquivo = os.path.join(DIRETORIO_FEEDBACKS, f'{destinario}_feedback.txt')
            # Abre o arquivo em modo de escrita e escreve todos os feedbacks
            with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo_feedback:
                # Passa por toda lista de feedback
                for feedback in self.lista_feedbacks:
                    # Caso o feedback seja para o destinatário da vez
                    if feedback.destinatario == destinario:
                        remetente_feedback = feedback.remetente # Extrai o remetente
                        mensagem_feedback = feedback.mensagem   # Extrai a mensagem
                        # Escreve o remetente, pula linha, escreve a mensagem e pula linha
                        arquivo_feedback.write(f'{remetente_feedback}:\n{mensagem_feedback}\n---\n')
                        
    @property
    def lista_feedbacks(self) -> List[Feedback]:
        return self.__lista_feedbacks

    @property
    def lista_destinatarios(self) -> List[str]:
        return self.__lista_destinatarios
