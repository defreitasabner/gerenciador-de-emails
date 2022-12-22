import csv
from typing import List, Dict, Union

from constantes import COLUNAS_ESPERADAS_PLANILHA_PS
from exception import ErroColunasEsperadas

#TODO: Adicionar Null Safety nos métodos (principalmente os getters e setters)
#TODO: Resolver o problema com nome com acentuação, pois isso gera problema no futuro
#TODO: Fazer validação de novas colunas
class Planilha:
    
    def __init__(self, caminho_csv: str) -> None:
        """
        Classe responsável por gerenciar os arquivos `.csv`. O método construtor de `Planilha` recebe um caminho (`str`) para um arquivo `.csv` e armazena as informações obtidas no atributo `dados`, na forma de uma lista de dicionários.
        """
        self.__colunas_esperadas: List[str] = COLUNAS_ESPERADAS_PLANILHA_PS
        self.__dados: Union[ List[Dict[str, str]], None ] = self.extrair_dados(caminho_csv)

    def extrair_dados(self, caminho_csv: str) -> Union[ List[Dict[str, str]], None ]:

        try:

            dados = []

            with open(caminho_csv, 'r', encoding='utf-8') as planilha:
                
                dados_planilha = csv.DictReader(planilha, delimiter=',', skipinitialspace=True)
                
                for dado in dados_planilha:
                    dados.append(dado)

            self.validar_colunas(dados)

            return dados
        
        except ErroColunasEsperadas as erro:
            # Caso o erro seja do tipo ErroColunasEsperadas, printa uma mensagem com nome do erro
            print(f'{erro.__class__.__name__}: As colunas do arquivo ".csv" não correspondem as colunas esperadas para esse tipo de Planilha (PS).')
        
    def validar_colunas(self, dados: List[Dict[str, str]]) -> None:
        """
        Método responsável por verificar se todos os dicionários extraídos estão com as chaves correspondentes as colunas esperadas do arquivo `.csv`. Vai retornar erro tanto se planilha estiver sem as colunas apropriadas, quanto se ocorreu algum erro durante a extração de algum dos dicionários.
        """
        for dado in dados:
            if(list(dado.keys()) == self.colunas_esperadas):
                print('OK')
            else:
                raise ErroColunasEsperadas()

    """
    Métodos Getters e Setters
    ===
    Os métodos abaixo servem apenas para acessarmos (getters) e alterarmos (setters) os valores dos atributos privados da classe.
    """

    @property
    def dados(self) -> Union[ List[Dict[str, str]], None ]:
        return self.__dados

    @dados.setter
    def dados(self, caminho_novos_dados: str) -> None:
        self.__dados = self.extrair_dados(caminho_novos_dados)

    @property
    def colunas_esperadas(self) -> List[str]:
        return self.__colunas_esperadas

    @colunas_esperadas.setter
    def colunas_esperadas(self, novas_colunas_esperadas) -> None:
        self.__colunas_esperadas = novas_colunas_esperadas