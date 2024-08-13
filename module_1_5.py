immutable_var = (1, 2, "a", "b", True)
print (immutable_var)
# immutable_var[2]= 4 # кортеж не поддерживает обращение по элементам, неизменяем.
# print(immutable_var)
mutable_list = ([1, 2, 3], ["a", "b", "c"], [True])
print(mutable_list)
mutable_list[0] [0] = 5
print(mutable_list)
mutable_list[1] [0] = "E"
