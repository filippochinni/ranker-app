import os


class PrintHandler:
	_GREEN = '\033[92m'
	_YELLOW = '\033[93m'
	_RED = '\033[91m'
	_CYAN = '\033[96m'
	_BLUE = '\033[94m'
	_RESET = '\033[0m'

	def __init__(self):
		self.resume = {}

	@staticmethod
	def generic_print(arg):
		print(f'{arg}')
		
	@staticmethod
	def print_table(table):
		print(f"\nComputed Table:\n\n{table}\n")

	@staticmethod
	def print_if_written(output_file, was_written):
		if was_written:
			print(f"Table written to {output_file}")
		else:
			print(f"Nothing written to {output_file}")

	@staticmethod
	def print_status(input_file, output_file, table, status):
		if not status:
			pass
		elif status == 0:
			PrintHandler._print_status_created(input_file, output_file, table)
		elif status == 1:
			PrintHandler._print_status_updated(input_file, table)
		elif status == 2:
			PrintHandler._print_status_unchanged(output_file, table)
		else:
			PrintHandler._print_status_skipped(input_file)

	def _print_status_created(input_file, output_file, table):
		print(f"{output_file} not found. Creating...")
		print(f"Computing table for {input_file}...")
		PrintHandler.print_table(table)	

	def _print_status_updated(input_file, table):
		print(f"Computing table for {input_file}...")
		PrintHandler.print_table(table)

	def _print_status_unchanged(output_file, table):
		print(f"{os.path.basename(output_file)} has not changed, there is no need to update the file.")
		PrintHandler.print_table(table)

	def _print_status_skipped(input_file):
		print(f"File {os.path.basename(input_file)} does not exist and user did not write. Skipping...\n")

	@staticmethod
	def print_separator(symbol='/'):
		print(f"\n{symbol * 120}\n\n")

	def update_resume(self, output_file, status):
		self.resume[os.path.basename(output_file)] = status

	def print_resume(self):
		padding = max([len(key) for key in self.resume.keys()]) + 5

		print("Resume:\n")
		for key, value in self.resume.items():
			if value == None:
				print(f"{key:<{padding}} --> \t{self._BLUE}None{self._RESET}")
			elif value == 0:
				print(f"{key:<{padding}} --> \t{self._CYAN}Created{self._RESET}")
			elif value == 1:
				print(f"{key:<{padding}} --> \t{self._GREEN}Updated{self._RESET}")
			elif value == 2:
				print(f"{key:<{padding}} --> \t{self._YELLOW}Unchanged{self._RESET}")
			else:
				print(f"{key:<{padding}} --> \t{self._RED}Skipped{self._RESET}")
		print("")

