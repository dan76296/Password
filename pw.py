import random
import sys


@staticmethod
def random_type(choices):
    return random.choice(choices)


class Reader(object):

    @staticmethod
    def read(filename):
        with open(filename, 'r', ) as f:
            return f.read()


class Password:

    def __init__(self):
        self.special_chars = "! @ £ $ % ^ & * ( ) _ - + = / > < [ ] { }".split(' ')
        self.alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(' ')
        self.numbers = range(0, 10)
        self.word_list = Reader.read('dictionary.txt').split()
        self.choices = "alphabet ALPHABET special number".split(' ')
        self.password = []

    def random_password(self, length, special_characters=False, random_case=True, numbers=False):
        for _ in length:
            choice = random_type()
            if choice == "alphabet":
                self.password.append(random.choice(self.alphabet))
            elif choice == "ALPHABET":
                self.password.append(random.choice(self.alphabet.upper()))
            elif choice == "special":
                self.password.append(random.choice(self.special_chars))
            elif choice == "number":
                self.password.append(random.choice(self.numbers))

            return ''.join(self.password)


    def dictionary_password(self, length, special_characters=False, numbers=True, range_max=999):
        pass

    def generate_pin(self, length):
        return "".join([str(random.choice(self.numbers)) for i in range(length)])
