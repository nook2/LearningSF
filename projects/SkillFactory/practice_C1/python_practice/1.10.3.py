class Client:
    def __init__(self, name='', surname='', balance=0):
        self.name = name
        self.surname = surname
        self.balance = balance

    def get_data(self):
        return self.name

    def get_name(self):
        return self.surname

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f' Клиент "{self.name} {self.surname}". Баланс:{self.balance}'


client = Client('Иван', 'Петров', 50)
print(client)
