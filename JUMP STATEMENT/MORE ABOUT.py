

print("Enter list of numbers. Enter z to exit. ")
list_num = []
while True:
    inp = input()
    if inp == 'z':
        break
    list_num.append(int(inp))
else:
     print("done")
print(list_num)