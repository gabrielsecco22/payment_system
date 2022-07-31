import random
import string

class Order:

    def __init__(self):
        self.id = "".join(random.choices(string.ascii_lowercase, k=6))
        self.status = "open"

    def set_status(self, status):
        self.status = status
