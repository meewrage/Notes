
class NoteView:
    def show_notes(self, notes):
        for note in notes:
            print(f"ID: {note.note_id}, Title: {note.title}, Created: {note.created_at}")

    def show_note_details(self, note):
        print(f"ID: {note.note_id}\nTitle: {note.title}\nBody: {note.body}\nCreated: {note.created_at}\nLast Modified: {note.last_modified}")

    def input_note_data(self):
        title = input("Введите заголовок: ")
        body = input("Введите содержание: ")
        return title, body

    def input_note_id(self):
        return input("Введите ID заметки: ")

    def show_message(self, message):
        print(message)
