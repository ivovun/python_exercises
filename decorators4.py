

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
def deco(func):
    print(func)
    def inner(self):
        print('running inner()')
    return inner


@deco
def target(arg):
    print(arg, 'running target()')

# deco(target)
target(2)
print(target)