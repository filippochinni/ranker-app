from ...core.ranker_utilities import *
from ...core.music_utilities import *
from ...core.ranker import *


class MenuObject:
	def __init__(self, name, options):
		self.name = name
		self.options = options

class MenuItem:
	def __init__(self, name, is_submenu = False, action = None):
		self.name = name
		self.is_submenu = is_submenu
		self.action = action

		if (self.is_submenu) and (self.action is not None):
			raise ValueError("A MenuItem cannot be both a submenu and an action.")


MAIN_MENU = MenuObject("RankerApp", [
	MenuItem("Ranker", is_submenu=True),
	MenuItem("Ranker Utilities", is_submenu=True),
	MenuItem("Music Utilities", is_submenu=True),
	MenuItem("Exit")
])

MENU_LIST = {
	"Ranker": MenuObject("Ranker", [
		MenuItem("Ranking Musica", is_submenu=True),
		MenuItem("Ranking Anime", is_submenu=True),
		MenuItem("Ranking Film", is_submenu=True),
		MenuItem("Back")
	]),
	"Ranker Utilities": MenuObject("Ranker Utilities", [
		MenuItem("Index Ranking", action=index_ranking),
		MenuItem("Playlists to CSV", action=playlists_to_csv),
		MenuItem("Build Artists Data", action=build_artists_data),
		MenuItem("Back")
	]),
	"Music Utilities": MenuObject("Music Utilities", [
		MenuItem("Folders to Playlists", action=folders_to_playlists),
		MenuItem("Playlists Fixer", action=fix_playlists),
		MenuItem("Back")
	]),

	"Ranking Musica": MenuObject("Ranking Musica", [
		MenuItem("Build Ranking Canzoni", action=build_ranking_canzoni),
		MenuItem("Build Ranking Artisti", action=build_ranking_artisti),
		MenuItem("Build Ranking Canzoni per Artista", action=build_ranking_canzoni_per_artista),
		MenuItem("Build Ranking Playlist", action=build_ranking_playlist),
		MenuItem("Back")
	]),
	"Ranking Anime": MenuObject("Ranking Anime", [
		MenuItem("Build Ranking Anime", action=build_ranking_anime),
		MenuItem("Build Lista Nomi Anime", action=build_lista_nomi_anime),
		MenuItem("Back")
	]),
	"Ranking Film": MenuObject("Ranking Film", [
		MenuItem("Build Ranking Film", action=build_ranking_film),
		MenuItem("Back")
	])
}