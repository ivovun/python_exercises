n = 0


def receiver(signal, **kwargs):
    global n
    n = n + 1
    print(n, '. receiver')
    def _decorator(func):
        signal.connect(func)
        return func
    return _decorator


def create(user):
    print(f"create user={user}")


class PostSave():
    def connect(self, func, **kwargs):
        print("connect ")

    def __init__(self):
        self.x = 3

    print("post_save")


ps = PostSave()

@receiver(ps, sender=1)
def create_profile(sender, instance, created, **kwargs):
    if created:
        create(user=instance)


create_profile(None, 1, 2)

