# initial = input()
# symbols = ['+', '-', '*', '/', '(', ')']
# initial = initial.replace(" ", "")
# print(initial, len(initial))
# final = ""
# operator = list()
# ind = list()

# for i in range(len(initial)):
#     if initial[i] in symbols:
#         final += ","
#         operator.append(initial[i])
#         ind.append(i)
#     else:
#         final += initial[i]

# final_list = final.split(",")
# print(final_list)
# print(operator)
# print(ind)

x = input()
new_list = [*x.replace(" ","")]
print(new_list)
proper_list = []
temp = ""
for i in new_list:
    if i.isdigit():
        temp += str(i)
        if new_list.index(i) == len(new_list):
            proper_list.append(temp)
        # break
    else:
        proper_list.append(temp)
        proper_list.append(i)
        temp = ""
print(proper_list)
