import sys
from notebook import Note, Notebook

class Menu:
    ''' menu to display and act as interface'''

    def __init__(self):
        self.notebook = Notebook()
        self.options = {
                '1' : self.show_notes,
                '2' : self.search_notes,
                '3' : self.add_note,
                '4' : self.modify_note,
                '5' : self.quit
            }

    def display_options(self):
        print("""
                Notebook options :

                1. Show all notes
                2. Search for notes
                3. Add note
                4. Modify note
                5. Quit """)

    def run(self):
        ''' Display the menu and run the options'''
        while True:
            self.display_options()
            choice = input('enter option : ')
            action = self.options.get(choice)
            if action :
                action()
            else :
                print('{} is an invalid option'.format(choice))

    def show_notes(self, notes=None):
        ''' Display the list of all notes.'''
        if not notes:
            notes = self.notebook.notes
            for note in notes:
                print('ID : {}'.format(note.page))
                print('tags : {}'.format(note.tags))
                print('memo : {}'.format(note.memo))

    def search_notes(self):
        ''' Search for notes according to the
    given keyword.'''
        filters = input('enter filter : ')
        notes = self.notebook.search(filters)
        self.show_notes(notes)

    def add_note(self):
        ''' add notes to the notebook.'''
        tags = input('enter tags : ')
        memo = input('enter memo : ')
        self.notebook.make_notebook(tags, memo)
        print('note has been added')

    def modify_note(self):
        search_id = input('Enter search ID : ')
        tags = input('Enter new tags : ')
        memo = input('Enter new memo : ')
        if tags:
            self.notebook.modify_tags(search_id, tags)
        if memo:
            self.notebook.modify_memo(search_id, memo)

    def quit(self):
        print('quit notebook')
        sys.exit(0)
        
if __name__ == '__main__':
    Menu().run()
        
