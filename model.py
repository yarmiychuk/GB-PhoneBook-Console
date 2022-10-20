path = 'phonebook.txt'
contacts = []
last_id: str = '0'
current_id: str = ''

def read_file():
    global contacts, last_id
    with open(path, 'r', encoding='utf_8') as f:
        contacts = [i.strip().split(';') for i in f.readlines()]
    last_id = '0' if len(contacts) == 0 else contacts[len(contacts) - 1][0]
    return contacts

def get_contacts():
    global contacts
    return contacts

def add_contact():
    global contacts, last_id
    new_id = str(int(last_id) + 1)
    contact = [new_id,\
        input('Введите Имя: '),\
        input('Введите Телефон: '),\
        input('Введите Комментарий: ')]
    contacts.append(contact)
    last_id = new_id
    return contact

def edit_contact():
    global contacts, current_id
    if current_id == '':
        return None
    index = get_index(current_id)
    if index == None:
        return None
    contact = [current_id,\
        input('Введите Имя: '),\
        input('Введите Телефон: '),\
        input('Введите Комментарий: ')]
    contacts[index] = contact
    current_id = ''
    return contact

def save_file():
    global contacts
    try:
        with open(path, 'w', encoding='utf_8') as f:
            for contact in contacts:
                f.write(';'.join(contact) + "\n")
    except:
        return False            
    return True

def delete_contact():
    global contacts, current_id
    if current_id == '':
        return False
    for i in range(len(contacts)):
        if contacts[i][0] == current_id:
            current_id = ''
            contacts.pop(i)
            return True
    return False

def get_index(id: str):
    global contacts
    for i in range(len(contacts)):
        if contacts[i][0] == id:
            return i
    return None

def get_current():
    global contacts, current_id
    if current_id == '':
        return None
    for i in range(len(contacts)):
        if contacts[i][0] == current_id:
            return contacts[i]
    return None
    

def find_by_name(name: str):
    global contacts, current_id
    current_id = ''
    for i in range(len(contacts)):
        if contacts[i][1] == name:
            current_id = contacts[i][0]
            return contacts[i]
    return None