def func():
    print("hello")

func()
# arguement
def func2(arg1, arg2):
    if arg1:
        print("Arg1")
        return arg1
    elif arg2:
        print("Arg2")
        return arg2
    print("hi")

a = func2(False, False) 
print(a)

func()