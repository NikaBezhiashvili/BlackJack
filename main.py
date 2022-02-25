## Imports

from db import *

# Class

class Player:
    def __init__(self, name ,balance):
        self.balance = balance
        self.name = name
    

    def hello(self):
        return f'Welcome {self.name}! Your balance - {self.balance}'

    def show_balance(self):
        return f'Your Balance is {self.balance}$'

    def update_balance(self, change):
        pass #TODOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO

## Login / Register

def login():
     while True:
                login_username = input('Enter username: ')
                if len(login_username) > 20: ## IN DATABASE NICKNAME COLUMN HAS 20 CHAR LEN LIMIT
                    print('Wrong Username')
                else:
                    try:
                        if login_username != cursor.execute(f"select nickname from krn_players where nickname = '{login_username}'").fetchone()[0]:
                            print('Exception1') ### EXCEPTION /  ## if returned exception means that username doesnt exists
                        elif login_username == cursor.execute(f"select nickname from krn_players where nickname = '{login_username}'").fetchone()[0]:
                            login_password = input('Enter password: ')
                            try:
                                if login_password == cursor.execute(f"select password from krn_players where nickname = '{login_username}'").fetchone()[0]:
                                    print('Logged in succesfully.')
                                    player = Player((cursor.execute(f"select nickname from krn_players where nickname = '{login_username}'").fetchone()[0]),(cursor.execute(f"select balance from krn_players where nickname = '{login_username}'").fetchone()[0]) )
                                    print(player.hello())
                                    break
                                elif login_password != cursor.execute(f"select password from krn_players where nickname = '{login_username}'").fetchone()[0]:
                                    ask = int(input('Wrong password.\nTry again - 1\nRegister page - 2\n'))
                                    try:
                                        if ask == 1:
                                            login()
                                        elif ask == 2:
                                            register()
                                    except ValueError:
                                        print('Wrong value Try Again')
                                        pass                              
                            except:
                                print('Wrong Value, try again.')                              
                    except TypeError:
                        while True:
                                    ask = int(input('Wrong username.\nTry again - 1\nRegister page - 2\n'))
                                    try:
                                        if ask == 1:
                                            login()
                                        elif ask == 2:
                                            register()
                                    except ValueError:
                                        print('Wrong value Try Again')
                                        pass

def register():
    while True:
                new_player_username = input('Enter new player username: ')
                if len(new_player_username) > 20: ## IN DATABASE NICKNAME COLUMN HAS 20 CHAR LEN LIMIT
                    print('Username must be least than 20 symbol')
                    pass
                else:    
                    try:
                        if new_player_username == cursor.execute(f"select nickname from krn_players where nickname = '{new_player_username}'").fetchone()[0]: ### EXCEPTION / if returned exception means that username doesnt exists
                            while True:
                                ask = int(input('Username is already taken.\nTry again - 1\nLogin page - 2\n'))
                                try:
                                    if ask == 1:
                                        register()
                                    elif ask == 2:
                                        login()
                                except ValueError:
                                    print('Wrong value Try Again')
                                    pass
                    except:
                        new_player_password = input('Enter new player password: ')
                        cursor.execute(f"insert into krn_players values (null, '{new_player_username}', '{new_player_password}', 0)")
                        cursor.commit()
                        player = Player((cursor.execute(f"select nickname from krn_players where nickname = '{new_player_username}'").fetchone()[0]),(cursor.execute(f"select balance from krn_players where nickname = '{new_player_username}'").fetchone()[0]) )
                        print(player.hello())
                        break

while True:
    try:
        Question_one = int(input('Login - 1\nRegister - 2\n')) 
        if Question_one == 1:
            login()
        elif Question_one == 2:
            register()            
        break                    
    except:
        print('here')
        break

# Run the program / Play the game