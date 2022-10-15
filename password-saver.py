from email.policy import default
import random
import copy

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

class User:
    def __init__(self):
        self.__passphrase__: str = ''
        self.__database__:list = []

    #getters
    def get_database(self) -> list:
        return self.__database__

    def get_passphrase(self) -> str:
        return self.__passphrase__

    #setters
    def set_database(self, database: list) -> None:
        self.__database__ = database

    def set_passphrase(self, passphrase: str) -> None:
        self.__passphrase__ = passphrase

class Startup:
    def __init__(self) -> None:
        pass

    def startup(self) -> None:
        user: User = User()
        user.set_passphrase = self.ask_passphrase()
        user.set_database(self.recieve_database(user.get_passphrase()))
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
            print('Your passphrase is: ', test_key, '\n' + 'Please write it down before proceed!')
            print('Type any key to proceed...')
            input()
            return test_key
        else:
            print('Please enter y/n')
            self.ask_passphrase()

    def recieve_database(self, passphrase: str) -> list:
        return [
            Message('test_title1', 'test_body1', is_encrypted=False),
            Message('test_title2', 'test_body2', is_encrypted=False),
            Message('test_title3', 'test_body3', is_encrypted=False)
            ]

class Session:
    def __init__(self, user=User()) -> None:
        self.user: User = user

    def get_user(self) -> User:
        return self.user

    def set_user(self, user: User) -> None:
        self.user = user

    def start_session(self) -> None:
        print('Press s to show messages')
        answer = input()
        if answer == 's':
            for item in self.user.get_database():
                print(item.get_title(), item.get_body())
        else:
            print('Unexpected input: ', answer, '\n' + 'Please provide expected input')
            self.start_session()

def __main__() -> int:
    startup: Startup = Startup()
    startup.startup()
    
    '''user: User = User()
    user.set_database(startup.recieve_database('df'))
    session: Session = Session()
    session.set_user(user)
    session.start_session()'''
    return 0

if __name__ == '__main__':
    __main__()