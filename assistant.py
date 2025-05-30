# assistant.py

from tinydb import TinyDB, Query

# Create (or open) a database file called data.json
db = TinyDB('data.json')

# Create tables (collections) inside our database
birthdays_table = db.table('birthdays')
meetings_table = db.table('meetings')

def add_birthday(name, relation, date):
    """Add a birthday with name, relation, and date."""
    birthdays_table.insert({'name': name, 'relation': relation, 'date': date})
    print(f"✅ Birthday for {name} ({relation}) saved as {date}")


def get_birthday(name):
    """Retrieve birthday of a person from the database."""
    Person = Query()
    result = birthdays_table.search(Person.name == name)
    if result:
        person = result[0]
        print(f"🎉 Your ({person['relation']}), {person['name']}'s birthday is on {person['date']}")
    else:
        print(f"❌ No birthday found for {name}")


def add_meeting(title, date):
    """Add a meeting entry to the database."""
    meetings_table.insert({'title': title, 'date': date})
    print(f"📅 Meeting '{title}' saved for {date}")

def get_meetings(date):
    """Retrieve meetings scheduled for a particular date."""
    Meeting = Query()
    result = meetings_table.search(Meeting.date == date)
    if result:
        print(f"📌 Meetings on {date}:")
        for m in result:
            print(f" - {m['title']}")
    else:
        print(f"🛌 No meetings scheduled on {date}")
def delete_birthday(name):
    """Delete a birthday entry by name."""
    Person = Query()
    deleted = birthdays_table.remove(Person.name == name)
    if deleted:
        print(f"🗑️ Birthday for {name} has been deleted.")
    else:
        print(f"❌ No birthday found for {name}.")

def delete_meeting(title, date):
    """Delete a meeting by title and date."""
    Meeting = Query()
    deleted = meetings_table.remove((Meeting.title == title) & (Meeting.date == date))
    if deleted:
        print(f"🗑️ Meeting '{title}' on {date} has been deleted.")
    else:
        print(f"❌ No meeting found with title '{title}' on {date}.")

# Simple interaction..

if __name__ == "__main__":
    print("🤖 Welcome to your Personal AI Secretary!")
    print(" - exit, if you are not adding anything changes.")

    while True:
        user_input = input("🧠 You: ")

        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        parts = user_input.split()

        if len(parts) < 2:
            print("❗ Invalid command. Try again.")
            continue

        command, action = parts[0], parts[1]

        if command == "birthday":
            if action == "add":
                name = input("👤 Who is the birthday for? ")
                relation = input("🤝 What is their relation to you? (e.g., Mom, Friend, Boss): ")
                date = input("📅 What is their birth date? (e.g., May 5): ")
                add_birthday(name, relation, date)
            elif action == "get":
                name = input("👤 Whose birthday do you want to get? ")
                get_birthday(name)
            elif action == "delete":
                name = input("👤 Whose birthday do you want to delete? ")
                delete_birthday(name)
            else:
                print("❗ Invalid birthday command. Use add, get, delete.")

        elif command == "meeting":
            if action == "add":
                title = input("📌 What is the meeting title? ")
                date = input("📅 When is the meeting? (e.g., 2025-04-15): ")
                add_meeting(title, date)
            elif action == "get":
                date = input("📌 What is the date of the meeting to get? ")
                get_meetings(date)
            elif action == "delete":
                title = input("📌 What is the title of the meeting to delete? ")
                date = input("📅 What is the date of the meeting to delete? (e.g., 2025-04-14): ")
                delete_meeting(title, date)
            else:
                print("❗ Invalid meeting command.")

        else:
            print("❓ Unknown command.  Use add, get, delete.")

