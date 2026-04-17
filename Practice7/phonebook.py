from csv import DictReader
from connect import connect



conn = connect()
cur = conn.cursor()



def insert_from_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        reader = DictReader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s) ON CONFLICT (name) DO NOTHING",
                (row['name'], row['phone'])
            )
    conn.commit()
    print("CSV data inserted.")



def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s) ON CONFLICT (name) DO NOTHING",
        (name, phone)
    )
    conn.commit()
    print("Contact added.")



def update_contact():
    name = input("Enter name to update: ")
    new_name = input("Enter new name (leave blank to skip): ")
    new_phone = input("Enter new phone (leave blank to skip): ")
    if new_name:
        cur.execute("UPDATE contacts SET name=%s WHERE name=%s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE contacts SET phone=%s WHERE name=%s", (new_phone, name))
    conn.commit()
    print("Contact updated.")



def query_contacts():
    print("1. Show all")
    print("2. Search by name")
    print("3. Search by phone prefix")
    choice = input("Choose: ")
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



def delete_contact():
    print("1. Delete by name")
    print("2. Delete by phone")
    choice = input("Choose: ")
    if choice == "1":
        name = input("Enter name: ")
        cur.execute("DELETE FROM contacts WHERE name=%s", (name,))
    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM contacts WHERE phone=%s", (phone,))
    conn.commit()
    print("Deleted.")



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