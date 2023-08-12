from datetime import datetime


class Note:
    def __init__(self, note_id, title, body, created_at, last_modified):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_at = created_at
        self.last_modified = last_modified

class NoteModel:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def get_notes(self):
        return self.notes

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None

    def update_note(self, note_id, title, body):
        note = self.get_note_by_id(note_id)
        if note:
            note.title = title
            note.body = body
            note.last_modified = datetime.now()

    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)

