'''Build a notebook app
 
Primary objective - 
learning OOP design concept
learning python syntax.'''

import datetime

last_page = 0

class Note:
    '''Note object contains'
relevant tags and text
a match method provides lower
level of search.'''

    def __init__(self, memo, tags):
        self.tags = tags
        self.memo = memo
        self.date = datetime.date.today()

        global last_page
        last_page += 1
        
        self.page = last_page

    def match(self, filters):
        return filters in self.memo or filters in self.tags

class Notebook():
    '''Notebook is a collection
of Notes. methods to make notes,
find by page, search by tags and
to edit a note.'''

    def __init__(self):
        self.notes = []

    def make_note(self, memo, tags):
        self.notes.append(Note(memo, tags))

    def _find_note(self, search_page):
        if len(self.notes) < int(search_page):
            return self.notes[search_page - 1]
        return None

    def modify_memo(self, search_id, memo):
        note = self._find_note(search_id)
        if note:
            note.memo = memo
            return True
        return False

    def search(self, filters):
        return [note for note in self.notes
                if note.match(filters)]

    
			
