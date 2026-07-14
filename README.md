# Ranker App

RankerApp is a utility app for building Rankings and other related utility functionalities.<br>
It is navigable through an old-fashioned Menu Interface.

It is a personal project which follows a structured and clear Manifesto.

## Rankings Manifesto

[Rankings Manifesto]

## Usage

### Menu Interface Usage

| Menu             | Functionality                     | Description                                                                                |
|------------------|-----------------------------------|--------------------------------------------------------------------------------------------|
| Ranking Musica   | Build Ranking Canzoni             | Build Ranking of Songs from the corrispondent [Raw] version                                |
| Ranking Musica   | Build Ranking Artisti             | Build Ranking of Artists from the corrispondent [Raw] version                              |
| Ranking Musica   | Build Ranking Canzoni per Artista | Build Ranking of Song for a user-chosen Artist from the corrispondent [Raw] version        |
| Ranking Musica   | Build Ranking Playlist            | Build Ranking of Playlists from the corrispondent [Raw] version                            |
| Ranking Anime    | Build Ranking Anime               | Build Ranking of Anime from the corrispondent [Raw] version                                |
| Ranking Anime    | Build Lista Nomi Anime            | Build the Anime Names List from the corrispondent [Raw] version                            |
| Ranking Film     | Build Ranking Film                | Build Ranking of Films from the corrispondent [Raw] version                                |
| Ranker Utilities | Index Ranking                     | Indexes a List of Entries                                                                  |
| Ranker Utilities | Playlists to CSV                  | Turns a Folder of Playlist .m3u files into a CSV file                                      |
| Music Utilities  | Folders to Playlists              | Turns a Folder (and Subfolders) into a .m3u Playlist mapping the Folder's .mp3 files       |
| Music Utilities  | Playlists Fixer                   | Replaces an inputed Substring with another inputed Substring in all Playlist Files content |

### Command Line Usage

**!! Not Implemented YET !!**

```
ranker-app [-h] [-cl]
```
#### Options

`-h`, `--help` &emsp;&emsp;&emsp;&emsp; Show this help message

`-cl` &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Use the Command Line interface instead of the Menu Interface


## Requirements
### Python
- Python 3.8 or higher
### Dependencies
- table-maker

_______________________________________________________________________________________________________________________

## [Rankings Manifesto]:

(Will be translated in English in the future)

_______________________________________________________________________________________________________________________

Rankings è un progetto che comprende Ranking (Classifiche) di vari tipi di Medium

Ogni Ranking è mutabile, non solo in quanto vengono aggiunte nuove Istanze di Medium, ma perché l'opinione su una Istanza può cambiare nel tempo

Sebbene vengano definite delle Linee Guida per classificare i Medium, il fattore di classificazione principale è il Feeling

I Ranking sono effettuati con minuzia utilizzando un approccio Bottom-up, partendo dagli Item peggiori per arrivare ai migliori

I tipi di Medium attualmente classificati con un Ranking sono i seguenti:

Anime  |  Film  |  Canzoni  |  Artisti

Ogni Ranking caratterizza le Istanze con degli Attributi, gli Attributi presenti dipendono dal Medium


L'Update dei Ranking è periodico ma non a tempo fisso
Le Minor Release possono avvenire in qualsiasi momento; le Major Release vanno eseguite raramente (indicativamente, al massimo 2 volte all'Anno)

Una Minor Release è un update senza storicizzazione, si modifica il Ranking sovrascrivendo il Ranking Current
Una Major Release è un update con storicizzazione, il Ranking Current viene, prima di essere aggiornato, copiato e memorizzato in una cartella Storico



////////////

++ Glossario:

- Ranking:		Quando si utilizza "Ranking" senza ulteriori specificazioni, si intende il Ranking in formato Tabellare
- Ranking Current:	Current (o Ranking Current) è la versione attuale del Ranking (non una versione storicizzata)
- Ranking Raw:		Ranking Raw (o Raw) è la versione Raw del Ranking; in formato csv, è utilizzata da RankerApp per creare i Ranking
- Medium:		Un Medium è inteso come un Tipo (o Categoria) di Medium			[esempi: Musica, Anime, Film]
- Istanza:		Una Istanza (o Istanza di Medium; o Item) è un singolo e unico Medium	[esempi: Canzone - Musica; singolo Film - Film]
- Entry:		Una Entry è una Istanza. Si utilizza questo termine quando si intende una Istanza all'intero della tabella del Ranking
- Attributo:		Un Attributo è una caratteristica di una Istanza			[esempi: Artista - Canzone; Anno - Film]
- Categoria:		Subset di Istanze all'interno di un Ranking, in genere per coprire casi particolari

////////////

++ Note Generali:

-

__________________________________________________________________________________________________________________________


@ Ranking Anime


Ranking Anime è il Ranking degli Anime
Sono considerati Anime tutti gli Anime con durata episodio standard o lunga
Sono considerati solo Anime conclusi (eccetto eccezioni)
Un Anime è considerato una volta sola, anche se diviso in parti considerabili distaccate (eccetto eccezioni)

++ Attributi:		Rank  |  Anime  |  Year  |  1st Watch

1) Rank:	Rank dell'Anime
2) Anime:	Titolo dell'Anime
3) Year:	Periodo di Airing dell'Anime
4) 1st Watch:	Anno 1a Watch (Periodo nei casi adatti)

++ Linee Guida:

-

++ Note:

- Il Ranking NON contiene Anime Movie stand-alone, essi sono contenuti nel Ranking Film
- Anime Movie strettamente relativi a un Anime sono considerati parte integrante dell'Anime
	- (Sono considerati ANCHE singolarmente se hanno buona valenza come stand-alone)
- Anime molto lunghi (es. One Piece) sono considerati anche se non conclusi
- Il Titolo è scritto in Romanji se il titolo originale è in Kanji; Stile solito

- Nel Ranking si identificano le seguenti Categorie:		// N è il Rank
	- N		--> Anime Concluso
	- bN		--> Anime Ongoing
	- iN		--> Anime Visione Interrotta
	- mN		--> Anime Meme (e/o durata ep inferiore allo standard)
	- uN		--> Anime Unranked (da posizionare alla prossima Release)


//////////////////////////////////////////////////////////////////////////////////////////////


@ Ranking Film


Raking Film è il Ranking dei Film
Sono Considerati Film tutti i Lungometraggi (anche brevi)

++ Attributi:		Rank  |  Film  |  Year  |  1st Watch

1) Rank:	Rank del Film
2) Film:	Titolo del Film
3) Year:	Anno del Film
4) 1st Watch:	Anno 1a Watch

++ Linee Guida:

-

++ Note:

- Film Live Action e Film Animati saranno divisi in Categorie
- Film Anime avranno il loro Ranking dedicato in futuro


//////////////////////////////////////////////////////////////////////////////////////////////


@ Ranking Canzoni


Ranking Canzoni è il Ranking delle Canzoni
Sono considerate Canzoni SOLO le Canzoni Giapponesi		// Info nelle Note
Se una Canzone già presente nel Ranking ha delle Versioni alternative, queste sono poste nella Categoria apposita

++ Attributi:		Rank  |  Song  |  Artist  |  Year  |  1st Listen  |  Playlist |  Rel Rank

1) Rank:	Rank della Canzone
2) Song:	Titolo della Canzone
3) Artist:	Artista della Canzone
4) Year:	Anno della Canzone
5) 1st Listen:	Anno 1o Ascolto
6) Playlist:	Playlist di appartenenza
7) Rel Rank:	Posizione Relativa nella Playlist

++ Linee Guida:

-

++ Note:

- I Titoli delle Canzoni sono coerenti con le Naming Conventions della Musica
- In questo Ranking si considerano solo le canzoni Giapponesi in quanto rappresentano la grande maggioranza delle Canzoni oggetto,\
  mettere tutto insieme sarebbe stato troppo confuso, in quanto alcune Canzoni Italiane e Inglese sarebbero a un Rank relativamente\
  alto, e in quanto sarebbe troppo difficile e strano confrontare i due blocchi di Lingue.\
  Si considera la possibilità futura di un Ranking apposito per Canzoni Italiane, Inglese e Altro
- Non si considerano le Soundtrack (no Vocal). Anche in questo caso, si considera la possibilità di un Ranking apposito

- Nel Ranking si identificano le seguenti Categorie:		// N è il Rank
	- N		--> Canzoni
	- vN		--> Versioni Alternative di Canzoni che sono già nel Ranking
	- uN		--> Canzoni Unranked (da posizionare alla prossima Release)


//////////////////////////////////////////////////////////////////////////////////////////////


@ Ranking Canzoni (per Artista)


Ranking Canzoni - <Artista> è il Ranking delle Canzoni per uno specifico Artista
Sono considerate Canzoni dell'Artista tutte le sue Full Release (anche le Cover, purché Full)
Se una Canzone già presente nel Ranking ha delle Versioni alternative, queste sono poste nella Categoria apposita

++ Attributi:		Rank  |  Song  |  Year  |  1st Listen  |  Playlist  |  Rel Rank

1) Rank:	Rank della Canzone
2) Song:	Titolo della Canzone
3) Year:	Anno della Canzone
4) 1st Listen:	Anno 1o Ascolto
5) Playlist:	Playlist di appartenenza
6) Rel Rank:	Posizione Relativa nella Playlist

++ Linee Guida:

- I posizionamenti del Ranking DEVONO rispecchiare il posizionamento nel Ranking Musica

++ Note:

- I Titoli delle Canzoni sono coerenti con le Naming Conventions della Musica

- Nel Ranking si identificano le seguenti Categorie:		// N è il Rank
	- N		--> Canzoni
	- vN		--> Versioni Alternative di Canzoni che sono già nel Ranking
	- uN		--> Canzoni Unranked (da posizionare alla prossima Release)


//////////////////////////////////////////////////////////////////////////////////////////////


@ Ranking Artisti


Ranking Artisti è il Ranking degli Artisti (Canzoni)
Sono considerati Artisti SOLO Cantanti e Band Giapponesi

++ Attributi:		Rank  |  Artist  |  Type  |  Num Songs  |  Top  |  Top <50|25|10>  |  Avg Rank

1) Rank:	Rank dell'Artista
2) Artist:	Nome dell'Artista o della Band
3) Type:	Se l'Artista è una Band o un Singolo
4) Num Songs:	Numero di Canzoni in Playlist dell'Artista
5) Top		Rank della Canzone con Rank più alto dell'Artista
6) Top<>	Numero di Canzoni dell'Artista nella Top<>
7) Avg Rank:	Rank Medio delle Canzoni dell'Artista

++ Linee Guida:

-

++ Note:

- Il nome "Ranking Artisti" è ambiguo, ma "Artist" è il nome utilizzato dai Music Player di Samsung e Windows


//////////////////////////////////////////////////////////////////////////////////////////////


@ Ranking Playlist


Ranking Playlist è il Ranking delle Playlist delle Canzoni
Sono considerate le Playlist esistenti, da cui questo Ranking viene generato

++ Attributi:		Playlist  |  Num Songs  |  Top  |  Top <50|25|10>  |  Avg Rank

1) Playlist:	Nome della Playlist
2) Num Songs:	Numero di Canzoni che la Playlist contiene
3) Top		Rank della Canzone con Rank più alto della Playlist
4) Top<>	Numero di Canzoni della Playlist nella Top<>
5) Avg Rank:	Rank Medio delle Canzoni della Playlist

++ Linee Guida:

-

++ Note:

- 

