#TODO: Criar classes de diferentes tipos de mensagens
#TODO: tornar o programa mais genérico "MensagemResultado" (para qualquer tipo de resultado)
class MensagemPS:

    def __init__(self, etapa_msg: str, msg_aprovado: str, msg_reprovado: str) -> None:
        self.etapa_msg: str = etapa_msg
        self.msg_aprovado: str = msg_aprovado
        self.msg_reprovado: str = msg_reprovado