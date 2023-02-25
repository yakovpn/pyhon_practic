from phonebook import phonebook
pb = phonebook("phonebook.txt")


def listRecordsAll():
    print(*pb.recordList, sep='\n')
    return True


def inputRecord(id=None):
    return {
        'id': id,
        'firstName': input("input first name:"),
        'middleName': input("input middle name:"),
        'lastName': input("input last name:"),
        'phone': input("input phone:")
    }


def addRecord():
    r = inputRecord()
    pb.add(r['firstName'], r['middleName'], r['lastName'], r['phone'])
    return True


def removeRecord():
    recordId = int(input("input record id:"))
    pb.remove(recordId)
    return True


def editRecord():
    rId = int(input("input record id:"))
    print(pb.get(rId))
    r = inputRecord(rId)
    pb.editRecord(r)
    return True


def searchRecord():
    substr = input("Input search string:")
    print(*pb.search(substr), sep='\n')
    return True

def savePhonebook():
    pb.saveToFile()
    return True


def exitFunc():
    return False


menuDict = {
    1: {"description": "List all record", "func": listRecordsAll},
    2: {"description": "Add new record", "func": addRecord},
    3: {"description": "Remove record", "func": removeRecord},
    4: {"description": "Edit record", "func": editRecord},
    5: {"description": "Save phonebook", "func": savePhonebook},
    6: {"description": "Search record", "func": searchRecord},
    7: {"description": "Exit", "func": exitFunc},
}

play = True
while play:
    for key, item in menuDict.items():
        print(f'{key}:{item["description"]}')

    try:
        index = int(input("Please select menu item:"))
        play = [item["func"]
                for key, item in menuDict.items() if key == index][0]()
    except Exception as e:
        print(e)
        break
