import csv
from connect import connect

def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                cur.execute(
                    "INSERT INTO contacts (name, phone) VALUES (%s, %s) ON CONFLICT (name) DO NOTHING",
                    (row['name'], row['phone'])
                )
            except Exception as e:
                print("Error inserting:", e)

    conn.commit()
    cur.close()
    conn.close()
    print("CSV data inserted.")


def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s) ON CONFLICT (name) DO NOTHING",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Contact added.")


def update_contact():
    name = input("Enter name to update: ")
    new_name = input("Enter new name (leave blank to skip): ")
    new_phone = input("Enter new phone (leave blank to skip): ")

    conn = connect()
    cur = conn.cursor()

    if new_name:
        cur.execute("UPDATE contacts SET name=%s WHERE name=%s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE contacts SET phone=%s WHERE name=%s", (new_phone, name))

    conn.commit()
    cur.close()
    conn.close()
    print("Contact updated.")


def query_contacts():
    print("1. Show all")
    print("2. Search by name")
    print("3. Search by phone prefix")

    choice = input("Choose: ")

    conn = connect()
    cur = conn.cursor()

    if choice == "1":
        cur.execute("SELECT * FROM contacts")

    elif choice == "2":
        name = input("Enter name: ")
        cur.execute("SELECT * FROM contacts WHERE name ILIKE %s", (f"%{name}%",))

    elif choice == "3":
        prefix = input("Enter prefix: ")
        cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", (f"{prefix}%",))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def delete_contact():
    print("1. Delete by name")
    print("2. Delete by phone")

    choice = input("Choose: ")

    conn = connect()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter name: ")
        cur.execute("DELETE FROM contacts WHERE name=%s", (name,))
    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM contacts WHERE phone=%s", (phone,))

    conn.commit()
    cur.close()
    conn.close()
    print("Deleted.")


def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Import from CSV")
        print("2. Add contact")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete contact")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_csv("contacts.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            query_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()