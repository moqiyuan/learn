def deco(fx):
    def fn(a):
        print('hello fn')
        fx(a)
        print('hello fx')
    return fn

@deco
def fx(a):
    for i in range(a):
        print(i*i)
fx(3)
