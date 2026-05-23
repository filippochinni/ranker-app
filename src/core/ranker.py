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
	_helper_build_ranking(
		RANKING_MUSICA_ARTISTI_INPUT,
		RANKING_MUSICA_FOLDER_OUTPUT,
		RANKING_MUSICA_ARTISTI_OUTPUT,
		write_output=True, indexing=True,
		col_alignment=['center', 'left', 'left', 'left', 'left']
	)

def build_ranking_canzoni_per_artista():
	artist, _, stop = _helper_build_ranking_canzoni_per_artista(RANKING_MUSICA_CANZONI_INPUT)
	if stop:
		print("Returning...")
		return

	_helper_build_ranking(
		RANKING_MUSICA_CANZONI_INPUT.replace("(Canzoni) - Raw.txt", f"(Canzoni - {artist}) - Raw.txt"),
		RANKING_MUSICA_CANZONIPERARTISTA_FOLDER_OUTPUT,
		f'{RANKING_MUSICA_CANZONIPERARTISTA_FOLDER_OUTPUT}/{f"Ranking Canzoni - {artist}.txt"}',
		write_output=True, indexing=True,
		col_alignment=['center', 'center', 'left', 'center', 'center', 'left']
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
	result = f'Rank,{to_csv_row(songs_list[0]).replace("Rank", "R_Abs", 1)}\n'
	result += f'{to_csv_row([])}\n'

	for s in songs_list[1:]:
		result += f'n,{to_csv_row(s)}\n'

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

