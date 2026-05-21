import os
from datetime import datetime
from json import load as json_load
from posixpath import dirname


class FileHandler:
	def __init__(self):
		self.input_files = []
		self.output_files = []

	def __call__(self, input_files, output_files):
		self.input_files = input_files
		self.output_files = output_files

	def handle_json(self, filename):
		with open(filename, 'r') as input_file:
			files_map = json_load(input_file)

		for key, value in files_map.items():
			reference_path = filename
			reference_dir = os.path.dirname(reference_path)

			input_path_join = os.path.join(reference_dir, key)
			output_path_join = os.path.join(reference_dir, value)

			input_path = os.path.abspath(input_path_join)
			output_path = os.path.abspath(output_path_join)

			self.input_files.append(input_path)
			self.output_files.append(output_path)

	def write_table(self, table, output_file):
		file_name = os.path.splitext(os.path.basename(output_file))[0]

		if not self._check_differences(table, output_file):
			return False

		sep = '\t' * 8
		timestamp = f"Last Update: {datetime.now().strftime('%Y-%m-%d - %H:%M:%S')}"

		with open(output_file, 'w', encoding='utf-8') as output_file_write:
			output_file_write.write(f"{file_name}{sep}{timestamp}\n\n\n")
			output_file_write.write(table)

		return True

	def _check_differences(self, table, output_file):
		with open(output_file, 'r', encoding='utf-8') as output_file:
			old_table = output_file.read().partition('\n\n\n')[2]

		if old_table != table:
			return True

		return False
	
	# @staticmethod
	# def check_file(file_to_check, optional=False, is_output=False):
	# 	if optional and file_to_check.strip() == "":
	# 		return None
		
	# 	file_to_check = file_to_check.strip().strip(f'"')
	# 	if not is_output and not os.path.isfile(file_to_check):
	# 		raise FileNotFoundError(f"File not found: {file_to_check}")
		
	# 	if is_output:
	# 		file_dir = os.path.dirname(file_to_check)
	# 		os.makedirs(file_dir, exist_ok=True)

	# 	return os.path.abspath(file_to_check)


	# @staticmethod
	# def check_directory(dir_to_check, optional=False, is_output=False):
	# 	if optional and dir_to_check.strip() == "":
	# 		return None
		
	# 	dir_to_check = dir_to_check.strip().strip(f'"')
	# 	if not os.path.isdir(dir_to_check):
	# 		return None
		
	# 	if is_output:
	# 		os.makedirs(dir_to_check, exist_ok=True)

	# 	return os.path.abspath(dir_to_check)
	

	@staticmethod
	def check_file(file_to_check):
		file_to_check = file_to_check.strip().strip(f'"')
		if not os.path.isfile(file_to_check):
			raise FileNotFoundError(f"File not found: {file_to_check}")

		return os.path.abspath(file_to_check)
	
	@staticmethod
	def check_directory(dir_to_check):
		dir_to_check = dir_to_check.strip().strip(f'"')
		if not os.path.isdir(dir_to_check):
			raise NotADirectoryError(f"Directory not found: {dir_to_check}")

		return os.path.abspath(dir_to_check)
	
	@staticmethod
	def get_user_input(is_directory=False):
		while True:
			user_input = input(f"{'Directory' if is_directory else 'File'} Path: ")

			if is_directory:
				checked_input = FileHandler.check_directory(user_input)
				return checked_input
			else:
				checked_input = FileHandler.check_file(user_input)
				return checked_input
			
	@staticmethod
	def write_output(output_file, content):
		with open(output_file, 'w', encoding='utf-8') as fw:
			fw.write(content)

	@staticmethod
	def write_output_folder(output_dir, output_map):
		FileHandler.check_directory(os.path.dirname(output_dir))
		os.makedirs(output_dir, exist_ok=True)
		
		for output_file, content in output_map.items():
			FileHandler.write_output(output_file, content)
			

# INPUT YES | OUTPUT PRINTED						        --> Ranker Utilities & Music Utilities Print
# INPUT YES | OUTPUT FILE (folder exists, file maybe)		--> Ranker Utilities Write
# INPUT YES | OUTPUT FOLDER (upper must exist, curr maybe)	--> Music Utilities Write
# INPUT NO  | OUTPUT PRINTED								--> Ranking Print
# INPUT NO  | OUTPUT FILE (folder exists, file maybe)		--> Ranking Write