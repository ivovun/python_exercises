

# class PostSave():
#     def connect(self, func, **kwargs):
#     # def connect(func, **kwargs):
#         for key, value in kwargs.items():
#             print("%s == %s" % (key, value))
#             print("post_save")
#
#
# ps = PostSave()
# ps.connect(2, x='2')
#
#
# def myFun(arg1, **kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))
#
#     # Driver code
#
#
# myFun("Hi", first='Geeks', mid='for', last='Geeks')


def deco(old_f):
    print(f'{deco} initialised with {old_f}')

    def new_f(*args, **kwargs):
        print(f'in "{new_f.__name__}" the old:"{old_f}":')
        old_f(*args, **kwargs)

    return new_f

@deco
def target(*args, **kwargs):
    print(f'run "{target}", param={args},{kwargs}')

target(8)


# def deco(func):
#     print(func)
#     def inner(x):
#         print('running inner()')
#         func(x)
#     return inner

# def target(n):
#     print(f'running target(), par={n}')

# target = deco(target)
# target(2)
