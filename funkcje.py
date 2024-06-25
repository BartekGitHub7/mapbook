def show_list(centres):
    print('Aktualna lista centrów konferencyjnych: ')
    for centre in centres:
        print(f" {centre['name']}")

def add_centre(centres):
    centre = input('Podaj nazwę centrum do dodania: ')
    centres.append({'name': centre, 'clients': []})
    print(f"{centre} zostało dodane do listy")
    show_list(centres)

def remove_centre(centres):
    centre_name = input('Podaj nazwę centrum do usunięcia:')
    centre_found = False
    for centre in centres:
        if centre['name'] == centre_name:
            centres.remove(centre)
            centre_found = True
            print(f"{centre_name} zostało usunięte z listy")
            break
    if not centre_found:
        print(f"{centre_name} nie znaleziono")
    show_list(centres)

def update_centre(centres):
    old_name = input("Podaj nazwę centrum do aktualizacji: ")
    centre_found = False
    for centre in centres:
        if centre['name'] == old_name:
            new_name = input(f"Podaj nową nazwę dla {old_name}: ")
            centre['name'] = new_name
            centre_found = True
            print(f"Nazwa centrum została zmieniona z {old_name} na {new_name}")
            break
    if not centre_found:
        print(f"{old_name} nie znaleziono na liście")
    show_list(centres)

def show_clients(centres):
    centre_name = input("Podaj nazwę centrum, którego lista klientów ma zostać wyświetlona: ")
    centre_found = False
    for centre in centres:
        if centre['name'] == centre_name:
            print(f"Lista klientów dla {centre_name}: ")
            for client in centre['clients']:
                print(f" - {client['name']}")
            centre_found = True
            break
    if not centre_found:
        print(f"{centre_name} nie znaleziono na liście")


def show_all_clients(centres):
    print("Lista wszystkich klientów w centrach konferencyjnych:")
    for centre in centres:
        print(f"Centrum konferencyjne: {centre['name']}")
        if centre['clients']:
            print("Klienci:")
            for client in centre['clients']:
                print(f" - {client['name']}")
        else:
            print("Brak klientów.")
        print()


def add_client(centres):
    centre_name = input("Podaj nazwę centrum, do którego chcesz dodać klienta: ")
    centre_found = False
    for centre in centres:
        if centre['name'] == centre_name:
            guest_name = input(f"Podaj nazwę klienta do dodania do {centre_name}: ")
            centre['clients'].append({'name': guest_name, 'reservation': []})
            print(f"{guest_name} został dodany do listy klientów {centre_name}")
            centre_found = True
            break
    if not centre_found:
        print(f"{centre_name} nie znaleziono na liście")


def remove_client(centres):
    centre_name = input('Podaj nazwę centrum, z któego chcesz usunąć klienta: ')
    centre_found = False
    for centre in centres:
        if centre['name'] == centre_name:
            client_name = input(f"Podaj nazwę klienta do usunięcia z {centre_name}: ")
            for client in centre['clients']:
                if client['name'] == client_name:
                    centre['clients'].remove(client)
                    print(f"{client_name} został usunięty z listy klientów {centre_name}")
                    centre_found = True
                    break
            if not centre_found:
                print(f"{client_name} nie znaleziono na liście")
            break
    if not centre_found:
        print(f"{centre_name} nie znaleziono na liście")

def update_client(centres):
    centre_name = input('Podaj nazwę centrum, w którym chcesz zaktualizować nazwę klienta: ')
    centre_found = False
    for centre in centres:
        if centre['name'] == centre_name:
            old_client_name = input(f"Podaj nazwę klienta do zaktualizowania w {centre_name}: ")
            for client in centre['clients']:
                if client['name'] == old_client_name:
                    new_guest_name = input(f"Podaj nową nazwę dla {old_client_name}: ")
                    client['name'] = new_guest_name
                    print(f"Nazwa klienta została zmieniona z {old_client_name} na {new_guest_name}")
                    centre_found = True
                    break
            if not centre_found:
                print(f"{old_client_name} nie znaleziono na liście")
            break
    if not centre_found:
        print(f"{centre_name} nie znaleziono na liście")


def show_reservations(centres):
    client_name = input("Podaj imię klienta, którego rezerwacje chcesz wyświetlić: ")
    client_found = False
    for centre in centres:
        for client in centre['clients']:
            if client['name'] == client_name:
                if client['reservation']:
                    print(f"Rezerwacje dla {client_name}: ")
                    for reservation in client['reservation']:
                        print(f" - {reservation}")
                    client_found = True
                break
        if client_found:
            break
    if not client_found:
        print(f"Klient o imieniu {client_name} nie został znaleziony w żadnym centrum konferencyjnym.")


def add_reservation(centres):
    client_name = input("Podaj nazwę klienta, do którego chcesz dodać rezerwację: ")
    centre_name = input("Podaj nazwę centrum, do którego chcesz dodać rezerwację: ")

    centre_found = False
    client_found = False

    for centre in centres:
        for client in centre['clients']:
            if client['name'] == client_name:
                client_found = True
                if centre_name not in client['reservation']:
                    client['reservation'].append(centre_name)
                break

    if not client_found:
        for centre in centres:
            if centre['name'] == centre_name:
                centre['clients'].append({'name': client_name, 'reservation': [centre_name]})
                client_found = True
                break

    if not client_found:
        print(f"Nie znaleziono klienta o nazwie {client_name} ani centrum o nazwie {centre_name}")
    else:
        print(f"Rezerwacja w {centre_name} została dodana dla {client_name}")

    if not centre_found and client_found:
        for centre in centres:
            if centre['name'] == centre_name:
                centre['clients'].append({'name': client_name, 'reservation': [centre_name]})
                break



def remove_reservation(centres):
    centre_name = input("Podaj nazwę centrum, z którego chcesz usunąć rezerwację: ")
    client_name = input("Podaj nazwę klienta: ")

    centre_found = False
    client_found = False

    for centre in centres:
        if centre['name'] == centre_name:
            centre_found = True
            for client in centre['clients']:
                if client['name'] == client_name:
                    client_found = True
                    if centre_name in client['reservation']:
                        client['reservation'].remove(centre_name)
                        print(f"Rezerwacja w {centre_name} została usunięta dla {client_name}")
                    else:
                        print(f"Nie znaleziono rezerwacji dla {client_name} w {centre_name}")
                    break

            if client_found and not client['reservation']:
                centre['clients'].remove(client)
                print(f"Klient {client_name} został usunięty z listy klientów {centre_name}, ponieważ nie ma innych rezerwacji")
            break

    if not centre_found:
        print(f"{centre_name} nie znaleziono na liście")
    elif not client_found:
        print(f"Klient {client_name} nie znaleziono w {centre_name}")


def update_reservation(centres):
    client_name = input("Podaj nazwę klienta, dla którego chcesz zaktualizować rezerwację: ")
    old_centre_name = input("Podaj obecną nazwę centrum, w którym znajduje się rezerwacja: ")
    new_centre_name = input("Podaj nową nazwę centrum, do którego chcesz przenieść rezerwację: ")

    old_centre_found = False
    new_centre_found = False
    client_found = False

    for centre in centres:
        if centre['name'] == old_centre_name:
            old_centre_found = True
            for client in centre['clients']:
                if client['name'] == client_name:
                    client_found = True
                    if old_centre_name in client['reservation']:
                        client['reservation'].remove(old_centre_name)
                    break

        elif centre['name'] == new_centre_name:
            new_centre_found = True
            if not any(client['name'] == client_name for client in centre['clients']):
                centre['clients'].append({'name': client_name, 'reservation': [new_centre_name]})
            else:
                for client in centre['clients']:
                    if client['name'] == client_name:
                        if new_centre_name not in client['reservation']:
                            client['reservation'].append(new_centre_name)
                        break

        if old_centre_found and new_centre_found:
            break

    if old_centre_found and new_centre_found:
        print(f"Rezerwacja w {old_centre_name} dla {client_name} została zaktualizowana na {new_centre_name}")
        print(f"{client_name} został przeniesiony z {old_centre_name} do {new_centre_name}")
    else:
        if not old_centre_found:
            print(f"{old_centre_name} nie znaleziono na liście")
        if not new_centre_found:
            print(f"{new_centre_name} nie znaleziono na liście")

    if old_centre_found and client_found:
        for centre in centres:
            if centre['name'] == old_centre_name:
                for client in centre['clients']:
                    if client['name'] == client_name:
                        centre['clients'].remove(client)
                        print(f"{client_name} został usunięty z listy klientów {old_centre_name}")
                        break



def show_employees(centres):
    centre_name = input("Podaj nazwę centrum, którego lista pracowników ma zostać wyświetlona: ")
    centre_found = False
    for centre in centres:
        if centre['name'] == centre_name:
            print(f"Lista pracowników dla {centre_name}: ")
        for employee in centre.get('employees', []):
            print(f" - {employee['name']}")
            centre_found = True
        break
    if not centre_found:
        print(f"{centre_name} nie znaleziono na liście")



def show_all_employees(centres):
    print("Lista wszystkich pracowników we wszystkich centrach konferencyjnych:")
    for centre in centres:
        print(f"Centrum: {centre['name']}")
        if 'employees' in centre:
            for employee in centre['employees']:
                print(f" - {employee['name']}")

def add_employee(centres):
    centre_name = input("Podaj nazwę centrum, do którego chcesz dodać pracownika: ")
    centre_found = False
    for centre in centres:
        if centre['name'] == centre_name:
            employee_name = input(f"Podaj imię i nazwisko pracownika do dodania do {centre_name}: ")
            if any(employee['name'] == employee_name for employee in centre.get('employees', [])):
                print(f"Pracownik o imieniu {employee_name} już istnieje w {centre_name}")
            else:
                centre.setdefault('employees', []).append({"name": employee_name})
                print(f"{employee_name} został dodany do listy pracowników {centre_name}")
            centre_found = True
            break
    if not centre_found:
        print(f"{centre_name} nie znaleziono na liście")

def remove_employee(centres):
    centre_name = input("Podaj nazwę centrum, z którego chcesz usunąć pracownika: ")
    centre_found = False
    for centre in centres:
        if centre['name'] == centre_name:
            employee_name = input(f"Podaj imię i nazwisko pracownika do usunięcia z {centre_name}: ")
            for employee in centre.get('employees', []):
                if employee['name'] == employee_name:
                    centre['employees'].remove(employee)
                    print(f"{employee_name} został usunięty z listy pracowników {centre_name}")
                    centre_found = True
                    break
            if not centre_found:
                print(f"{employee_name} nie znaleziono na liście pracowników {centre_name}")
            break
    if not centre_found:
        print(f"{centre_name} nie znaleziono na liście")


def update_employee(centres):
    centre_name = input("Podaj nazwę centrum, w którym chcesz zaktualizować pracownika: ")
    centre_found = False
    for centre in centres:
        if centre['name'] == centre_name:
            employee_name = input(f"Podaj imię i nazwisko pracownika do zaktualizowania w {centre_name}: ")
            for employee in centre.get('employees', []):
                if employee['name'] == employee_name:
                    new_employee_name = input(f"Podaj nowe imię i nazwisko dla {employee_name}: ")
                    employee['name'] = new_employee_name
                    print(f"Imię pracownika zostało zmienione z {employee_name} na {new_employee_name}")
                    centre_found = True
                    break
            if not centre_found:
                print(f"{employee_name} nie znaleziono na liście pracowników {centre_name}")
            break
    if not centre_found:
        print(f"{centre_name} nie znaleziono na liście")
