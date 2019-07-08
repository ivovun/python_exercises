
words = ["premodareciya", "prenemoderaciya",
 "peremoderaciya", "moderaciya"]


def foo(_words, pre):
    return [x for x in _words 
    		      if x.startswith(pre)]


print(foo(words, 'pre'))








# def foo(_words, pref):
#    length = len(pref)
#    _answer = []
#
#    for i in _words:
#
#        if i[length:] == i.replace(pref,  ''):
#
#           _answer.append(i)
#
#
#    return _answer



# def foo(_words, pre):
#     arr = []
#     for x in _words:
#         if x.startswith(pre):
#             arr.append(x)
#     return arr




