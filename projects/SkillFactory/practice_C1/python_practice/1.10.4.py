class Client:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Guests(Client):
    def __init__(self, name, address, status):
        super().__init__(name)
        self.address = address
        self.status = status

    def get_address(self):
        return self.address

    def get_status(self):
        return self.status


List = [{'name': 'Петя', 'address': 'МCK', 'status': 'VIP'}, {'name': 'Вася', 'address': 'СПБ', 'status': 'Regular'}]
#with open('client.txt', "r") as List:

print('Список приглашенных гостей')
for i in List:
    client = Guests(name=i.get('name'), address=i.get('address'), status=i.get('status'))
    print(f'{client.name}, г. {client.address}, статус {client.status}')
