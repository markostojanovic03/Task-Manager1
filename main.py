import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"

#Ucitavanje podataka iz json-a
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)
#Pisanje iz liste nazad u json file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f , indent=4)
# Meni za korisnika
def show_menu():
    print("\n -- Task Manager --")
    print("1. Prikazi zadatke")
    print("2. Dodaj zadatke")
    print("3. Izbrisi zadatak")
    print("4. Oznaci zadatak kao zavrsen")
    print("5. Oznaci zadatak kao nezavrsen")
    print("6. Izlaz")
#Ispis svih zadataka
def list_tasks(tasks):
    if not tasks:
        print("Nema zadataka")
        return
    for i, task in enumerate(tasks, 1):
        status = "✔" if task.get("completed") else "✘"
        print(f"{i}. {task.get('title')} | Rok: {task.get('deadline')} | Prioritet: {task.get('priority')} [{status}]")

#Glavna petlja
if __name__ == "__main__":
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Izaberi opciju: ")
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            title = input("Unesi naziv zadatka: ")
            while True:
                deadline = input("Unesi rok (YYYY-MM-DD): ")
                try:
                    datetime.strptime(deadline, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Nevažeći datum! Pokušaj ponovo (format: YYYY-MM-DD).")

            while True:
                priority = input("Unesi prioritet (visok, srednji, nizak): ").lower()
                if priority  in ("visok", "srednji", "nizak"):
                    break
                print("Nevazeci prioritet! Pokusaj ponovo.")

            tasks.append({"title": title,
                          "priority": priority,
                          "deadline": deadline,
                          "completed": False
                          })
            save_tasks(tasks)
            print("Zadatak dodat.")
        elif choice == "3":
            list_tasks(tasks)
            index = int(input("Unesi redni broj zadatka koji zelis da obrises: ")) - 1
            if 0 <= index < len(tasks):
                deleted = tasks.pop(index)
                save_tasks(tasks)
                print("Zadatak obrisan.")
            else:
                print("Neispravan broj zadatka")
        elif choice == "4":
            list_tasks(tasks)
            index = int(input("Unesi redni broj zadatka koji zelis da oznacis da je zavrsen: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["completed"] = True
                save_tasks(tasks)
                print("Zadatak oznacen kao zavrsen.")
            else:
                print("Neispravan broj zadatka")
        elif choice == "5":
            list_tasks(tasks)
            index = int(input("Unesi broj zadatka za označavanje kao nezavršen: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["completed"] = False
                save_tasks(tasks)
                print("Zadatak označen kao nezavršen.")
                list_tasks(tasks)
            else:
                print("Neispravan broj zadatka.")
        elif choice == "6":
            print("Izlaz iz programa.")
            break
        else:
            print("Nepoznata opcija! Probaj opet.")


