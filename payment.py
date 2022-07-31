from authorizer import Authorizer


class PaymentProcessor:

    def __init__(self, authorizer: Authorizer):
        self.authorizer = authorizer

    def pay(self, order):
        self.authorizer.authorize()
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print(f"Processing payment for order with id {order.id}")
        order.set_status("paid")