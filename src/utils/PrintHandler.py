import os


class PrintHandler:
	_GREEN = '\033[92m'
	_YELLOW = '\033[93m'
	_RED = '\033[91m'
	_CYAN = '\033[96m'
	_BLUE = '\033[94m'
	_RESET = '\033[0m'

	def __init__(self, output_obj='Result'):
		self.resume = {}
		self.output_obj = output_obj
		if self.output_obj == 'Table':
			self.print_result = self.print_table

	@staticmethod
	def generic_print(arg):
		print(f'{arg}')

	@staticmethod
	def colored_print(arg):
		print(f'{PrintHandler._RED}{arg}{PrintHandler._RESET}')

	def print_table(self, table):
		print(f"\nComputed {self.output_obj}:\n\n{table}\n")

	def print_result(self, result):
		print(f"\nComputed {self.output_obj}:\n\n{result}\n")

	def print_status(self, input_file, output_file, result, status, is_written=False):
		if status == None:
			pass
		elif status == 0:
			PrintHandler._print_status_created(self, input_file, output_file, result)
		elif status == 1:
			PrintHandler._print_status_updated(self, input_file, result)
		elif status == 2:
			PrintHandler._print_status_unchanged(self, output_file, result)
		elif status == 3:
			PrintHandler._print_status_user_skipped(self, input_file)
		else:
			PrintHandler._print_status_skipped(self, input_file)
		
		print(f"{self._GREEN if is_written else self._YELLOW}{self.output_obj if is_written else 'Nothing'} written{self._RESET} to {output_file}")

	def _print_status_created(self, input_file, output_file, result):
		print(f"{output_file} not found. Creating...")
		print(f"{self._CYAN}Computing{self._RESET} {self.output_obj} for {input_file}...")
		self.print_result(result)	

	def _print_status_updated(self, input_file, result):
		print(f"{self._GREEN}Computing{self._RESET} {self.output_obj} for {input_file}...")
		self.print_result(result)

	def _print_status_unchanged(self, output_file, result):
		print(f"{os.path.basename(output_file)} {self._YELLOW}has not changed{self._RESET}, there is no need to update the file.")
		self.print_result(result)

	def _print_status_user_skipped(self, output_file):
		print(f"{self._RED}Did not write{self._RESET} {self.output_obj} in {os.path.basename(output_file)}. Skipping...\n")
	
	def _print_status_skipped(self, input_file):
		print(f"File {os.path.basename(input_file)} does not exist or {self._BLUE}unknown error{self._RESET}. Skipping...\n")

	@staticmethod
	def print_separator(symbol='_'):
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

