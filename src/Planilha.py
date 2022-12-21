import csv
from typing import List, Dict

from constantes import LISTA_COLUNAS_ESPERADAS

#TODO: Adicionar verificador dos campos presentes na planilha, devem ser sempre os mesmos
class Planilha:
    
    def __init__(self, caminho_csv: str) -> None:
        """
        Classe responsável por gerenciar os arquivos `.csv`. O método construtor de `Planilha` recebe um caminho (`str`) para um arquivo `.csv` e armazena as informações obtidas no atributo `dados`, na forma de uma lista de dicionários.
        """
        self.colunas_esperadas: List[str] = LISTA_COLUNAS_ESPERADAS
        self._dados: List[Dict[str, str]] = self.extrair_dados(caminho_csv)

    def extrair_dados(self, caminho_csv: str) -> List[Dict[str, str]]:

        try:

            dados = []

            with open(caminho_csv, 'r', encoding='utf-8') as planilha:
                
                dados_planilha = csv.DictReader(planilha, delimiter=',', skipinitialspace=True)
                
                for dado in dados_planilha:
                    dados.append(dado)

            self.validar_colunas(dados)

            return dados
        
        except Exception:
            
            raise Exception('Ocorreu um erro ao abrir a planilha...')
            
    @property
    def dados(self) -> List[Dict[str, str]]:
        """
        Método responsável pelo acesso aos dados do objeto `Planilha`. Retorna os dados na forma de uma lista com dicionários, no qual cada dicionário representa uma linha da planilha e as chaves são os títulos das colunas e os valores são referentes aos valores daquela linha.
        """
        return self._dados

    @dados.setter
    def dados(self, caminho_novos_dados: str) -> None:
        """
        Método responsável pela troca de dados do objeto `Planilha`. Apenas para o caso de querermos carregar novos dados vindos de outro arquivo `.csv`. Os dados antigos serão substituídos na memória.
        """
        novos_dados = self.extrair_dados(caminho_novos_dados)
        self._dados = novos_dados

    def validar_colunas(self, dados: List[Dict[str, str]]) -> None:
        """
        Método responsável por verificar se todos os dicionários extraídos estão com as chaves correspondentes as colunas esperadas do arquivo `.csv`. Vai retornar erro tanto se planilha estiver sem as colunas apropriadas, quanto se ocorreu algum erro durante a extração de algum dos dicionários.
        """
        try:

            for dado in dados:
                if(list(dado.keys()) == self.colunas_esperadas):
                    print('OK')
                else:
                    raise Exception('Erro ')
        
        except:
            raise Exception('Erro')