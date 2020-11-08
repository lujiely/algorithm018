for i in range(10-1,0,-1):
    print(i)
    i = 5

class A(object):
    def __init__(self):
        print("init")
    def __del__(self):
        print("del")
print(A() is A())
print(id(A()) is id(A()))


