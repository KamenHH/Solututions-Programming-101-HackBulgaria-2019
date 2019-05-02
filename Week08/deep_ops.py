from data_builder import DataBuilder

class DeepOps:
    def __init__(self, data):
        self._data_object = DataBuilder(data)

    def deep_find(self, key, bfs=False):
        result = self.deep_find_all(key, bfs)
        return result[0] if result else None

    def deep_find_all(self, key, bfs=False):
        if bfs:
            ordered_data = self._data_object.bfs()
        else:
            ordered_data = self._data_object.dfs()
        return [v for k, v in ordered_data
                if k == key]

    def deep_compare(self, obj1, obj2):
        pass
        
if __name__ == "__main__":
    # data = [{'a': 1}]
    # obj = DeepOps(data)
    # for i in obj.deep_find_all('a'):
    #     print(i)
    # print(obj.deep_find('a', bfs=True))
    db_obj = DataBuilder({'a': 1})
    dfs_result = db_obj.dfs()
    print(db_obj.data)
    print(dfs_result)