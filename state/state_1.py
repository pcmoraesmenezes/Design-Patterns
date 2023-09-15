"""
O padrão de projeto State é um padrão comportamental que tem a
intenção de permitir a um objeto alterar o seu comportamento
quando o seu estado interno muda. O objeto parecerá ter mudado
a sua classe.

O padrão State pode ser interpretado como uma máquina de estados
finitos, onde cada estado representa uma situação específica
do objeto. Transições de estado são feitas por meio de métodos
que mudam a situação do objeto.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self):
        self.state.pending()

    def approve(self):
        self.state.approve()

    def reject(self):
        self.state.reject()


class OrderState(ABC):

    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None:
        pass

    @abstractmethod
    def approve(self) -> None:
        pass

    @abstractmethod
    def reject(self) -> None:
        pass

    def __str__(self) -> str:
        return self.__class__.__name__


class PaymentPending(OrderState):

    def __init__(self, order: Order):
        self.order = order

    def pending(self) -> None:
        print('O pedido já está em estado de pagamento pendente.\n')

    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print('Pagamento aprovado.\n')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento rejeitado.\n')


class PaymentApproved(OrderState):

    def __init__(self, order: Order):
        self.order = order

    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('Pagamento pendente.\n')

    def approve(self) -> None:
        print('O pedido já está em estado de pagamento aprovado.\n')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento rejeitado.\n')


class PaymentRejected(OrderState):

    def __init__(self, order: Order):
        self.order = order

    def pending(self) -> None:
        print('Pagamento Recusado.\n')

    def approve(self) -> None:
        print('Pagamento Recusado.\n')

    def reject(self) -> None:
        print('O pedido já está em estado de pagamento rejeitado.\n')


if __name__ == "__main__":
    order = Order()
    order.pending()
    order.approve()
    order.reject()
    order.reject()
    order.pending()
    order.approve()
    order.reject()
