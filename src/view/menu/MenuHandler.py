import os

from .MenuBuilder import MenuBuilder
from .MenuObject import MAIN_MENU, MENU_LIST


class MenuHandler:
	def __init__(self):
		self.menu_builder = MenuBuilder()
		self.prev_menu_stack = []
		self.curr_menu = MAIN_MENU

	def start(self):
		while True:
			self._open_menu()
			user_input = input("\n")

			if not user_input.isdigit():
				continue

			user_input = int(user_input)

			if (user_input < 0) or (user_input >= len(self.curr_menu.options)):
				continue

			selected_option = self.curr_menu.options[user_input-1]

			if selected_option.is_submenu:
				self.prev_menu_stack.append(self.curr_menu)
				self.curr_menu = MENU_LIST[selected_option.name]
			elif selected_option.action is not None:
				selected_option.action()
				input()
			else:
				if len(self.prev_menu_stack) == 0:
					break
				self.curr_menu = self.prev_menu_stack.pop()

	def _open_menu(self):
		os.system("clear||cls")
		self.menu_builder.print_menu(self.curr_menu)