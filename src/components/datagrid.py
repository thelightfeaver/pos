"""Widget Table."""

from PySide6.QtCore import QAbstractTableModel, Qt


class DataGrid(QAbstractTableModel):
    def __init__(self, data, headers=list[str], values=list[str]):
        super().__init__()
        self._data = data
        self._headers = headers
        self._values = values

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            categoria = self._data[index.row()]

            for i, value in enumerate(self._values):
                if index.column() == i:

                    if type(value) == list:
                        sub_att = categoria
                        for v in value:
                            sub_att = getattr(sub_att, v)

                        return sub_att
                    else:
                        return getattr(categoria, value)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._headers[section]
            elif orientation == Qt.Vertical:
                return str(section + 1)

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable
