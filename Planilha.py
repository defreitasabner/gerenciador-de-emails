import csv
from typing import List, Dict

class Planilha:
    
    def __init__(self, caminho_csv: str) -> None:
        self._dados: List[Dict[str, str]] = self.extrair_dados(caminho_csv)

    def extrair_dados(self, caminho_csv: str) -> List[Dict[str, str]]:

        try:

            dados = []

            with open(caminho_csv, 'r', encoding='utf-8') as planilha:
                
                dados_planilha = csv.DictReader(planilha, delimiter=',', skipinitialspace=True)
                
                for dado in dados_planilha:
                    dados.append(dado)

            return dados
        
        except Exception:
            
            raise Exception('Ocorreu um erro ao abrir a planilha...')
            
    @property
    def dados(self) -> List[Dict[str, str]]:
        return self._dados

    @dados.setter
    def dados(self, caminho_novos_dados: str) -> None:
        novos_dados = self.extrair_dados(caminho_novos_dados)
        self._dados = novos_dados