import json
from os import path


class phonebook:
    filename = None
    recordList = []
    autoIncrement = 0

    def __init__(self, filename):
        self.filename = filename
        self.recordList = []
        if path.exists(filename):
            self.readFromFile()

    def readFromFile(self):
        with open(self.filename) as json_file:
            self.__dict__ = json.load(json_file)

    def saveToFile(self):
        with open(self.filename, "w", encoding="utf-8") as json_file:
            json.dump(self, json_file,
                      default=lambda obj: obj.__dict__, sort_keys=True, indent=4)

    def add(self, firstName: str, middleName: str, lastName: str, phone: str):
        self.autoIncrement += 1
        record = {
            'id': self.autoIncrement,
            'firstName': firstName,
            'middleName': middleName,
            'lastName': lastName,
            'phone': phone
        }
        self.recordList.append(record)
        return True

    def remove(self, recordId: int):
        self.recordList.remove(self.get(recordId))

    def get(self, recordId: int):
        return [item for item in self.recordList if item["id"] == recordId][0]

    def subs(self, record: dict, substr):
        return len([value for key, value in record.items() if substr in str(value)]) > 0

    def search(self, substr: str):
        return list(filter(
            lambda record: len([value for key, value in record.items() if substr in str(value)]) > 0, self.recordList))

    def editRecord(self, record):
        self.recordList.remove(
            [item for item in self.recordList if item['id'] == record['id']][0])
        self.recordList.append(record)
