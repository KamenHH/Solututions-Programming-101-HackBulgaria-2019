from datagenerator import DataGenerator


class DeepOps:
    def __init__(self, data):
        self._data = DataGenerator(data)
    
    @property
    def data(self):
        return self._data.data

    def deep_find(self, key, bfs=False):
        """Task 1. Returns the first occurrence of the given @key in the data.
        (Returns the first element from @deep_find_all.)"""
        result = self.deep_find_all(key, bfs)
        return result[0] if result else None

    def deep_find_all(self, key, bfs=False):
        """Task2. Returns of all the values that match the given @key in the data."""
        if bfs:
            gen_data = self._data.bfs()
        else:
            gen_data = self._data.dfs()
        return [value for obj in gen_data
                for k, value in obj.items()
                if k == key]

    def deep_update(self, key, val):
        """Task3. Updates all vulues in the data with key equal to the given @key argument."""
        for obj in self._data.dfs():
            for k in obj:
                if k == key:
                    obj[k] = val


    def deep_aplly(self, function):
        """Task4. Apllies (if possible) @function to all the values of the data."""
        for obj in self._data.dfs():
            for key in obj:
                try:
                    obj[key] = function(obj[key])
                except Exception: continue

    def deep_compare(self, other):
        """Task5. Compares to objects ( dicts, list or other iterables). 
        Returns true if their structure, types and keys are equal."""

        def dicts_helper(self_data, other_data):
            if len(self_data) != len(other_data):
                return False
            for (self_k, self_v), (other_k, other_v) in zip(self_data.items(), other_data.items()):
                if self_k == other_k:
                    if type(self_v) != type(other_v):
                        return False
                    elif DataGenerator.is_dict(self_v):
                        if not dicts_helper(self_v, other_v): 
                            return False
                    elif DataGenerator.is_iterable(self_v):
                        if not iterable_helper(self_v, other_v):
                            return False
                    else:
                        if self_v != other_v:
                            return False
                else:
                    return False
            return True
            
        def iterable_helper(self_data, other_data):
            if len(self_data) != len(other_data):
                return False
            for self_item, other_item in zip(self_data, other_data):
                if type(self_item) != type(other_item):
                    return False
                elif DataGenerator.is_dict(self_item):
                    if not dicts_helper(self_item, other_item):
                        return False
                elif DataGenerator.is_iterable(self_item):
                    if not iterable_helper(self_item, other_item):
                        return False
                else:
                    if self_item != other_item:
                        return False
            return True

        return dicts_helper(self.data, other) if DataGenerator.is_dict(self.data) else \
                                                    iterable_helper(self.data, other)
