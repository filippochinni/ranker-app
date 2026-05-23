import os
import re

from ..utils.FileHandler import FileHandler
from ..utils.PrintHandler import PrintHandler
from .ranker_utilities import was_written_wizard, what_status_wizard
from .core_consts import FOLDERS_TO_PLAYLISTS_FOLDER, PLAYLISTS_FIXER_FOLDER


def folders_to_playlists(input_folder=None, write_output=False):
	if input_folder is None:
		checked_input_folder = FileHandler.get_user_input(is_directory=True)
	else:
		checked_input_folder = FileHandler.check_directory(input_folder)

	f_print_handler = PrintHandler()

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

	PrintHandler.generic_print("\n".join(result.values()))
	write_output = FileHandler.get_user_bool("Write Output?")

	if write_output:
		status_dict = FileHandler.write_output_folder(FOLDERS_TO_PLAYLISTS_FOLDER, result, check_diff=True)
	else:
		status_dict = {}
		for k, v in result.items():
			changed = FileHandler.check_differences_file(k, v)
			status = what_status_wizard(changed)
			status_dict[k] = status

	for k, v in status_dict.items():
		written = was_written_wizard(write_output, v)
		f_print_handler.print_status(checked_input_folder, k, result, v, is_written=written)
		f_print_handler.update_resume(k, v)
		PrintHandler.print_separator()
	f_print_handler.print_resume()
	PrintHandler.print_separator()
	return result


def fix_playlists(input_folder=None, write_output=False, pattern=None, replacement=None, in_place=False):
	if input_folder is None:
		checked_input_folder = FileHandler.get_user_input(is_directory=True)
	else:
		checked_input_folder = FileHandler.check_directory(input_folder)

	if pattern is None:
		pattern = input("Regex Pattern: ")
	if replacement is None:
		replacement = input("Replacement: ")
	regex = re.compile(pattern)

	f_print_handler = PrintHandler()
	PrintHandler.generic_print('')

	if not in_place:
		in_place = FileHandler.get_user_bool("In Place?")

	m_output_folder = checked_input_folder if in_place else PLAYLISTS_FIXER_FOLDER

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
		PrintHandler.colored_print("\nNo Files Affected.\n")
		return result
	
	PrintHandler.generic_print("\n".join(result_new.values()))
	write_output = FileHandler.get_user_bool("Write Output?")

	if write_output:
		status_dict = FileHandler.write_output_folder(m_output_folder, result_new, check_diff=True)
	else:
		status_dict = {}
		for k, v in result_new.items():
			changed = FileHandler.check_differences_file(k, v)
			status = what_status_wizard(changed)
			status_dict[k] = status

	for k, v in status_dict.items():
		written = was_written_wizard(write_output, v)
		f_print_handler.print_status(checked_input_folder, k, result_new, v, is_written=written)
		f_print_handler.update_resume(k, v)
		PrintHandler.print_separator()
	f_print_handler.print_resume()
	PrintHandler.print_separator()
	return result_new

