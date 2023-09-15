"""
Chain of Responsability (COR)  é um padrão comportamental que tem
a intensão de evitar o acoplamento do remetente de uma solicitação
ao seu receptor, ao dar a mais de um objeto a oportunidade de tratar
essa solicitação. Encadear os objetos receptores, passando a solicitação
ao longo da cadeia até que um objeto a trate.

O padrão COR desacopla o remetente de um pedido do seu receptor, dando a
esta chance de tratar o pedido ou passá-lo para o próximo receptor da cadeia.
Uma cadeia pode ser montada em tempo de execução ou pode ser construída
em um código fixo.

O padrão COR é projetado para evitar acoplamento no remetente de uma
solicitação com seu receptor, dando a mais de um objeto a oportunidade
de tratar a solicitação.
Encadear os objetos receptores, passando a solicitação ao longo da cadeia até
que um objeto a trate.
"""


def Handler_ABC(letter: str) -> str:
    letters = ['A', 'B', 'C']
    if letter in letters:
        return f'Handler_ABC: conseguiu tratar {letter}\n'
    return handler_DEF(letter)


def handler_DEF(letter: str) -> str:
    letters = ['D', 'E', 'F']
    if letter in letters:
        return f'handler_DEF: conseguiu tratar {letter}\n'
    return handler_unsolved(letter)


def handler_unsolved(letter: str) -> str:
    return f'handler_unsolved: não conseguiu tratar {letter}\n'


if __name__ == "__main__":
    print(Handler_ABC('A'))
    print(Handler_ABC('B'))
    print(Handler_ABC('C'))
    print(Handler_ABC('D'))
    print(Handler_ABC('E'))
    print(Handler_ABC('F'))
    print(Handler_ABC('G'))
    print(Handler_ABC('H'))
    print(Handler_ABC('I'))
    print(Handler_ABC('J'))
    print(Handler_ABC('K'))
    print(Handler_ABC('L'))
    print(Handler_ABC('M'))
    print(Handler_ABC('N'))
    print(Handler_ABC('O'))
    print(Handler_ABC('P'))
    print(Handler_ABC('Q'))
    print(Handler_ABC('R'))
    print(Handler_ABC('S'))
    print(Handler_ABC('T'))
    print(Handler_ABC('U'))
    print(Handler_ABC('V'))
    print(Handler_ABC('W'))
    print(Handler_ABC('X'))
    print(Handler_ABC('Y'))
    print(Handler_ABC('Z'))
