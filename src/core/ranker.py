from tablemaker import TableMaker # type: ignore

from ..utils.PrintHandler import PrintHandler
from ..utils.FileHandler import FileHandler
from ..utils.utils import get_user_bool
from .core_consts import *
from .ranker_utilities import index_ranking


def build_ranking_canzoni(write_output=True):
	if write_output:
		write_output = get_user_bool("Write Output?")

	FileHandler.check_file(RANKING_MUSICA_CANZONI_INPUT)
	FileHandler.check_directory(RANKING_MUSICA_FOLDER_OUTPUT)
	FileHandler.check_file(RANKING_MUSICA_CANZONI_OUTPUT)
	
	print_handler = PrintHandler()
	file_handler = FileHandler()
	table_maker = TableMaker()

	if write_output:
		index_ranking(RANKING_MUSICA_CANZONI_INPUT, write_output=True, in_place=True)
		computed_table = table_maker(RANKING_MUSICA_CANZONI_INPUT, has_header=True)
		changed = file_handler.write_table(computed_table, RANKING_MUSICA_CANZONI_OUTPUT)
		written = changed
	else:
		raw_file = index_ranking(RANKING_MUSICA_CANZONI_INPUT, write_output=False, in_place=True)
		computed_table = table_maker(raw_file, has_header=True, from_string=True)
		changed = FileHandler.check_differences_table(computed_table, RANKING_MUSICA_CANZONI_OUTPUT)
		written = False

	if changed:
		print_handler.print_status_updated(RANKING_MUSICA_CANZONI_INPUT, computed_table)
		print_handler.update_resume(RANKING_MUSICA_CANZONI_OUTPUT, 1)
	else:
		print_handler.print_status_unchanged(RANKING_MUSICA_CANZONI_OUTPUT, computed_table)
		print_handler.update_resume(RANKING_MUSICA_CANZONI_OUTPUT, 2)

	PrintHandler.print_written_status(RANKING_MUSICA_CANZONI_OUTPUT, written)
	print_handler.print_separator()
	print_handler.print_resume()


def build_ranking_artisti():
	print("NOT IMPLEMENTED YET")
	pass

def build_ranking_canzoni_per_artista():
	print("NOT IMPLEMENTED YET")
	pass


def build_ranking_anime():
	print("NOT IMPLEMENTED YET")
	pass

def build_lista_nomi_anime():
	print("NOT IMPLEMENTED YET")
	pass


def build_ranking_film():
	print("NOT IMPLEMENTED YET")
	pass

