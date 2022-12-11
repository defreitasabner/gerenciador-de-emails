import csv
from typing import List, Dict

class Planilha:
    
    def __init__(self, caminho_csv: str) -> None:
        self.dados: List[Dict[str, str]] = self.extrair_dados(caminho_csv)

    def extrair_dados(caminho_csv: str) -> List[Dict[str, str]]:

        try:

            dados = []

            with open(caminho_csv, 'r', encoding='utf-8') as planilha:
                
                dados_planilha = csv.DictReader(planilha)
                
                for dado in dados_planilha:
                    dados.append(dado)

            return dados
        
        except Exception:
            
            raise Exception('Ocorreu um erro ao abrir a planilha...')
