"""Builds the desired value according to the algorithm (DFS, BFS) used."""
import pprint


class GraphBuilder:
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

    def dfs(self):
        dfs_struct = []
        def _dfs(data, items):
            for obj in data:
                dfs_struct.append((obj, data[obj])) 
                if GraphBuilder.is_dict(data[obj]):
                    _dfs(data[obj], obj)
                elif GraphBuilder.is_iterable(data[obj]):
                    for sub_obj in data[obj]:
                        if GraphBuilder.is_dict(sub_obj):
                            _dfs(sub_obj, items)
            return items

        return _dfs(self.data, dfs_struct)

    @staticmethod
    def is_dict(obj):
        return isinstance(obj, dict)
    
    @staticmethod
    def is_iterable(obj):
        try:
            iter(obj)
            return True
        except TypeError:
            return False

            
    @staticmethod
    def pprint_data(data):
        pprint.pprint(data, indent=1, width=17) 


if __name__ == "__main__":
    data = {
        'a': [
                {
                    'a1':1, 
                    'b1': [
                        {
                            'a2': 2,
                            'b2': 3
                        }
                    ]
                }
            ],
    }

    gb = GraphBuilder(data)
    print(gb.dfs())