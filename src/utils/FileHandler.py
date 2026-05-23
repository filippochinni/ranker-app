import os
from datetime import datetime


_RANKING_SEP = '\n\n\n'

class FileHandler:
	def __init__(self):
		pass
	
	
	@staticmethod
	def check_file(file_to_check):
		file_to_check = file_to_check.strip().strip(f'"')
		if not FileHandler.check_file_exists(file_to_check):
			raise FileNotFoundError(f"File not found: {file_to_check}")

		return os.path.abspath(file_to_check)
	
	@staticmethod
	def check_directory(dir_to_check):
		dir_to_check = dir_to_check.strip().strip(f'"')
		if not os.path.isdir(dir_to_check):
			raise NotADirectoryError(f"Directory not found: {dir_to_check}")

		return os.path.abspath(dir_to_check)
	
	@staticmethod
	def check_file_exists(file_to_check):
		return os.path.isfile(file_to_check)

	@staticmethod
	def check_differences_file(existing_file, content, is_ranking=False):
		if not os.path.isfile(existing_file):
			return None
		
		with open(existing_file, 'r', encoding='utf-8') as existing_file:
			if is_ranking:
				old_content = existing_file.read().partition(_RANKING_SEP)[2]
			else:
				old_content = existing_file.read()

		if old_content != content:
			return True
		return False
	
	@staticmethod
	def get_user_input(is_directory=False):
		while True:
			user_input = input(f"\n{'Directory' if is_directory else 'File'} Path: ")
			print("\n")

			if is_directory:
				checked_input = FileHandler.check_directory(user_input)
				return checked_input
			else:
				checked_input = FileHandler.check_file(user_input)
				return checked_input
			
	@staticmethod
	def get_user_bool(prompt):
		while True:
			user_input = input(f"\n{prompt} (y/n): ").strip().lower()
			print("\n")
			if user_input == 'y':
				return True
			elif user_input == 'n':
				return False
			
	@staticmethod
	def write_output(output_file, content, check_diff=False):
		status = None
		do_write = True
		if not os.path.isfile(output_file):
			status = 0
		elif check_diff:
			do_write = FileHandler.check_differences_file(output_file, content)
			status = 1 if do_write else 2

		if do_write:
			with open(output_file, 'w', encoding='utf-8') as fw:
				fw.write(content)

		return status

	@staticmethod
	def write_output_folder(output_dir, output_map, check_diff=False):
		FileHandler.check_directory(os.path.dirname(output_dir))
		os.makedirs(output_dir, exist_ok=True)
		
		status_dict = {}
		for output_file, content in output_map.items():
			status_dict[output_file] = FileHandler.write_output(output_file, content, check_diff=check_diff)
		return status_dict

	@staticmethod
	def write_table(output_file, table, check_diff=False, is_ranking=False):
		status = None
		if not os.path.isfile(output_file):
			status = 0
		elif check_diff:
			if not FileHandler.check_differences_file(output_file, table, is_ranking=is_ranking):
				status = 2
				return status
			else:
				status = 1
		
		result = table
		if is_ranking:
			file_name = os.path.splitext(os.path.basename(output_file))[0]
			sep = '\t' * 8
			timestamp = f"Last Update: {datetime.now().strftime('%Y-%m-%d - %H:%M:%S')}"
			result = f"{file_name}{sep}{timestamp}{_RANKING_SEP}" + table

		FileHandler.write_output(output_file, result, check_diff=False)
		return status

