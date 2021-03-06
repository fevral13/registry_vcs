from PyQt4 import QtGui


class Commit():
    def __init__(self, created, modified, deleted):
        self.created = created
        self.modified = modified
        self.deleted = deleted

    def created_model(self):
        model = QtGui.QStandardItemModel()
        for item in self.created:
            value_path, value_type_data = item
            value_type, value_data = value_type_data
            row = [
                QtGui.QStandardItem('{}'.format(value_path)),
                QtGui.QStandardItem('{}'.format(value_data))
            ]
            model.appendRow(row)
        return model

    def modified_model(self):
        model = QtGui.QStandardItemModel()
        for item in self.modified:
            value_path, old_value, new_value = item
            value_type, value_data = new_value
            row = [
                QtGui.QStandardItem('{}'.format(value_path)),
                QtGui.QStandardItem('{}'.format(value_data))
            ]
            model.appendRow(row)
        return model

    def deleted_model(self):
        model = QtGui.QStandardItemModel()
        for item in self.deleted:
            value_path, value_type_data = item
            value_type, value_data = value_type_data
            row = [
                QtGui.QStandardItem('{}'.format(value_path)),
                QtGui.QStandardItem('{}'.format(value_data))
            ]
            model.appendRow(row)
        return model



    @property
    def name(self):
        return 'Created {}, modified {}, deleted {}'.format(len(self.created), len(self.modified), len(self.deleted))

    def merge(self, other):
        pass

    def rollback(self):
        return