from typing import List, Dict

from Feedback import Feedback
from constantes import COLUNAS_ESPERADAS_PLANILHA_180

class GerenciadorFeedbacks:

    """
    Classe responsável por gerenciar os feedbacks. Recebe dados vindos da propriedade `dados` de uma `Planilha180`. Todos os dados vindos da planilha são convertidos em objetos `Feedback` ficam armazenados na propriedade `lista_feedbacks`.
    """

    def __init__(self, dados_planilha_180: List[Dict[str,str]]) -> None:
        self.__lista_feedbacks = self.__adicionar_feedbacks(dados_planilha_180)

    def __str__(self) -> str:
        return f'Total de feedbacks: {self.lista_feedbacks}'

    def __adicionar_feedbacks(self, dados_planilha_180: List[Dict[str,str]]) -> List[Feedback]:
        """
        Método privado responsável por receber os dados vindos de uma classe `Planilha180`, instanciar objetos `Feedback` e adicioná-los à `lista_feedbacks`.
        """
        lista_feedbacks = []

        for dado in dados_planilha_180:

            feedback = Feedback(
                remetente= dado[COLUNAS_ESPERADAS_PLANILHA_180[2]],     # Quem é você?
                destinatario= dado[COLUNAS_ESPERADAS_PLANILHA_180[3]],  # Pra quem quer dar Feedback?
                mensagem= dado[COLUNAS_ESPERADAS_PLANILHA_180[4]]       # Feedback:
            )

            lista_feedbacks.append(feedback)

        return lista_feedbacks

    @property
    def lista_feedbacks(self) -> List[Feedback]:
        return self.__lista_feedbacks
