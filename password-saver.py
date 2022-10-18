import random
import copy

#Startup|-- User -- set_passphrase -- ask_passphrase
#       |       |______________________________________
#       |-- Storage -- set_database -- load_database --|get_passphrase
#       |       |__________________
#       |-- Session -- set_user --|start_session|
#                                               |get_database

class Key:
    def __init__(self):
        pass

    def get_key(self):
        return str(random.randint(2, 1024))

class Encrypter:
    def __init__(self, key: str):
        self.__key__: str = key

    def encrypt(self, message: str)->str:
        return message + self.__key__

class Decrypter:
    def __init__(self, key: str) -> None:
        self.__key__: str = key

    def decrypt(self, message: str) -> str:
        return message - self.__key__

class Message:
    def __init__(self, title: str, body: str, is_encrypted: bool) -> None:
        self.is_encrypted = is_encrypted
        self.__title__: str = title
        self.__body__: str = body

    def decrypt_message(self, decrypter: Decrypter) -> None:
        self.__title__: str = decrypter.decrypt(self.__title__)
        self.__body__: str = decrypter.decrypt(self.__body__)
        self.is_encrypted = False

    def encrypt_message(self, encrypter: Encrypter) -> None:
        self.__title__: str = encrypter.encrypt(self.__title__)
        self.__body__: str = encrypter.encrypt(self.__body__)
        self.is_encrypted = True

    #getters
    def get_title(self) -> str:
        return self.__title__

    def get_body(self) -> str:
        return self.__body__

    #setters
    def set_title(self, title: str) -> None:
        self.__title__ = title

    def set_body(self, body: str) -> None:
        self.__body__ = body

class Storage:
    def __init__(self, database: list=None) -> None:
        if database is not None:
            self.__database__ = database
        else:
            self.__database__:list = []

    #getters
    def get_database(self) -> list:
        return self.__database__

    #setters
    def set_database(self, database: list) -> None:
        self.__database__ = database

    #database saver
    def save_database(self, passphrase: str):
        path: str = 'db.txt'
        with open(path, 'w') as file:
            file.writelines(data.get_title() + '\n' + data.get_body() + '\n' * 2 for data in self.get_database())
            file.close()

    #database loader
    def load_database(self, passphrase: str):
        return [
            Message('test_title1', 'test_body1', is_encrypted=False),
            Message('test_title2', 'test_body2', is_encrypted=False),
            Message('test_title3', 'test_body3', is_encrypted=False)
            ]
        '''
        path = ''
        with open(path, 'r') as file:
            df = file.read()
            print(df)
            file.close()
        '''

class User:
    def __init__(self, passphrase=None, storage=None):
        if passphrase is not None:
            self.__passphrase__: str = passphrase
        else:
            self.__passphrase__: str = ''

        if storage is not None:
            self.__storage__: Storage = storage
        else:
            self.__storage__: Storage = Storage()

    #getters
    def get_passphrase(self) -> str:
        return self.__passphrase__

    def get_storage(self) -> Storage:
        return self.__storage__

    #setters
    def set_passphrase(self, passphrase: str) -> None:
        self.__passphrase__ = passphrase

    def set_storage(self, storage: Storage) -> None:
        self.__storage__ = storage

class Startup:
    def __init__(self) -> None:
        pass

    def startup(self) -> None:
        user: User = User(passphrase=self.ask_passphrase())
        storage: Storage = Storage()
        storage.set_database(storage.load_database(user.get_passphrase()))
        user.set_storage(storage)
        session: Session = Session()
        session.set_user(user)
        session.start_session()

    def ask_passphrase(self) -> str:
        print('Do you have a passphrase?' + '\n' + '[y/n]')
        passphrase_input = input()
        if passphrase_input == 'y':
            return input('please enter passphrase: ')
        elif passphrase_input == 'n':
            key: Key = Key()
            test_key = key.get_key()
            print(
                'Your passphrase is: ', 
                test_key, 
                '\n' + 'Please write it down before proceed!'
                )
            print('Type any key to proceed...')
            input()
            return test_key
        else:
            print('Please enter y/n')
            self.ask_passphrase()

class Session:
    def __init__(self, user=User()) -> None:
        self.__user__: User = user

    def get_user(self) -> User:
        return self.__user__

    def set_user(self, user: User) -> None:
        self.__user__ = user

    def start_session(self) -> None:
        while True:
            print(
                'Press show to show messages \n' + 
                'Press add to add new message \n' +
                'Press edit n to edit message n \n' +
                'Press encrypt to encrypt database \n' +
                'Press decrypt to decrypt database \n' +
                'Press exit to exit \n'
                )
            answer = input()
            #show all the messages
            if answer == 'show':
                for item in self.__user__.get_storage().get_database():
                    print(item.get_title(), item.get_body())
                print('')
            #add a new message
            elif answer == 'add':
                title: str = input('Enter title of the message: \n')
                body: str = input('Enter body of the message: \n')
                message: Message = Message(title, body, is_encrypted=False)
                df = self.__user__.get_storage().get_database()
                df.append(message)
                self.__user__.get_storage().set_database(df)
                print('New message added \n')
            #edit message
            elif answer == 'edit':
                pass
            #encrypt entire database
            elif answer == 'encrypt':
                pass
            #decrypt entire database
            elif answer == 'decrypt':
                pass
            #break
            elif answer == 'exit':
                break
            #unexpected input
            else:
                print(
                    'Unexpected input: ', 
                    answer, 
                    '\n' + 'Please provide expected input'
                    )
            
            self.__user__.get_storage().save_database('db.txt')

def __main__() -> int:
    startup: Startup = Startup()
    startup.startup()
    return 0

if __name__ == '__main__':
    __main__()