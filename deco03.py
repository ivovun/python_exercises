def prefix_deco(pref):
	def deco(orig_func):
	    print(pref, orig_func)
	    def inner(x):
	        print(pref, 'running inner()')
	        orig_func(x)
	        print(pref, 'after original func')
	    return inner
	return deco  

def target(n):
    print(f'running target(), par={n}')


target = prefix_deco('LOG:')(target)
target(2)