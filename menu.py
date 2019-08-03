import sys
from notebook import Note 
from notebook import Notebook 

class Menu:
	'''Display a menu and respond to choices'''
	def __init__(self):
		self.notebook = Notebook()

		self.choices = {
			'1' : self.show_notes,
			'2' : self.search_notes,
			'3' : self.add_notes,
			'4' : self.modify_notes,
			'5' : self.quit,
		}

	def display(self):
		print('''
			Menu :
			1. Show Notes
			2. Search Notes
			3. Add Notes
			4. Modify
			5. Quit''')

	def run(self):
		'''Display menu, enter choice and get result'''
		while True:
			self.display()
			self.choice = input('Enter choice : ')
			action = choices.get(choice)
			if action:
				action()
			else:
				print('{} is not valid'.format(choice))

	def show_notes(self, notes = None):
		if not notes:
			notes = self.notebook.notes

		for note in notes:
			print('{0} : {1}\n{2}'.format(
				note_id, tags, memo))

	def search_notes(self):
		filter = input('Search for : ')
		notes = self.notebook.search(filter)
		self.show_notes(notes)

	def add_notes(self):
		memo = input('Enter memo : ')
		self.notebook.new_note(memo)
		print('Your memo has been added')

	def modify_notes(self):
		note_id = int(input('Enter note id :'))
		memo = input('Enter new memo : ')
		tags = input('Enter tags : ')
		if memo:
			self.notebook.modify_memo(note_id, memo)
		if tags:
			self.notebook.modify_tags(note_id, tags)

	def quit(self):
		print('End of notebook')
		sys.exit(0)

if __name__ == '__main__':
	Menu().run()