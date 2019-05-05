from datagenerator import DataGenerator


class DeepOps:
    def __init__(self, data_generator_obj):
        self._data = data_generator_obj

    def deep_find(self, key, bfs=False):
        result = self.deep_find_all(key, bfs)
        return result[0] if result else None

    def deep_find_all(self, key, bfs=False):
        if bfs:
            gen_data = self._data.bfs()
        else:
            gen_data = self._data.dfs()
        return [value for obj in gen_data
                for k, value in obj.items()
                if k == key]

    def deep_update(self, key, val):
        for obj in self._data.dfs():
            for k in obj:
                if k == key:
                    obj[k] = val


    def deep_aplly(self, function):
        for obj in self._data.dfs():
            for key in obj:
                try:
                    obj[key] = function(obj[key])
                except Exception: continue

    