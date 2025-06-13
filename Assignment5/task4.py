class Payment:
    def process_payment(self, amount):
        raise NotImplementedError("Override this method")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"

# Example
cc = CreditCardPayment()
pp = PayPalPayment()
print(cc.process_payment(100))
print(pp.process_payment(150))
