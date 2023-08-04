def func1(huh):
    def wrapper(*args):
        print("this func1")
        return huh(*args)
    return wrapper

@func1
def func2(hello):
    print("this func2", hello)

func2(10)