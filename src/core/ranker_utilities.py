import os
import re
import csv

from ..utils.FileHandler import FileHandler
from .core_consts import INDEX_RANKING_FILE, PLAYLISTS_CSV_FILE, RANKING_MUSICA_CANZONI_INPUT, RANKING_MUSICA_ARTISTI_INPUT


def index_ranking(input_file=None, write_output=False, in_place=False):
	if input_file is None:
		checked_input_file = FileHandler.get_user_input()
		write_output = FileHandler.get_user_bool("Write Output?")
	else:
		checked_input_file = FileHandler.check_file(input_file)

	if not in_place and write_output:
		in_place = FileHandler.get_user_bool("In Place?")

	m_output_file = checked_input_file if in_place else INDEX_RANKING_FILE

	result = ""
	
	with open(checked_input_file, "r", newline="", encoding='utf-8') as fr:
		header = fr.readline()
		result += f'{header}'
		
		simple_counter = 0
		counter_map = {}
		for line in fr.readlines():
			if not line.strip():
				result += "\n"
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
	
	if write_output:
		FileHandler.write_output(m_output_file, result)
	print(result)	#TODO: PrintHandler
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
		write_output = FileHandler.get_user_bool("Write Output?")
	else:
		checked_input_folder = FileHandler.check_directory(input_folder)

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
	
	if write_output:
		FileHandler.write_output(PLAYLISTS_CSV_FILE, result)
	print(result)	#TODO: PrintHandler
	return result


def build_artists_data(write_output=True):
	if write_output:
		write_output = FileHandler.get_user_bool("Write Output?")

	FileHandler.check_file(RANKING_MUSICA_CANZONI_INPUT)
	FileHandler.check_file(RANKING_MUSICA_ARTISTI_INPUT)
	
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
	for k, v in result_dict.items():
		field_rank = 'n'
		field_artist = k
		field_type = "-----"
		field_num_songs = len(v)
		field_avg_rank = f"{sum([int(s) for s in v if s.isdigit()]) / len([t for t in v if t.isdigit()]):.1f}°"

		csv_line = [field_rank, field_artist, field_type, field_num_songs, field_avg_rank]
		result += f'{to_csv_row(csv_line)}\n'

	if write_output:
		FileHandler.write_output(result, RANKING_MUSICA_ARTISTI_INPUT)
	print(result)	#TODO: PrintHandler
	return result

