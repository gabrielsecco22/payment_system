import string
import random
from abc import ABC, abstractmethod


class Authorizer(ABC):

    @abstractmethod
    def authorize(self):
        pass

    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class Authorizer_SMS(Authorizer):

    def __init__(self):
        self.authorized = False
        self.code = None

    def generate_sms_code(self):
        self.code = "".join(random.choices(string.digits, k=6))

    def authorize(self):
        code = input("Enter SMS code: ")
        self.authorized = code == self.code

    def is_authorized(self) -> bool:
        return self.authorized


class Authorizer_Robot(Authorizer):

    def __init__(self):
        self.authorized = False
        self.code = None

    def authorize(self):
        robot = ""
        while robot != "y" and robot != "n":
            robot = input("Are you a robot(y/n)? ").lower()
        self.authorized = robot == "n"

    def is_authorized(self) -> bool:
        return self.authorized
