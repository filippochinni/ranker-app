from .view.cl.CLParser import CLParser
from .utils.FileHandler import FileHandler
from .utils.PrintHandler import PrintHandler
from .view.menu.MenuHandler import MenuHandler


def main():

	cl_parser = CLParser()
	file_handler = FileHandler()
	print_handler = PrintHandler()

	args = cl_parser()
	# cl_parser.print_namespace()

	if args.cl:
		print("CL INTERFACE NOT IMPLEMENTED YET")
		return
	
	menu_handler = MenuHandler()
	menu_handler.start()



if __name__ == '__main__':
	main()
