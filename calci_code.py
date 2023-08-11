import time

with open("logging.txt", "w") as write_file:
    write_file.write("") 

def logging(fun):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, *kwargs)
        time_taken = time.time() - start_time
        with open("logging.txt", "a") as append_file:
            append_file.write(f"ran {fun} for {time_taken}")
    return wrapper

x = "11 +22 -1*((6/2)*2)+1-(12/2)"
new_list = [*x.replace(" ","")]
#print(new_list)
proper_list = []
temp = ""

for i in range(len(new_list)):
    if new_list[i].isdigit():
        temp += str(new_list[i])
        if i == len(new_list)-1:
            proper_list.append(temp)
    else:
        if len(temp) > 0:
            proper_list.append(temp)
        proper_list.append(new_list[i])
        temp = ""

print(f"Proper List: {proper_list}, {len(proper_list)}")

temp2 = 0
str_with_symb = ""

def subtract(num_1, num_2):
    return num_1 - num_2

def add(num_1, num_2):
    return num_1 + num_2

def divide(num_1, num_2):
    return num_1 / num_2

def multiply(num_1, num_2):
    return num_1 * num_2

operators = {
    "-":subtract,
    "+":add,
    "/":divide,
    "*":multiply,
}

@logging
def calculate(num_1, operator, num_2):
    return operators[operator](int(num_1), int(num_2))

@logging
def calc(start_index, n_list):
    num_1 = None
    num_2 = None
    opr = None
    for i in range(start_index+1, len(n_list)):
        if i == len(n_list):
            return n_list
        if str(n_list[i]).replace(".","",1).isdigit():
            if not num_1:
                num_1 = n_list[i]
            else:
                num_2 = n_list[i]
        elif n_list[i] in [*"+-*/"]:
            opr = n_list[i]
        elif n_list[i] == "(":
            start_index = i
        elif n_list[i] == ")":
            return (start_index, i, result)
        if num_1 and num_2 and opr:
            result = calculate(num_1,opr, num_2)

@logging
def func(n_list):
    try:
        refresh_list = calc(n_list.index("("), n_list)
        n_list = n_list[0 : refresh_list[0]] + [refresh_list[2]] + n_list[refresh_list[1]+1:]
        return func(n_list)
    except ValueError as e:
        return n_list
func(proper_list)
print("Final List:", func(proper_list))