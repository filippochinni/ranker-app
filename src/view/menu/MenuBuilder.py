from .MenuObject import MenuObject


class MenuBuilder:
	def __init__(self):
		pass

	def print_menu(self, menu: MenuObject):
		print(f"--- {menu.name} ---")
		for i in range(len(menu.options[:-1])):
			print(f"{i+1}.\t\t\t{menu.options[i].name}")
		print(f"\n0.\t\t\t{menu.options[-1].name}")