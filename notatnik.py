from main import add_user, data_of_users, read, delete_user, update_user

while True:
    print('menu:')
    print('0 - zakończ pracę')
    print('1 - dodaj użytkownika')
    print('2 - usuń użytkownika')
    print('3 - wyświetl użytkowników')
    print('4 - aktualizuj użytkownika')
    menu_option: str = input('Podaj opjcę do uruchomienia: ')
    if menu_option == '0': break
    if menu_option == '1': add_user(data_of_users)
    if menu_option == '2': delete_user(data_of_users)
    if menu_option == '3': read(data_of_users)
    if menu_option == '4': update_user(data_of_users)