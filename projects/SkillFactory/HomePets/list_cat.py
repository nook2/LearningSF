from class_pets import Pets

cats = [
    {
        "name": "barsik",
        "sex": "male",
        "age": "3",
    },
    {
        "name": "murka",
        "sex": "female",
        "age": "5",
    },
    {
        "name": "kat",
        "sex": "male",
        "age": "7",
    },
    {
        "name": "lusa",
        "sex": "female",
        "age": "3",
    },
    {
        "name": "pushok",
        "sex": "male",
        "age": "4",
    },
]
for cat in cats:
    c = Pets(name=cat.get("name"), sex=cat.get("sex"), age=cat.get("age"))
    print(c.name)
    print(c.sex)
    print(c.age)
