from tablemaker import TableMaker # type: ignore

from ..utils.PrintHandler import PrintHandler
from ..utils.FileHandler import FileHandler
from ..utils.utils import get_user_bool
from .core_consts import *
from .ranker_utilities import index_ranking, search_artist, get_songs_from_artist, _to_csv_row


def _helper_build_ranking(RANKING_INPUT, RANKING_FOLDER_OUTPUT, RANKING_OUTPUT, write_output=True, indexing=False):
	if write_output:
		write_output = get_user_bool("Write Output?")

	FileHandler.check_file(RANKING_INPUT)
	FileHandler.check_directory(RANKING_FOLDER_OUTPUT)
	FileHandler.check_file(RANKING_OUTPUT)
	
	print_handler = PrintHandler()
	file_handler = FileHandler()
	table_maker = TableMaker()

	if write_output:
		if indexing:
			index_ranking(RANKING_INPUT, write_output=True, in_place=True)
		computed_table = table_maker(RANKING_INPUT, has_header=True)
		changed = file_handler.write_table(computed_table, RANKING_OUTPUT)
		written = changed
	else:
		obj_to_table = RANKING_INPUT
		if indexing:
			obj_to_table = index_ranking(RANKING_INPUT, write_output=False, in_place=True)
		computed_table = table_maker(obj_to_table, has_header=True, from_string=True)
		changed = FileHandler.check_differences_table(computed_table, RANKING_OUTPUT)
		written = False

	if changed:
		print_handler.print_status_updated(RANKING_INPUT, computed_table)
		print_handler.update_resume(RANKING_OUTPUT, 1)
	else:
		print_handler.print_status_unchanged(RANKING_OUTPUT, computed_table)
		print_handler.update_resume(RANKING_OUTPUT, 2)

	PrintHandler.print_written_status(RANKING_OUTPUT, written)
	print_handler.print_separator()
	print_handler.print_resume()


def build_ranking_canzoni(write_output=True):
	_helper_build_ranking(
		RANKING_MUSICA_CANZONI_INPUT,
		RANKING_MUSICA_FOLDER_OUTPUT,
		RANKING_MUSICA_CANZONI_OUTPUT,
		write_output=write_output, indexing=True
	)

def build_ranking_artisti():
	_helper_build_ranking(
		RANKING_MUSICA_ARTISTI_INPUT,
		RANKING_MUSICA_FOLDER_OUTPUT,
		RANKING_MUSICA_ARTISTI_OUTPUT,
		write_output=True, indexing=True
	)

def build_ranking_canzoni_per_artista():
	artist, _ = _helper_build_ranking_canzoni_per_artista(RANKING_MUSICA_CANZONI_INPUT)
	_helper_build_ranking(
		RANKING_MUSICA_CANZONI_INPUT.replace("(Canzoni) - Raw.txt", f"(Canzoni - {artist}) - Raw.txt"),
		RANKING_MUSICA_CANZONIPERARTISTA_FOLDER_OUTPUT,
		f'{RANKING_MUSICA_CANZONIPERARTISTA_FOLDER_OUTPUT}/{f"Ranking Canzoni - {artist}.txt"}',
		write_output=True, indexing=True
	)

def _helper_build_ranking_canzoni_per_artista(input_file=RANKING_MUSICA_CANZONI_INPUT):
	while True:
		artist = input("Insert Artist Name: ").strip()
		if search_artist(artist):
			break
		print("Artist Name not Found.\n")
	
	file_to_build = input_file.replace("(Canzoni) - Raw.txt", f"(Canzoni - {artist}) - Raw.txt")
	write_output = False
	try:
		FileHandler.check_file(file_to_build)
	except:
		write_output = get_user_bool("Write Output?")

	songs_list = get_songs_from_artist(artist, input_file)
	result = f'Rank A,{_to_csv_row(songs_list[0])}\n'
	result += f'{_to_csv_row([])}\n'

	for s in songs_list[1:]:
		result += f'n,{_to_csv_row(s)}\n'

	if write_output:
		FileHandler.write_output(file_to_build, result)
	print(result)	#TODO: PrintHandler
	return artist, result


def build_ranking_anime():
	_helper_build_ranking(
		RANKING_ANIME_INPUT,
		RANKING_ANIME_FOLDER_OUTPUT,
		RANKING_ANIME_OUTPUT,
		write_output=True, indexing=True
	)

def build_lista_nomi_anime():
	_helper_build_ranking(
		LISTA_NOMI_ANIME_INPUT,
		PROJECT_HUB_ROOT,
		LISTA_NOMI_ANIME_OUTPUT,
		write_output=True, indexing=False
	)


def build_ranking_film():
	_helper_build_ranking(
		RANKING_FILM_INPUT,
		RANKING_FILM_FOLDER_OUTPUT,
		RANKING_FILM_OUTPUT,
		write_output=True, indexing=True
	)
