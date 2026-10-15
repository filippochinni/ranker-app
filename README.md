# Ranker App

RankerApp is an utility app for building Rankings and other related utility functionalities.<br>
It is navigable through an old-fashioned Menu Interface.

It is a personal project which follows a structured and clear Manifesto.

## Rankings Manifesto Link

[Rankings Manifesto](#rankings-manifesto)

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
| Ranking Film     | Build Ranking Film (Cartoon)      | Build Ranking of Films (Cartoon) from the corrispondent [Raw] version                      |
| Ranking Film     | Build Ranking Film (Anime)        | Build Ranking of Films (Anime) from the corrispondent [Raw] version                        |
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

## Rankings Manifesto

> Notes: [Leftovers from original italian version: Canzone/Canzoni = Song/Songs; Artista/Artisti = Artist/Artists; Storico = History]

Rankings is a Project that includes Rankings of various types of Medium

Each Ranking is mutable, not only because new Instances of Medium are added, but also because the opinion on an Instance can change over time

The main ranking factor is "feeling"<br>
Some Rankings may have objective classification criteria. If that is not the case, the only factor is "feeling"

Rankings are made meticulously using a Bottom-Up approach, starting from the worst Items to the best ones

The types of Medium currently ranked with a Ranking are the following:

	Anime  |  Film  |  Canzoni  |  Artisti  |  Playlist

Each Ranking characterizes the Instances with Attributes, what Attributes are present depends on the Medium

Rankings update is periodic, without a given timeframe<br>
Minor Releases can happen at any time; Major Releases should be performed rarely (approximately, at most 2 times a year)

A Minor Release is an update without historicization, the Ranking is modified by overwriting the Current Ranking<br>
A Major Release is an update with historicization, the Current Ranking is copied and stored in a Storico folder before being updated

## Glossary:

|                     |                                                                                                                          |
|---------------------|--------------------------------------------------------------------------------------------------------------------------|
| **Ranking**         | When "Ranking" is used without further specifications, it refers to the Ranking in Tabular format                        |
| **Ranking Current** | Current (or Ranking Current) is the current (non-historicized) version of the Ranking                                    |
| **Ranking Raw**     | Ranking Raw (or Raw) is the Raw version of the Ranking; in csv format, is used by RankerApp to create the Rankings       |
| **Medium**          | A Medium is intended as a Type of Medium [examples: Music, Anime, Film]                                                  |
| **Instance**        | An Instance (or Instance of Medium) (or Item) is a single and unique Medium [examples: Song - Music; single Film - Film] |
| **Entry**           | An Entry is an Instance in table. This term is used when referring to an Instance within the table of the Ranking        |
| **Attribute**       | An Attribute is a characteristic of an Instance [examples: Artist - Song; Year - Film]                                   |
| **Category**        | Subset of Instances within a Ranking, usually to cover special cases                                                     |
| **SubRanking**      | Logical Ranking within a Category                                                                                        |
| **Rank**            | Ordinal number representing the Position of an Instance in the Ranking (or SubRanking)                                   |


___________________________________________________________________________________________________________________________________________________________


## Ranking Anime

Ranking Anime is the Ranking of Anime<br>
[For Main Category] Are considered Anime all Anime with standard or long episode duration<br>
[For Main Category] Are considered only Anime which are concluded (except exceptions)<br>
An Anime is considered a single time, even if divided into parts that could be considered separate (except exceptions)

### Attributes:

	Rank  |  Anime  |  Year  |  1st Watch

|    |           |                                          |
|----|-----------|------------------------------------------|
| 1) | Rank      | Rank of the Anime                        |
| 2) | Anime     | Title of the Anime                       |
| 3) | Year      | Airing Period of the Anime               |
| 4) | 1st Watch | Year of 1st Watch (Period in applicable) |

### Notes:

- The Ranking does NOT contain stand-alone Anime Movies, they are contained in the Ranking Film (Anime)
- Anime Movies that are strictly related to an Anime are considered as integral part of the Anime towards classification
- Anime which are very long (e.g. One Piece) are considered in the main category even if they are not concluded
- The Title is written in Romanji if the original title is in Kanji; Usual Style (Title Style)
- The Anime Title follows the "Canonical Name" defined in Lista Nomi Anime

### Categories:

(N is the Rank)

|    |                                                     |
|----|-----------------------------------------------------|
| N  | Anime Concluded                                     |
| bN | Anime Ongoing                                       |
| iN | Anime Watch Interrupted                             |
| mN | Anime Meme (and/or episode duration below standard) |
| uN | Anime Unranked (to be ranked in the next Release)   |


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


## Ranking Film

Ranking Film is the Ranking of Films<br>
It is divided into 3 Rankings: `Film  |  Film (Cartoon)  |  Film (Anime)`<br>
Are considered Films all full-length Movies (even if short)

### Attributes:

	Rank  |  Film  |  Year  |  1st Watch  |  Plays  |  Rating  |  ID Trakt  |  ID IMDb  |  ID TMDB

|    |           |                                         |
|----|-----------|-----------------------------------------|
| 1) | Rank      | Rank of the Film                        |
| 2) | Film      | Title of the Film                       |
| 3) | Year      | Year of the Film                        |
| 4) | 1st Watch | Date of 1st Watch                       |
| 5) | Plays     | Number of Rewatches                     |
| 6) | Rating    | Rating (score from 1 to 10) of the Film |
| 7) | ID Trakt  | ID of the Film on Trakt                 |
| 8) | ID IMDb   | ID of the Film on IMDb                  |
| 9) | ID TMDB   | ID of the Film on TMDB                  |

### Notes:

- The Ranking is sorted according to the Rating Attribute
- Films with the same Rating are sorted according to "feeling"
- The Film Title is the one corresponding to the Trakt Title for that Film
- The Title of Films (Anime) follows the "Canonical Name" defined in Lista Nomi Anime

### Categories:

(N is the Rank)

|    |                                                                                         |
|----|-----------------------------------------------------------------------------------------|
| N  | Film                                                                                    |
| vN | Alternative Versions (Re-releases) that are considered different Films by movie DBs |
| sN | TV Specials of TV Series/Anime/Cartoons that are considered "Films" by movie DBs        |
| uN | Film Unranked (to be ranked in the next Release)                                        |


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


## Ranking Canzoni

Ranking Canzoni is the Ranking of Songs<br>
Are considered Songs ONLY Japanese Songs (more info in the Notes)<br>
If a Song already present in the Ranking has alternative Versions, these are placed in the appropriate Category

### Attributes:

	Rank  |  Song  |  Artist  |  Year  |  1st Listen  |  Playlist |  Rel Rank

|    |            |                                   |
|----|------------|-----------------------------------|
| 1) | Rank       | Rank of the Song                  |
| 2) | Song       | Title of the Song                 |
| 3) | Artist     | Artist of the Song                |
| 4) | Year       | Year of the Song                  |
| 5) | 1st Listen | Date of 1st Listen                |
| 6) | Playlist   | Playlist of the Song              |
| 7) | Rel Rank   | Relative Position in the Playlist |

### Notes:

- The Titles of Songs are compliant with the Naming Conventions of Music
- In this Ranking only Japanese Songs are considered because they represent the vast majority of Songs in question;\
putting everything together would have been too confusing, as some Italian and English Songs would be at a relatively\
high Rank, and it would be too difficult and strange to compare the two language blocks.\
It will be considered in the future to have a specific Ranking for Italian, English and Other Songs
- Soundtracks (no Vocal) Songs are not considered. In this case too, it will be considered to have a specific Ranking

### Categories:

(N is the Rank)

|    |                                                      |
|----|------------------------------------------------------|
| N  | Songs                                                |
| vN | Alternative Versions of Songs already in the Ranking |
| uN | Unranked Songs (to be ranked in the next Release)    |


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


## Ranking Canzoni (per Artista)

Ranking Canzoni - \<Artista\> is the Ranking of Songs for a specific Artist<br>
Are considered Songs of the Artist all their Full Releases (even Covers, as long as they are Full)<br>
If a Song which is already present in the Ranking has alternative Versions, these are placed in the appropriate Category

### Attributes:

	Rank  |  Song  |  Year  |  1st Listen  |  Playlist  |  Rel Rank

|    |            |                                   |
|----|------------|-----------------------------------|
| 1) | Rank       | Rank of the Song                  |
| 2) | Song       | Title of the Song                 |
| 3) | Year       | Year of the Song                  |
| 4) | 1st Listen | Date of 1st Listen                |
| 5) | Playlist   | Playlist of the Song              |
| 6) | Rel Rank   | Relative Position in the Playlist |

### Notes:

- The Titles of Songs are compliant with the Naming Conventions of Music
- The ranks of the Ranking MUST reflect the ranks in Ranking Musica (Canzoni)

### Categories:

(N is the Rank)

|    |                                                      |
|----|------------------------------------------------------|
| N  | Songs                                                |
| vN | Alternative Versions of Songs already in the Ranking |
| uN | Unranked Songs (to be ranked in the next Release)    |


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


## Ranking Artisti

Ranking Artisti is the Ranking of Artists (of Music Songs)<br>
Are considered Artists ONLY Japanese Singers and Bands<br>

### Attributes:

	Rank  |  Artist  |  Type  |  Num Songs  |  Top  |  Top <50|25|10>  |  Avg Rank

|    |           |                                                                                                                                                         |
|----|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1) | Rank      | Rank of the Artist                                                                                                                                      |
| 2) | Artist    | Name of the Artist                                                                                                                                      |
| 3) | Type      | Type of the Artist (<`Solo`\|`Band`\|`Band (Duo)`\|`Solo (Utaite)`\|`Solo (VSinger)`\|`Solo (Seiyuu)`\|`Solo (Anisong)`\|`Band (Project)`\|`Producer`>) |
| 4) | Num Songs | Number of Songs in Playlist of the Artist                                                                                                               |
| 5) | Top       | Rank of the Song with the highest Rank of the Artist                                                                                                    |
| 6) | Top<>     | Number of Songs of the Artist in the Top<>                                                                                                              |
| 7) | Avg Rank  | Average Rank of the Songs of the Artist                                                                                                                 |

### Notes:

- The name "Ranking Artisti" is ambiguous, but "Artist" is the name used in the mp3 standard


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


## Ranking Playlist

Ranking Playlist is the Ranking of Playlists of Songs<br>
Are considered all and only the existing Playlists, which are used to generate this Ranking<br>

### Attributes:

	Playlist  |  Num Songs  |  Top  |  Top <50|25|10>  |  Avg Rank

|    |           |                                                        |
|----|-----------|--------------------------------------------------------|
| 1) | Playlist  | Name of the Playlist                                   |
| 2) | Num Songs | Number of Songs in the Playlist                        |
| 3) | Top       | Rank of the Song with the highest Rank of the Playlist |
| 4) | Top<>     | Number of Songs of the Playlist in the Top<>           |
| 5) | Avg Rank  | Average Rank of the Songs of the Playlist              |

### Notes:

- Playlists are sorted by name, they do not have a Rank attribute. This Ranking only has a statistical purpose
