from collections import deque


class DataGenerator:
    """Returns a generator object. Depending on the algorithm used (DFS, BFS)"""
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

    def dfs(self):
        """Returns a generator object which yields each item from the input data.
        Gets all the children of each node (dict value), if any, and then starts backtracking."""

        def dict_helper(data):
            """Works with dicts only.
            If it encounters an iterable different from dict, calls @iterables_helper()"""
            yield data
            for key, value in data.items():
                if DataGenerator.is_dict(value):                    
                    yield from dict_helper(value)
                elif DataGenerator.is_iterable(value):
                    yield from iterables_helper(value)

        def iterables_helper(iterable):
            """Calls @dict_helper method if the object is of type dict, else
            calls self recursively if @obj is an iterable (list, set, tuple..)
            until a dictionary is reached.
            """
            for obj in iterable:
                if DataGenerator.is_dict(obj):
                    yield from dict_helper(obj)
                elif DataGenerator.is_iterable(obj):
                    yield from iterables_helper(obj)

        """If data is a dict, first calls @dict_helper, else - calls @iterables_helper.
            This way the program is not limited only to dict schemas"""
        return dict_helper(self.data) if DataGenerator.is_dict(self.data) \
                                                else iterables_helper(self.data)

    def bfs(self):
        """Returns a generator object which yields each item from the input data.
        Gets all the nodes at each tree level (dict keys)
        and then proceeds to the children."""
        q = deque([self._data])
        def bfs_helper(queue):     
            """Works with dicts only.
            If it encounters an iterable different from dict, calls @iterables_helper()"""
            data = q.popleft()
            # we call in case a list/tuple/set schema is given
            if DataGenerator.is_iterable(data) and not DataGenerator.is_dict(data):
                iterables_helper(data, queue)
                data = q.popleft()
            yield data
            for key, value in data.items():
                if DataGenerator.is_dict(value): 
                    queue.append(value)
                elif DataGenerator.is_iterable(value):
                    iterables_helper(value, queue)
            if queue:
                yield from bfs_helper(queue)
            

        def iterables_helper(iterable, queue):
            """Enqueues @obj if it is a dict or
            calls self recursively if @obj is an iterable (list, set, tuple..)
            until all dicts have been appended to the @queue."""
            for obj in iterable:
                if DataGenerator.is_dict(obj):
                    queue.append(obj)
                elif DataGenerator.is_iterable(obj):
                    iterables_helper(obj, queue)

        return bfs_helper(q)

    @staticmethod
    def is_dict(obj):
        return isinstance(obj, dict)
    
    @staticmethod
    def is_iterable(obj):
        if isinstance(obj, str):
            return False
        try:
            iter(obj)
            return True
        except TypeError:
            return False


def main():
    pass


if __name__ == "__main__":
    main()    