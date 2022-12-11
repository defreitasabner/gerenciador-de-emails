class GeradorMensagem:

    @staticmethod
    def gerar_mensagem(etapa_mensagem: str, status_candidato: str, nome_candidato: str) -> str:
        
        arquivo = None

        if status_candidato == 'aprovado':
            if etapa_mensagem == 'formulario':
                arquivo = 'formulario_aprovado.txt'
        elif status_candidato == 'reprovado':
            if etapa_mensagem == 'formulario':
                arquivo = 'formulario_reprovado.txt'
        else:
            raise Exception('Existem candidatos que não se enquadram como aprovados ou reprovados nessa etapa!')

        with open(f'mensagens/{arquivo}', 'r', encoding='utf-8') as arquivo_txt:
            
            mensagem = ''

            for linha in arquivo_txt:
                mensagem += linha

            mensagem_tratada = mensagem.replace('$candidato', nome_candidato)

            return mensagem_tratada