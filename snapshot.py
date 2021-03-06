from datetime import datetime

from regobj import HKEY_LOCAL_MACHINE, HKEY_USERS, HKEY_CURRENT_USER
from commit import Commit

KEYS = (HKEY_LOCAL_MACHINE, HKEY_USERS)
KEYS = (HKEY_CURRENT_USER, )

class Snapshot():
    def __init__(self, initial=False):
        self.name = str(datetime.now())
        self.values = {}
        if not initial:
            for root in KEYS:
                self.collect_values(root)

    def collect_values(self, root, path=''):
        for value in root.values():
            value_path = '{path}\\{root_name}\\{name}'.format(path=path, root_name=root.name, name=value.name)
            self.values[value_path] = value.type, value.data

        if path:
            root_path = '{path}\\{root_name}'.format(path=path, root_name=root.name)
        else:
            root_path = root.name
        for subkey in root.subkeys():
            self.collect_values(subkey, root_path)

    def compare_to(self, other):
        self_keys = set(self.values.keys())
        other_keys = set(other.values.keys())

        deleted_keys = other_keys - self_keys
        created_keys = self_keys - other_keys

        common_keys = self_keys.intersection(other_keys)
        modified_keys = set((key for key in common_keys if self.values[key] != other.values[key]))

        created = [(k, self.values[k]) for k in created_keys]
        deleted = [(k, other.values[k]) for k in deleted_keys]
        modified = [(k, self.values[k], other.values[k]) for k in modified_keys]
        return Commit(created, modified, deleted)

if __name__ == '__main__':
    before = datetime.now()
    s1 = Snapshot()
    print(len(s1.values))
    print(datetime.now() - before)
    p = input('change anything')

    s2 = Snapshot()

    print(s1.compare_to(s2))