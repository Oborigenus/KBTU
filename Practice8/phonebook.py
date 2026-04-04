from connect import connect

conn = connect()
cur = conn.cursor()

def upsert(name, phone):
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()

def search(pattern):
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def paginate(limit, offset):
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete(value):
    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()

def bulk_insert():
    names = ["Alice", "Bob", "Charlie"]
    phones = ["1234567890", "invalid", "9876543210"]

    cur.execute("CALL insert_many(%s, %s)", (names, phones))
    conn.commit()


while True:
    print("\n--- PHONEBOOK MENU ---")
    print("1. Insert/Update")
    print("2. Search")
    print("3. Paginate")
    print("4. Delete")
    print("5. Bulk Insert")
    print("0. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        upsert(name, phone)

    elif choice == "2":
        pattern = input("Search: ")
        search(pattern)

    elif choice == "3":
        limit = int(input("Limit: "))
        offset = int(input("Offset: "))
        paginate(limit, offset)

    elif choice == "4":
        value = input("Name or Phone: ")
        delete(value)

    elif choice == "5":
        bulk_insert()

    elif choice == "0":
        break