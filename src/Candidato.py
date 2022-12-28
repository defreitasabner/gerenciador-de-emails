from typing import Union

class Candidato:

    def __init__(self,
    id: str,
    nome: str, 
    email: str, 
    formulario: Union[str, None],
    dinamica: Union[str, None],
    entrevista: Union[str, None],
    capacitacao: Union[str, None],
    trainee: Union[str, None]
    ) -> None:

        """
        Classe responsável por representar cada um dos candidatos do processo seletivo. Os primeiros atributos representam informações dos candidatos (`id`, `nome` e `email`) e os demais representam o status do candidato em cada etapa (`formulario`, `dinamica`, `entrevista`, `capacitacao` e `trainee`). Caso o candidato ainda não tenha sido avaliado na etapa, espera-se receber `None`. Caso ele tenha sido avaliado, espera-se uma string com valor `aprovado` ou `reprovado`.
        """

        self.__id: str = id
        self.__nome: str = nome
        self.__email: str = email
        self.__formulario: Union[str, None] = formulario
        self.__dinamica: Union[str, None] = dinamica
        self.__entrevista: Union[str, None] = entrevista
        self.__capacitacao: Union[str, None] = capacitacao
        self.__trainee: Union[str, None] = trainee

    def __str__(self) -> str:
        """
        Método especial de classes Python. Retorna uma `str` que representa a classe quando usamos a função `str()` ou `print()` (diretamente).
        """
        return f'Candidato {self.id}: {self.nome} => form: {self.formulario}| din: {self.dinamica}| ent: {self.entrevista} | cap: {self.capacitacao}| tra: {self.trainee};'

    def __repr__(self) -> str:
        """
        Método especial de classes Python. Retorna uma `str` que representa a classe em termos de atributos e seus valores quando usamos a função `repr()` ou `print()` (com ela dentro de uma `list`).
        """
        return f'Candidato(id= {self.id}, nome= {self.nome}, email= {self.email})'
    
    """
    Métodos Getters e Setters
    ===
    Os métodos abaixo servem apenas para acessarmos (getters) e alterarmos (setters) os valores dos atributos privados da classe.
    """

    @property
    def id(self) -> str:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def email(self) -> str:
        return self.__email

    @property
    def formulario(self) -> Union[str, None]:
        return self.__formulario

    @property
    def dinamica(self) -> Union[str, None]:
        return self.__dinamica

    @property
    def entrevista(self) -> Union[str, None]:
        return self.__entrevista

    @property
    def capacitacao(self) -> Union[str, None]:
        return self.__capacitacao

    @property
    def trainee(self) -> Union[str, None]:
        return self.__trainee