class Feedback:

    """
    Classe responsável por armazenar as informações importantes que compõem um feedback de 180: `remetente` (quem enviou o feedback), `destinatario` (para quem foi o feedback) e `mensagem` (qual foi a mensagem enviada no feedback).
    """

    def __init__(self, remetente: str, destinatario: str, mensagem: str) -> None:
        self.remetente: str = remetente
        self.destinatario: str = destinatario
        self.mensagem: str = mensagem

    def __str__(self) -> str:
        return f'de {self.remetente} para {self.destinatario} : {self.mensagem[:16]}...'

    def __repr__(self) -> str:
        return f'(remetente: {self.remetente}, destinatario: {self.destinatario}, mensagem: {self.mensagem})'