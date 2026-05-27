import csv

from tablemaker import TableMaker # type: ignore

from ..utils.PrintHandler import PrintHandler
from ..utils.FileHandler import FileHandler
from .core_consts import *
from .ranker_utilities import index_ranking, to_csv_row, was_written_wizard, what_status_wizard


def _helper_build_ranking(RANKING_INPUT, RANKING_FOLDER_OUTPUT, RANKING_OUTPUT, write_output=True, indexing=False, col_alignment=['center']):
	FileHandler.check_file(RANKING_INPUT)
	FileHandler.check_directory(RANKING_FOLDER_OUTPUT)

	f_print_handler = PrintHandler(output_obj='Table')
	f_table_maker = TableMaker()

	object_to_table = RANKING_INPUT
	if indexing:
		object_to_table = index_ranking(RANKING_INPUT, write_output=write_output, in_place=True)
	computed_table = f_table_maker(object_to_table, has_header=True, from_string=indexing, colalign=col_alignment)

	PrintHandler.generic_print(computed_table)
	if write_output:
		write_output = FileHandler.get_user_bool("Write Output?")

	if write_output:
		status = FileHandler.write_table(RANKING_OUTPUT, computed_table, check_diff=True, is_ranking=True)
	else:
		changed = FileHandler.check_differences_file(RANKING_OUTPUT, computed_table, is_ranking=True)
		status = what_status_wizard(changed)

	written = was_written_wizard(write_output, status)
	f_print_handler.print_status(RANKING_INPUT, RANKING_OUTPUT, computed_table, status, is_written=written)
	f_print_handler.update_resume(RANKING_OUTPUT, status)
	f_print_handler.print_resume()
	PrintHandler.print_separator()


def build_ranking_canzoni(write_output=True):
	_helper_build_ranking(
		RANKING_MUSICA_CANZONI_INPUT,
		RANKING_MUSICA_FOLDER_OUTPUT,
		RANKING_MUSICA_CANZONI_OUTPUT,
		write_output=write_output, indexing=True,
		col_alignment=['center', 'left', 'left', 'center', 'center', 'left', 'center']
	)

def build_ranking_artisti():
	stop = _helper_build_ranking_artisti()
	if stop:
		print("Returning...")
		return
	_helper_build_ranking(
		RANKING_MUSICA_ARTISTI_INPUT,
		RANKING_MUSICA_FOLDER_OUTPUT,
		RANKING_MUSICA_ARTISTI_OUTPUT,
		write_output=True, indexing=True,
		col_alignment=['center', 'left', 'left', 'center', 'left', 'center', 'center', 'center', 'right']
	)

def _helper_build_ranking_artisti(input_file=RANKING_MUSICA_CANZONI_INPUT):
	f_print_handler = PrintHandler()
	
	origianl_types = {}
	result_header = []
	with open(RANKING_MUSICA_ARTISTI_INPUT, 'r', encoding='utf-8', newline='') as csv_file:
		csv_reader = csv.reader(csv_file)
		result_header = next(csv_reader)
		for row in list(csv_reader)[1:]:
			if not row or not row[1]:
				continue
			origianl_types[row[1]] = row[2]

	result_dict = {}
	songs_list = _get_all_songs(input_file)
	for s in songs_list:
		if s[2] not in result_dict:
			result_dict[s[2]] = []
		result_dict[s[2]] += [s[0]]
	print("\n\nTESTESTETSTES\n\n",result_dict)
	
	result = f'{to_csv_row(result_header)}\n\n'
	csv_line_list = []
	for k, v in result_dict.items():
		field_rank = 'n'
		field_artist = k
		field_type = "-----" if k not in origianl_types else origianl_types[k]
		field_num_songs = len(v)
		field_top = f"{min([int(r) for r in v if r.isdigit()])}°"
		field_top_50 = f"{len([r for r in v if r.isdigit() and int(r) <= 50])}"
		field_top_25 = f"{len([r for r in v if r.isdigit() and int(r) <= 25])}"
		field_top_10 = f"{len([r for r in v if r.isdigit() and int(r) <= 10])}"
		field_avg_rank = f"{sum([int(r) for r in v if r.isdigit()]) / (len([rt for rt in v if rt.isdigit()]) + 0.0001):.1f}"

		csv_line_list += [ [field_rank, field_artist, field_type, field_num_songs, field_top, field_top_50, field_top_25, field_top_10, field_avg_rank] ]
	csv_line_list.sort(key=lambda x: (x[7], x[3], x[6], x[5]), reverse=True)

	for csv_line in csv_line_list: 
		result += f'{to_csv_row(csv_line)}\n'

	PrintHandler.generic_print('\n')
	PrintHandler.generic_print(result)
	write_output = FileHandler.get_user_bool("Write Output?")

	if write_output:
		status = FileHandler.write_output(RANKING_MUSICA_ARTISTI_INPUT, result, check_diff=True)
		stop = False
	else:
		changed = FileHandler.check_differences_file(RANKING_MUSICA_ARTISTI_INPUT, result)
		status = what_status_wizard(changed)
		stop = True

	written = was_written_wizard(write_output, status)
	f_print_handler.print_status(RANKING_MUSICA_CANZONI_INPUT, RANKING_MUSICA_ARTISTI_INPUT, result, status, is_written=written)
	f_print_handler.update_resume(RANKING_MUSICA_ARTISTI_INPUT, status)
	f_print_handler.print_resume()
	PrintHandler.print_separator('^')

	return stop


def build_ranking_canzoni_per_artista():
	artist, _, stop = _helper_build_ranking_canzoni_per_artista(RANKING_MUSICA_CANZONI_INPUT)
	if stop:
		print("Returning...")
		return

	_helper_build_ranking(
		RANKING_MUSICA_CANZONI_INPUT.replace("(Canzoni) - Raw.txt", f"(Canzoni - {artist}) - Raw.txt"),
		RANKING_MUSICA_CANZONIPERARTISTA_FOLDER_OUTPUT,
		f'{RANKING_MUSICA_CANZONIPERARTISTA_FOLDER_OUTPUT}/{RANKING_MUSICA_TAG_STR} (Canzoni - {artist}).txt',
		write_output=True, indexing=True,
		col_alignment=['center', 'center', 'left', 'center', 'center', 'left', 'center']
	)

def _helper_build_ranking_canzoni_per_artista(input_file=RANKING_MUSICA_CANZONI_INPUT):
	f_print_handler = PrintHandler()
	while True:
		input_artist = input("\nInsert Artist Name: ").strip()
		artist = _search_artist(input_artist)
		if artist:
			print('\n')
			break
		print("Artist Name not Found.")
	file_to_build = input_file.replace("(Canzoni) - Raw.txt", f"(Canzoni - {artist}) - Raw.txt")

	songs_list = _get_songs_from_artist(artist, input_file)
	result = f'Rank,{to_csv_row(songs_list[0]).replace("Rank", "R Abs", 1)}\n'
	result += f'{to_csv_row([])}\n'

	for s in songs_list[1:]:
		result += f'{'n' if s[0].isdigit() else 'vn'},{to_csv_row(s)}\n'

	PrintHandler.generic_print('\n')
	PrintHandler.generic_print(result)
	write_output = FileHandler.get_user_bool("Write Output?")

	if write_output:
		status = FileHandler.write_output(file_to_build, result, check_diff=True)
		stop = False
	else:
		changed = FileHandler.check_differences_file(file_to_build, result)
		status = what_status_wizard(changed)
		stop = True

	written = was_written_wizard(write_output, status)
	f_print_handler.print_status(input_file, file_to_build, result, status, is_written=written)
	f_print_handler.update_resume(file_to_build, status)
	f_print_handler.print_resume()
	PrintHandler.print_separator('^')

	return artist, result, stop

def build_ranking_playlist():
	stop = _helper_build_ranking_playlist(RANKING_MUSICA_CANZONI_INPUT)
	if stop:
		print("Returning...")
		return

	_helper_build_ranking(
		RANKING_MUSICA_PLAYLIST_INPUT,
		RANKING_MUSICA_FOLDER_OUTPUT,
		RANKING_MUSICA_PLAYLIST_OUTPUT,
		write_output=True, indexing=False,
		col_alignment=['left', 'center', 'left', 'center', 'center', 'center', 'right']
	)

def _helper_build_ranking_playlist(input_file=RANKING_MUSICA_CANZONI_INPUT):
	f_print_handler = PrintHandler()
	songs_list = _get_all_songs(input_file)

	result_header = []
	with open(RANKING_MUSICA_PLAYLIST_INPUT, 'r', encoding='utf-8', newline='') as csv_file:
		csv_reader = csv.reader(csv_file)
		result_header = next(csv_reader)

	result_dict = {}
	for s in songs_list:
		if s[5] not in result_dict:
			result_dict[s[5]] = []
		result_dict[s[5]] += [s[0]]

	csv_line_list = []
	for k, v in result_dict.items():
		field_playlist = k
		field_num_songs = len(v)
		field_top = f"{min([int(r) for r in v if r.isdigit()])}°"
		field_top_50 = f"{len([r for r in v if r.isdigit() and int(r) <= 50])}"
		field_top_25 = f"{len([r for r in v if r.isdigit() and int(r) <= 25])}"
		field_top_10 = f"{len([r for r in v if r.isdigit() and int(r) <= 10])}"
		field_avg_rank = f"{sum([int(r) for r in v if r.isdigit()]) / (len([rt for rt in v if rt.isdigit()]) + 0.0001):.1f}"

		csv_line_list += [ [field_playlist, field_num_songs, field_top, field_top_50, field_top_25, field_top_10, field_avg_rank] ]	
	csv_line_list.sort(key=lambda x: x[0])
	
	result = f'{to_csv_row(result_header)}\n\n'
	for csv_line in csv_line_list: 
		result += f'{to_csv_row(csv_line)}\n'

	PrintHandler.generic_print('\n')
	PrintHandler.generic_print(result)
	write_output = FileHandler.get_user_bool("Write Output?")

	if write_output:
		status = FileHandler.write_output(RANKING_MUSICA_PLAYLIST_INPUT, result, check_diff=True)
		stop = False
	else:
		changed = FileHandler.check_differences_file(RANKING_MUSICA_PLAYLIST_INPUT, result)
		status = what_status_wizard(changed)
		stop = True

	written = was_written_wizard(write_output, status)
	f_print_handler.print_status(input_file, RANKING_MUSICA_PLAYLIST_INPUT, result, status, is_written=written)
	f_print_handler.update_resume(RANKING_MUSICA_PLAYLIST_INPUT, status)
	f_print_handler.print_resume()
	PrintHandler.print_separator('^')

	return stop


def build_ranking_anime():
	_helper_build_ranking(
		RANKING_ANIME_INPUT,
		RANKING_ANIME_FOLDER_OUTPUT,
		RANKING_ANIME_OUTPUT,
		write_output=True, indexing=True,
		col_alignment=['center', 'left', 'left', 'left']
	)

def build_lista_nomi_anime():
	_helper_build_ranking(
		LISTA_NOMI_ANIME_INPUT,
		PROJECT_HUB_ROOT,
		LISTA_NOMI_ANIME_OUTPUT,
		write_output=True, indexing=False,
		col_alignment=['center', 'left', 'left', 'left', 'left', 'left']
	)


def build_ranking_film():
	_helper_build_ranking(
		RANKING_FILM_INPUT,
		RANKING_FILM_FOLDER_OUTPUT,
		RANKING_FILM_OUTPUT,
		write_output=True, indexing=True,
		col_alignment=['center', 'left', 'center', 'center']
	)


def _search_artist(artist_to_search, input_file=RANKING_MUSICA_CANZONI_INPUT):
	with open(input_file, 'r', encoding='utf-8', newline='') as csv_file:
		csv_reader = csv.reader(csv_file)
		for row in list(csv_reader)[1:]:
			if not row or not row[2]:
				continue
			if row[2].strip().lower() == artist_to_search.strip().lower():
				return row[2].strip()
	return None

def _get_songs_from_artist(artist_to_search, input_file=RANKING_MUSICA_CANZONI_INPUT):
	result = []
	with open(input_file, 'r', encoding='utf-8', newline='') as csv_file:
		csv_reader = csv.reader(csv_file)
		header = next(csv_reader)
		header.pop(2)
		result = [header,]
		for row in list(csv_reader)[1:]:
			if not row or not row[2]:
				continue
			if row[2].strip().lower() == artist_to_search.strip().lower():
				result += [[row[0], row[1], row[3], row[4], row[5], row[6]]]
	return result

def _get_all_songs(input_file=RANKING_MUSICA_CANZONI_INPUT):
	result = []
	with open(input_file, 'r', encoding='utf-8', newline='') as csv_file:
		csv_reader = csv.reader(csv_file)
		next(csv_reader)
		for row in list(csv_reader):
			if not row or not row[5]:
				continue
			result += [ row ]
	return result

