import os
import re
import csv

from ..utils.FileHandler import FileHandler
from ..utils.PrintHandler import PrintHandler
from .core_consts import INDEX_RANKING_FILE, PLAYLISTS_CSV_FILE, RANKING_MUSICA_CANZONI_INPUT, RANKING_MUSICA_ARTISTI_INPUT, RANKING_ARTISTI_BUILDING_FILE


def index_ranking(input_file=None, write_output=False, in_place=False):
	if input_file is None:
		checked_input_file = FileHandler.get_user_input()
	else:
		checked_input_file = FileHandler.check_file(input_file)

	f_print_handler = PrintHandler()

	result = ""	
	with open(checked_input_file, "r", encoding='utf-8') as fr:
		header = fr.readline()
		result += f'{header}\n'
		
		simple_counter = 0
		counter_map = {}
		for line in fr.readlines():
			if not line.strip():
				continue
			
			split_line = line.split(",")
			index_type, *_ = split_line
			
			if len(index_type) == 0:
				result += f'{line}'
				continue
			
			if index_type.isdigit():
				simple_counter += 1
				result += f'{",".join([str(simple_counter)] + _)}'
			else:
				prefix = list(index_type)[:-1]
				prefix = "".join(prefix)

				if not counter_map.get(prefix):
					counter_map[prefix] = 0
				counter_map[prefix] += 1
				
				updated_val = f'{prefix}{counter_map[prefix]}'
				result += f'{",".join([str(updated_val)] + _)}'
	
	PrintHandler.generic_print('\n')
	PrintHandler.generic_print(result)
	write_output = FileHandler.get_user_bool("Write Output?")

	if not in_place and write_output:
		in_place = FileHandler.get_user_bool("In Place?")

	m_output_file = checked_input_file if in_place else INDEX_RANKING_FILE

	if write_output:
		status = FileHandler.write_output(m_output_file, result, check_diff=True)
	else:
		changed = FileHandler.check_differences_file(m_output_file, result)
		status = what_status_wizard(changed)

	written = was_written_wizard(write_output, status)
	f_print_handler.print_status(checked_input_file, m_output_file, result, status, is_written=written)
	f_print_handler.update_resume(m_output_file, status)
	f_print_handler.print_resume()
	PrintHandler.print_separator('^')
	return result


BLACKLIST = {
	'Anime ED': '---',
	'Anime OP': '---',
	'Anime MOVIE': '---',
    'Anime Varie': '---',

    'Soundtrack 0': '---',
    'Soundtrack 1': '~2026-03',
	'Soundtrack LONG': '---',

	'Varie 0': '---',
	'Varie 1': '---',
	'Varie 2': '---',
	'Varie 3': '---',
    'Videogame Varie': '---'
}
WHITELIST = {
    'Playlist 001': '~2018-04',
	'Playlist 002': '~2019/08',
	'Playlist 003': '~2019/10',
	'Playlist 004': '~2019/12',
	'Playlist 005': '~2020/03',
	'Playlist 006': '~2020/05',
	'Playlist 007': '~2020/09',
	'Playlist 008 Pt.1': '~2021/03',
	'Playlist 008 Pt.2': '~2021/03',
	'Playlist 009': '~2021/07',
	'Playlist 010': '~2021/11',
	'Playlist 011 Pt.1': '~2022/04',
	'Playlist 011 Pt.2': '~2022/04',
	'Playlist 012': '~2022/09',
	'Playlist 013 Pt.1': '~2023/02',
	'Playlist 013 Pt.2': '~2023/02',
	'Playlist 014': '~2023/07',
	'Playlist 015 Pt.1': '~2023/09',
	'Playlist 015 Pt.2': '~2023/09',
	'Playlist 016': '~2024/03',
	'Playlist 017': '~2024/07',
	'Playlist 018': '~2024/11',
    'Playlist 019': '~2025-03',
    'Playlist 020': '~2026-03',
}

def playlists_to_csv(input_folder=None, write_output=False):
	if input_folder is None:
		checked_input_folder = FileHandler.get_user_input(is_directory=True)
	else:
		checked_input_folder = FileHandler.check_directory(input_folder)

	f_print_handler = PrintHandler()
	
	result = ""
	for filename in os.listdir(checked_input_folder):

		file_path = os.path.join(checked_input_folder, filename)
		if not os.path.isfile(file_path):
			continue
		
		filename = re.sub(r'\.[^.]+$', '', filename)
		if (filename not in WHITELIST) or (filename in BLACKLIST):
			continue

		with open(file_path, "r", encoding="utf-8") as f:

			f_lines = [s for s in f.readlines() if not s.startswith('#')]
			count = len(f_lines)
			for line in f_lines:
				line = line.strip()
				
				song_file = line.split("\\")[-1]
				
				parts_song, parts_artist = song_file.rstrip('.mp3').split(" - ")
				parts_playlist = filename
				parts_watch = WHITELIST[filename]
				parts_rel_rank = f'{count}°/{len(f_lines)}'
				
				csv_line = ['n', parts_song, parts_artist, '----', parts_watch, parts_playlist, parts_rel_rank]
				result += f'{to_csv_row(csv_line)}\n'
				
				count -= 1
		result += f'{to_csv_row([])}\n'
	
	PrintHandler.generic_print(result)
	write_output = FileHandler.get_user_bool("Write Output?")

	if write_output:
		status = FileHandler.write_output(PLAYLISTS_CSV_FILE, result, check_diff=True)
	else:
		changed = FileHandler.check_differences_file(PLAYLISTS_CSV_FILE, result)
		status = what_status_wizard(changed)

	written = was_written_wizard(write_output, status)
	f_print_handler.print_status(checked_input_folder, PLAYLISTS_CSV_FILE, result, status, is_written=written)
	f_print_handler.update_resume(PLAYLISTS_CSV_FILE, status)
	f_print_handler.print_resume()
	PrintHandler.print_separator()
	return result


def build_artists_data(write_output=False):
	FileHandler.check_file(RANKING_MUSICA_CANZONI_INPUT)
	FileHandler.check_file(RANKING_MUSICA_ARTISTI_INPUT)

	f_print_handler = PrintHandler()
	
	result_header = []
	with open(RANKING_MUSICA_ARTISTI_INPUT, 'r', encoding='utf-8', newline='') as csv_file:
		csv_reader = csv.reader(csv_file)
		result_header = next(csv_reader)
	
	result_dict = {}
	with open(RANKING_MUSICA_CANZONI_INPUT, 'r', encoding='utf-8', newline='') as csv_file:
		csv_reader = csv.reader(csv_file)
		for row in list(csv_reader)[1:]:
			if not row or not row[2]:
				continue
			temp_artist = row[2]
			temp_rank = row[0]
			if temp_artist not in result_dict:
				result_dict[temp_artist] = []
			result_dict[temp_artist] += [temp_rank]
	
	result = f'{to_csv_row(result_header)}\n\n'
	csv_line_list = []
	for k, v in result_dict.items():
		field_rank = 'n'
		field_artist = k
		field_type = "-----"
		field_num_songs = len(v)
		field_avg_rank = f"{sum([int(s) for s in v if s.isdigit()]) / (len([t for t in v if t.isdigit()]) + 0.0001):.1f}°"

		csv_line_list += [ [field_rank, field_artist, field_type, field_num_songs, field_avg_rank] ]
	
	csv_line_list.sort(key=lambda x: x[3], reverse=True)
	for csv_line in csv_line_list: 
		result += f'{to_csv_row(csv_line)}\n'

	PrintHandler.generic_print('\n')
	PrintHandler.generic_print(result)
	if not write_output:
		write_output = FileHandler.get_user_bool("Write Output?")

	if write_output:
		status = FileHandler.write_output(RANKING_ARTISTI_BUILDING_FILE, result, check_diff=True)
	else:
		changed = FileHandler.check_differences_file(RANKING_ARTISTI_BUILDING_FILE, result)
		status = what_status_wizard(changed)

	written = was_written_wizard(write_output, status)
	f_print_handler.print_status(RANKING_MUSICA_CANZONI_INPUT, RANKING_ARTISTI_BUILDING_FILE, result, status, is_written=written)
	f_print_handler.update_resume(RANKING_ARTISTI_BUILDING_FILE, status)
	f_print_handler.print_resume()
	PrintHandler.print_separator()
	return result


def to_csv_row(values):
    csv_fields = []
    for v in values:
        field = str(v)

        if any(c in field for c in [',', '"', '\n']):
            field = field.replace('"', '""')
            field = f'"{field}"'

        csv_fields += [field]
    return ",".join(csv_fields)

def was_written_wizard(is_write_output, status=None):
	if not is_write_output:
		return False
	written = True if (status == 0 or status == 1) else False
	return written

def what_status_wizard(was_changed):
	if was_changed == None:
		status = 3
	elif was_changed:
		status = 1
	else:
		status = 2
	return status
