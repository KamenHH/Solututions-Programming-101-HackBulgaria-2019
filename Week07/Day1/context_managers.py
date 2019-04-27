from contextlib import contextmanager
from datetime import datetime
from random import randint
import time


class PerformanceManager:
    def __init__(self, name):
        self.filename = name

    def __enter__(self):
        self.start = datetime.now()
        return self

    def __exit__(self, *args):
        end = datetime.now()
        exec_time = end - self.start
        with open(self.filename, 'a') as f:
            f.write(f'Date {end}. Execution time: {exec_time.total_seconds()}\n')


@contextmanager
def performance(filename):
    """decorator version"""
    start = datetime.now()
    yield
    end = datetime.now()
    exec_time = end - start
    with open(filename, 'a') as f:
        f.write(f'Date {end}. Execution time: {exec_time.total_seconds()}\n')


class assertRaises:
    def __init__(self, exception, msg=None):
        self.exception = exception
        self.msg = msg

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            raise Exception('Error, no excpetion was raised')
        if self.msg is not None and self.msg != exc_val:
            raise Exception('Error, excpetion messeages are not the same!')
        if exc_type != self.exception:
            raise Exception(f'Error, exptected {self.exception}, got {exc_type}!') 
        print('Test passed.')
        return True


@contextmanager
def assertRaisesCMDecorator(exception, msg=None):
    """decorator version"""
    try:
        yield
    except Exception as e:
        if msg is not None and msg != str(e):
            raise Exception('Error, excpetion messeages are not the same!')
        elif not isinstance(e, exception):
            raise Exception(f'Error, exptected {exception}, got {e.__class__}!')         
        else:
            print('Test passed.')
            return True
    else:
        raise Exception('Error, no excpetion was rasied!')


def foo():
    time.sleep(randint(1,2))
    print('Done!')


def foo1(a):
    if not isinstance(a, int):
        raise ValueError('Some cool error!')


def main():
    with performance('performance_log.txt'):
        foo()

    with PerformanceManager('performance_log.txt'):
        foo()

    with assertRaises(ValueError):
        foo1('a')

    with assertRaisesCMDecorator(ValueError, 'Some cool error!'):
        foo1('a')


if __name__ == "__main__":
    main()



