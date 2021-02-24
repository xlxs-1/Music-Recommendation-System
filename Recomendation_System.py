import matplotlib.pyplot as plt
import pandas as pd
import random

def normalizeCsvAndSave():
    a = open("clear_file.csv", "w", encoding="utf-8")

    for line in open("spotify_dataset.csv", "r", encoding="utf-8"):
        str = line.replace(";;;;", "").replace('"""', '"').replace('""', '"').replace(",", '",', 1)
        a.write(str)


#   FUNCTIONS

# Creates a plot of most popular artists.
def PlotmostPopularArtists():
    plt.close("all")
    spotify_data['artistname'].value_counts()[0:41].plot(kind='bar', title="Top 40 Most Popular Artists")
    plt.show()


# Creates a plot of most popular track.
def PlotmostPopularSongs():
    plt.close("all")
    spotify_data['trackname'].value_counts()[0:81].plot(kind='bar', title="Top 80 Most Popular Songs")
    plt.show()


# Creates a plot of most popular playlist.
def PlotmostPopularPlaylists():
    plt.close("all")
    spotify_data['playlistname'].value_counts()[0:21].plot(kind='bar', title="Top 20 Most Popular Playlists")
    plt.show()


# Creates a plot of the most popular songs of an artist.
def PlotmostPopularSongsPerArtist(artist):
    a = spotify_data[spotify_data['artistname'] == artist]['trackname']

    plt.close("all")
    a.value_counts()[0:51].plot(kind='bar', title="Top 50 Most Popular Songs")
    print(a)
    plt.show()


# Creates a plot of the most popular artists of a User .
def PlotmostPopularArtistPerUser(user):
    a = spotify_data[spotify_data['user_id'] == user]['artistname']

    plt.close("all")
    a.value_counts()[0:11].plot(kind='bar', title="Top 10 Most Artist")
    print(a)
    plt.show()


# Function that returns the most popular Artists.
def mostPopularArtists():
    b = spotify_data['artistname'].value_counts()[0:41]


# Function that returns the most popular Songs.
def mostPopularSongs():
    b = spotify_data['trackname'].value_counts()[0:81].reset_index()

    print(b.values.tolist())


# Function that returns the most popular Playlists.
def mostPopularPlaylists():
    b = spotify_data['playlistname'].value_counts()[0:21]


# Function that returns the most popular Songs of an artist.
def mostPopularSongsPerArtist(artist):
    a = spotify_data[spotify_data['artistname'] == artist]['trackname']

    b = a.value_counts()[0:51].reset_index()
    c = b.values.tolist()
    for i in range(len(c)):
        c[i].append(artist)
    return c


# Function that returns the most popular Artists of a user.
def mostPopularArtistPerUser(user):
    a = spotify_data[spotify_data['user_id'] == user]['artistname']

    b = a.value_counts()[0:11].reset_index()
    return b.values.tolist()


# Function that returns the most popular playlists that a user heard.
def mostPopularPlaylistsPerUser(user):
    a = spotify_data[spotify_data['user_id'] == user]['playlistname']

    b = a.value_counts()[0:11].reset_index()
    return b.values.tolist()


# Function that returns all Artists that a user ever heard.
def ArtistPerUser(user):
    a = spotify_data[spotify_data['user_id'] == user]['artistname']

    b = a.value_counts().reset_index()
    return b.values.tolist()


# Function that returns all Artists of a given playlist
def ArtistsPerPlaylist(playlist):
    a = spotify_data[spotify_data['playlistname'] == playlist]['artistname']

    b = a.value_counts().reset_index()
    return b.values.tolist()


# Function that makes an Artists list
def MakeArtistsLists(user):
    return


# Recomendations of popular songs of the artists that the user listened to
def RecomenderPopular(user):
    Artists = mostPopularArtistPerUser(user)
    Songs = []
    for i in range(len(Artists)):
        Songs.extend(mostPopularSongsPerArtist(Artists[i][0]))

    Songs.sort(reverse=True, key=lambda tup: tup[1])

    # for ii in range(30):
    # print(Songs[ii][0], " - ", Songs[ii][2])
    return Songs


# Recomendations of least popular songs of the artists that the user listened to
def RecomenderObscure(user):
    Artists = mostPopularArtistPerUser(user)
    Songs = []
    for i in range(len(Artists)):
        Songs.extend(mostPopularSongsPerArtist(Artists[i][0]))

    Songs.sort(reverse=False, key=lambda tup: tup[1])

    # for ii in range(30):
    #    print(Songs[ii][0], " - ", Songs[ii][2])
    return Songs


# Recomendations of random songs of the artists that the user listened to
def RecomenderRandom(user):
    Artists = mostPopularArtistPerUser(user)
    Songs = []
    for i in range(len(Artists)):
        Songs.extend(mostPopularSongsPerArtist(Artists[i][0]))

    random.shuffle(Songs)

    # for ii in range(30):
    #    print(Songs[ii][0], " - ", Songs[ii][2])
    return Songs


# Ballanced recomendation that makes a playist of 5 songs per artist that a user listened too
# The Artists here are the 10 most popular
def RecomenderBalanced(user):
    Artists = mostPopularArtistPerUser(user)
    Songs = []
    for i in range(len(Artists)):
        Song = mostPopularSongsPerArtist(Artists[i][0])
        random.shuffle(Song)

        for ii in range(5 if len(Song) >= 5 else len(Song)):
            Songs.append(Song[ii])
    random.shuffle(Songs)

    # for ii in range(len(Songs)):
    #    print(Songs[ii][0], " - ", Songs[ii][2])
    return Songs


# Ballanced recomendation that makes a playist of 5 songs per artist that a user listened to
# The Artists here are a mix of popular and other random artists that the user listened to
def RecomenderPerfectlyBalanced(user):
    Artists = ArtistPerUser(user)
    Songs = []

    if len(Artists) <= 5:
        return RecomenderBalanced(user)

    else:
        for i in range(5):
            Song = mostPopularSongsPerArtist(Artists[i][0])
            random.shuffle(Song)
            for ii in range(5 if len(Song) >= 5 else len(Song)):
                Songs.append(Song[ii])
        random.shuffle(Artists)
        for i in range(5):
            Song = mostPopularSongsPerArtist(Artists[i][0])
            for ii in range(5 if len(Song) >= 5 else len(Song)):
                Songs.append(Song[ii])

        random.shuffle(Songs)

        # for ii in range(len(Songs)):
        #    print(Songs[ii][0], " - ", Songs[ii][2])
        return Songs


def RecomenderPlaylistArtist(user):
    Artists1 = ArtistPerUser(user)
    Playlists = mostPopularPlaylistsPerUser(user)
    Artists2 = []
    Songs = []
    for i in range(5 if len(Artists1) >= 5 else len(Artists1)):
        Song = mostPopularSongsPerArtist(Artists1[i][0])
        random.shuffle(Song)
        for ii in range(5 if len(Song) >= 5 else len(Song)):
            Songs.append(Song[ii])
    for i in range(3 if len(Playlists) >= 3 else len(Playlists)):
        Artists2.extend(ArtistsPerPlaylist(Playlists[i][0]))
    random.shuffle(Artists2)
    for i in range(5 if len(Artists2) >= 5 else len(Artists2)):
        Song = mostPopularSongsPerArtist(Artists2[i][0])
        random.shuffle(Song)
        for ii in range(5 if len(Song) >= 5 else len(Song)):
            Songs.append(Song[ii])

    random.shuffle(Songs)

    # for ii in range(len(Songs)):
    #    print(Songs[ii][0], " - ", Songs[ii][2])
    return Songs


# Function that prints a playlist
def printPlaylist(playlist):
    print("____________Song - Artist____________")
    print("_____________________________________")
    for ii in range(len(playlist)):
        print(playlist[ii][0], " - ", playlist[ii][2])

def getAsStringPlaylistAtMost50(playlist):
    s=""
    s=s+"____________Song - Artist____________\n"
    s=s+"_____________________________________\n"
    for ii in range(len(playlist) if len(playlist) <= 50 else 50  ):
        s=s+playlist[ii][0]+ " - "+ playlist[ii][2]+"\n"
    s=s.split("\n")
    s=list(dict.fromkeys(s))
    s="\n".join(s)
    return s

#  Read CSV File
filename = "clear_file.csv"
print("Reading the data")
spotify_data = pd.read_csv(filename, error_bad_lines=False, warn_bad_lines=False)
# ,keep_default_na=False,skip_blank_lines=True

# fix comumn names:  ['user_id', ' "artistname"', ' "trackname"', ' "playlistname"']  =>
# ['user_id', 'artistname','trackname', 'playlistname']
spotify_data.columns = ['user_id', 'artistname', 'trackname', 'playlistname']