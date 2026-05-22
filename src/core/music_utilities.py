import os
import re

from ..utils.FileHandler import FileHandler
from .core_consts import FOLDERS_TO_PLAYLISTS_FOLDER, PLAYLISTS_FIXER_FOLDER


def folders_to_playlists(input_folder=None, write_output=False):
	if input_folder is None:
		checked_input_folder = FileHandler.get_user_input(is_directory=True)
		write_output = FileHandler.get_user_bool("Write Output?")
	else:
		checked_input_folder = FileHandler.check_directory(input_folder)

	result = {}

	for root, _, files in os.walk(checked_input_folder):
		
		if root == checked_input_folder:
			continue

		sub = os.path.basename(root)
		output_file_path = os.path.join(FOLDERS_TO_PLAYLISTS_FOLDER, f"{sub}.m3u8")
		result[output_file_path] = "#EXTM3U\n"
		result[output_file_path] += f"#{sub}\n\n"

		for file in files:
			abs_path = os.path.abspath(os.path.join(root, file))
			fixed_path = re.sub(r'(:(.+?((\\\\)(\\\\)))(.+?((\\\\)(\\\\)))|:(.+?[(\\\\)(\\/)])(.+?[(\\\\)(\\/)]))', lambda m: m.group(1).lower(), abs_path)
			result[output_file_path] += f"{fixed_path}\n"
		result[output_file_path] += "\n"

	if write_output:
		FileHandler.write_output_folder(FOLDERS_TO_PLAYLISTS_FOLDER, result)
	print("\n".join(result.values()))	#TODO: PrintHandler
	return result


def fix_playlists(input_folder=None, write_output=False, pattern=None, replacement=None, in_place=False):
	if input_folder is None:
		checked_input_folder = FileHandler.get_user_input(is_directory=True)
		write_output = FileHandler.get_user_bool("Write Output?")
	else:
		checked_input_folder = FileHandler.check_directory(input_folder)

	if not in_place and write_output:
		in_place = FileHandler.get_user_bool("In Place?")

	m_output_folder = checked_input_folder if in_place else PLAYLISTS_FIXER_FOLDER

	if pattern is None:
		pattern = input("Regex Pattern: ")
	if replacement is None:
		replacement = input("Replacement: ")

	regex = re.compile(pattern)

	result = {}
	result_new = {}

	for name in os.listdir(checked_input_folder):
		path = os.path.join(checked_input_folder, name)

		if not os.path.isfile(path):
			continue

		with open(path, "r", encoding="utf-8") as f:
			content = f.read()

		result_path = path if in_place else os.path.join(m_output_folder, name)
		result[result_path] = content
		new_content = regex.sub(replacement, content)
		result_new[result_path] = new_content

	if list(result.values()) == list(result_new.values()):
		print("\nNo Files Affected\n")	#TODO: PrintHandler
		return result
	
	if write_output:
		FileHandler.write_output_folder(m_output_folder, result_new)
	print("\n".join(result_new.values()))	#TODO: PrintHandler
	return result_new

