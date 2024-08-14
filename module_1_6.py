my_dict = {"Alex": 1990, "Valeria": 1991, "Nikita": 2015}
print(my_dict)
print(my_dict["Alex"])
print(my_dict.get("Alisa", "Такого ключа нет"))
my_dict.update({"Sasha": 1990, "Jenia": 1992})
print(my_dict)
new_dict = my_dict.pop("Nikita")
print(new_dict)
print(my_dict)

my_set = {1, 2, 3, 1, 1, 1, 2, 2, "string",(4,5,6),(4,5,6),True, True }
print(my_set)
my_set.add(8)
my_set.add(7)
my_set.discard(1)
print(my_set)
