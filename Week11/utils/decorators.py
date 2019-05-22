import os


class Clear:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        os.system('cls' if os.name == 'nt' else 'clear')
        return self.func(*args, **kwargs)


if __name__ == "__main__":
    c = Clear(lambda x: print(x+2))(2)
