my_value1 = 10  # int
my_value2 = 11.00
my_value3 = True
my_value4 = None
my_value5 = "Test komm in it"

if my_value1 == 10:
    print('Value ist 10')
elif my_value1 > 10:
    print('Value größer 10')
else:
    print('Hey now')


my_list = [12, "13", True, False, None]  # Liste

for i in my_list:
    print(i)

for i in range(len(my_list)):
    print(1)


my_dict = {
    "a": 1, "b": 3
}  # jewals "n" ist der key und der muss angegeben werden in der For schleidfe

for k, v in my_dict.items():
    print(k, v)

i = 0

while True:
    i += 1
    print(1)
    if i == 10:
        break
