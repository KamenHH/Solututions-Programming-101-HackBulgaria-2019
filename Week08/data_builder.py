import pprint
from collections import deque


class DataBuilder:
    """Builds a list containing the elements of the given data
    in a specific order according to the algorithm (DFS, BFS) used.
    data = [(dict key, dict data)]"""
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

    def dfs(self):
        """Returns a list containing the objects from the data using the DFS algorithm.
        Gets all the children of each object, when the last child is reached, starts backtracking."""
        dfs_struct = []
        def dict_helper(data, struct):
            for obj in data:
                dfs_struct.append((obj, data[obj]))       
                if DataBuilder.is_dict(data[obj]):
                    dict_helper(data[obj], obj)
                elif DataBuilder.is_iterable(data[obj]):
                    iterables_helper(data[obj], struct)
            return struct

        def iterables_helper(iterable, struct):
            """Calls @dict_helper method if the object is of type dict, else
            calls self recursively if @obj is an iterable (list, set, tuple..)."""
            for obj in iterable:
                if DataBuilder.is_dict(obj):
                    dict_helper(obj, struct)
                elif DataBuilder.is_iterable(obj):
                    iterables_helper(obj, struct)
            return struct

        """If data is a dict, first calls @dict_helper, else - calls @iterables_helper.
            This way the program is not limited only to dict schemas"""
        return dict_helper(self.data, dfs_struct) if DataBuilder.is_dict(self.data) \
                                                else iterables_helper(self.data, dfs_struct)

    def bfs(self):
            """Returns a list containing the objects from the data using the BFS algorithm,
            gets all the object at each tree level, when the last object in the level is reached, 
            proceeds to the next one."""
            queue, bfs_struct = deque([self.data]), []
            def bfs_helper(q, struct):
                data = q.popleft()
                for obj in data:
                    bfs_struct.append((obj, data[obj]))
                    if DataBuilder.is_dict(data[obj]): # and data[obj] not in q:
                        q.append(data[obj])
                    elif DataBuilder.is_iterable(data[obj]): # and data[obj] not in q::
                        iterables_helper(data[obj], queue)
                if q:
                    bfs_helper(q, struct)
                return struct
            
            def iterables_helper(iterable, queue):
                """Enqueues the object if it's a dict or
                calls self recursively if @obj is an iterable (list, set, tuple..)."""
                for obj in iterable:
                    if DataBuilder.is_dict(obj):
                        queue.append(obj)
                    elif DataBuilder.is_iterable(obj):
                        iterables_helper(obj, queue)
                return None

            return bfs_helper(queue, bfs_struct)


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

            
    @staticmethod
    def pprint_data(data):
        pprint.pprint(data, indent=1, width=10) 


if __name__ == "__main__":
    data = {
        'a': [
            {
                'a1': 1,
                'a2': 2
            }
        ],
        'b': 2
    }

    data1 = [
        {'a': 1}
    ]
    

    gb = DataBuilder(data1)
    # print(gb.dfs())
    print('')
    print(gb.dfs())
