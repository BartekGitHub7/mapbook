from centre_list import centres
from funkcje import show_list, add_centre, remove_centre, update_centre, show_clients, show_all_clients, add_client, remove_client, update_client, show_reservations, add_reservation, remove_reservation, update_reservation, show_all_employees, show_employees, add_employee, remove_employee, update_employee


correct_password = "qwerty"
logged_in = False

while not logged_in:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Logowanie udane!")
        logged_in = True
    else:
        print("Złe hasło!")

if logged_in:
    if __name__ == '__main__':
        print('Witaj ponownie!')
        while True:
            print('Menu:')
            print('0 - Zamknij')
            print('1 - Lista centrów konferencyjnych')
            print('2 - Lista klientów')
            print('3 - Lista pracowników')
            menu_option = input('Wybierz jedną z opcji: ')
            if menu_option == '0':
                break
            elif menu_option == '1':
                while True:
                    print('0 - Powrót do menu głównego')
                    print('1 - Wyświetl obecną listę centrów konferencyjnych')
                    print('2 - Dodaj centrum konferencyjne')
                    print('3 - Usuń centrum konferencyjne')
                    print('4 - Aktualizuj centrum konferencyjne')
                    działanie = input('Jakie działanie chcesz podjąć?: ')
                    if działanie == '0':
                        break
                    elif działanie == '1':
                        show_list(centres)
                    elif działanie == '2':
                        add_centre(centres)
                    elif działanie == '3':
                        remove_centre(centres)
                    elif działanie == '4':
                        update_centre(centres)
                    else:
                        print('Niepoprawna opcja, spróbuj ponownie')


            elif menu_option == '2':
                while True:
                    print('0 - Powrót do menu głównego')
                    print('1 - Wyświetl listę klientów danego centrum konferencyjnego')
                    print('2 - Wyświetl listę wszystkich klientów')
                    print('3 - Dodaj klienta do centrum konferencyjnego')
                    print('4 - Usuń klienta z centrum konferencyjnego')
                    print('5 - Aktualizuj nazwę klienta')
                    print('6 - Wyświetl rezerwację danego klienta')
                    print('7 - Dodaj rezerwację do klienta')
                    print('8 - Usuń rezerwację klienta')
                    print('9 - Aktualizuj rezerwację klienta')
                    działanie = input("Jakie działanie chcesz podjać?: ")
                    if działanie == '0':
                        break
                    elif działanie == '1':
                        show_clients(centres)
                    elif działanie == '2':
                        show_all_clients(centres)
                    elif działanie == '3':
                        add_client(centres)
                    elif działanie == '4':
                        remove_client(centres)
                    elif działanie == '5':
                        update_client(centres)
                    elif działanie == '6':
                        show_reservations(centres)
                    elif działanie == '7':
                        add_reservation(centres)
                    elif działanie == '8':
                        remove_reservation(centres)
                    elif działanie == '9':
                        update_reservation(centres)
                    else:
                        print('Niepoprawna opcja, spróbuj ponownie')


            elif menu_option == '3':
                while True:
                    print('0 - Powrót do menu głównego')
                    print('1 - Wyświetl listę pracowników danego centrum konferencyjnego')
                    print('2 - Wyświetl listę wszystkich pracowników')
                    print('3 - Dodaj pracownika do centrum konferencyjnego')
                    print('4 - Usuń pracownika z centrum konferencyjnego')
                    print('5 - Aktualizuj pracownika')
                    działanie = input("Jakie działanie chcesz podjąć?: ")

                    if działanie == '0':
                        break
                    elif działanie == '1':
                        show_employees(centres)
                    elif działanie == '2':
                        show_all_employees(centres)
                    elif działanie == '3':
                        add_employee(centres)
                    elif działanie == '4':
                        remove_employee(centres)
                    elif działanie == '5':
                        update_employee(centres)
                    else:
                        print('Niepoprawna opcja, spróbuj ponownie')
