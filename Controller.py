
from datetime import datetime
from Model import Note, NoteModel
from View import NoteView

class NoteController:
    def __init__(self):
        self.model = NoteModel()
        self.view = NoteView()

    def create_note(self):
        title, body = self.view.input_note_data()
        note_id = len(self.model.notes) + 1
        created_at = datetime.now()
        last_modified = created_at
        note = Note(note_id, title, body, created_at, last_modified)
        self.model.add_note(note)
        self.view.show_message("Заметка создана!")

    def list_notes(self):
        notes = self.model.get_notes()
        self.view.show_notes(notes)

    def view_note_details(self):
        note_id = self.view.input_note_id()
        note = self.model.get_note_by_id(int(note_id))
        if note:
            self.view.show_note_details(note)
        else:
            self.view.show_message("Не найдено.")

    def edit_note(self):
        note_id = self.view.input_note_id()
        note = self.model.get_note_by_id(int(note_id))
        if note:
            title, body = self.view.input_note_data()
            self.model.update_note(note.note_id, title, body)
            self.view.show_message("Заметка обновлена!")
        else:
            self.view.show_message("Не найдено.")

    def delete_note(self):
        note_id = self.view.input_note_id()
        self.model.delete_note(int(note_id))
        self.view.show_message("Заметка удалена!")

    def run(self):
        while True:
            self.view.show_message("1. Создать заметку\n2. Посмотреть список\n3. Посмотреть детали заметки\n4. Редактировать\n5. Удалить\n6. Выход")
            choice = input("Введите команду: ")

            if choice == "1":
                self.create_note()
            elif choice == "2":
                self.list_notes()
            elif choice == "3":
                self.view_note_details()
            elif choice == "4":
                self.edit_note()
            elif choice == "5":
                self.delete_note()
            elif choice == "6":
                break
            else:
                self.view.show_message("Ошибка. Введите команду еще раз.")

if __name__ == "__main__":
    controller = NoteController()
    controller.run()

