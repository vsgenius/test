def people(number):
    # number = input("Введите номер документа: ")
    for document in documents:
        if document["number"] == number:
            return True
    return False


def shelf(number):
    # number = input("Введите номер документа: ")
    for key, value in directories.items():
        if number in value:
            return True
    return False


def list_doc():
    for document in documents:
        print(document['type'], document['number'], document['name'])


def add_doc(number_doc,type_doc,name_doc,num_dir):
    # number_doc = input("Введите номер документа: ")
    # type_doc = input("Введите тип документа: ")
    # name_doc = input("Введите имя владельца: ")
    while True:
        # num_dir = input("Введите номер полки: ")
        if num_dir in directories.keys():
            break
        else:
            return False
    new_doc = {"type": type_doc, "number": number_doc, "name": name_doc}
    documents.append(new_doc)
    directories[num_dir].append(number_doc)
    return True


def delete(number_doc):
    # number_doc = input("Введите номер документа для УДАЛЕНИЯ: ")
    res = False
    for doc in documents:
        if number_doc in doc['number']:
            documents.remove(doc)
            res = True
            break
    for key, value in directories.items():
        if number_doc in value:
            value.remove(number_doc)
            res = True
    return True if res else False


def move(number_doc, num_dir):
    while True:
        # number_doc = input("Введите номер документа для переноса: ")
        if find_dir_val(number_doc) != False:
            break
        else:
            return False
    while True:
        # num_dir = input("Введите номер целевой полки: ")
        if find_dir_key(num_dir) != False:
            break
        else:
            return False
    directories[find_dir_val(number_doc)].remove(number_doc)
    directories[num_dir].append(number_doc)
    return True


def add_shelf(num_dir):
    while True:
        # num_dir = input("Введите номер целевой полки: ")
        if find_dir_key(num_dir) == False:
            break
        else:
            return False
    directories[num_dir] = []
    return True


def find_dir_val(number):
    for key, value in directories.items():
        if number in value:
            return key
    return False


def find_dir_key(number):
    for key, value in directories.items():
        if number in key:
            return True
    return False


def list_shelf():
    for key, value in directories.items():
        print(f'Полка {key} : {value}')


def main():
    while True:
        command = input("Введите команду: ")
        if command == 'p':
            print(people())
            print()
        elif command == 's':
            print(shelf())
            print()
        elif command == 'l':
            list_doc()
            print()
        elif command == 'a':
            print(add_doc())
            print()
        elif command == 'd':
            print(delete())
            print()
        elif command == 'm':
            print(move())
            print()
        elif command == 'as':
            print(add_shelf())
            print()
        elif command == 'ls':
            list_shelf()
            print()
        elif command == 'q':
            break
        elif command == 'h':
            print("""
    # p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    # s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    # l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    # a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
    # d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. 
    # m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. 
    # as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
    # h - help.
    # q - Выход
        """)
            print()
        else:
            print('Ввведите правильную команду. Введите "h" для прочтения Help')


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
