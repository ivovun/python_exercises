
def deco(old_f):
    print(f'{deco} initialised with {old_f}')

    def new_f(*args, **kwargs):
        print(f'in "{new_f.__name__}" the old:"{old_f}":')
        old_f(*args, **kwargs)

    return new_f


def target(*args, **kwargs):
    print(f'run "{target}", param={args},{kwargs}')

target = deco(target)
target(8)