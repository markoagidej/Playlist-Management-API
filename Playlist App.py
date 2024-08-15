from flask import Flask, request, jsonify

app = Flask(__name__)

# Task 1: Data Organization with Lists and Dictionaries:
song_list = []
playlist_dictionary = {}

# Songs
def create_song(artist, album, title, genre):
    new_song = {
                    'artist': artist,
                    'album': album,
                    'title': title,
                    'genre': genre
                }
    song_list.append(new_song)
    return new_song

def update_song(artist, album, title, genre):
    song_to_update = get_song(title)
    new_song = create_song(artist, album, title, genre)
    for playlist, songList in playlist_dictionary.items():
        for song in songList:
            if song == song_to_update:
                playlist_dictionary[playlist].append(new_song)
    delete_song(song = song_to_update)

def delete_song(**kwargs):
    song = kwargs.get("song", None)
    title = kwargs.get("title", None)
    if song:
        if song in song_list:
            song_list.remove(song)
            for playlist in playlist_dictionary.values():
                while song in playlist:
                    playlist.remove(song)
    elif title:
        song = get_song(title)
        delete_song(song = song)

def get_song(title):
    for song in song_list:
        if song['title'] == title:
            return song
        else:
            print(f"No song found with title of: {title}")

# Playlists
def create_playlist(name):
    if name in playlist_dictionary:
        print(f"Playlist titled '{name}' already exists!")
    else:
        playlist_dictionary[name] = []

def update_playlist(old_name, new_name):
    playlist_to_update, song_list = get_playlist(old_name)
    playlist_dictionary[new_name] = song_list
    delete_playlist(playlist_to_update)

def get_playlist(name):
    return name, playlist_dictionary[name]

def delete_playlist(name):
    if name in playlist_dictionary:
        del playlist_dictionary[name]

# Song/Playlist interactions
def add_song_to_playlist(song_title, playlist_name):
    song_to_add = get_song(song_title)
    playlist = get_playlist(playlist_name)[1]
    playlist.append(song_to_add)
    playlist_dictionary[playlist_name] = playlist
    print(f"{song_title} added to playlist: {playlist_name}")

def remove_song_from_playlist(song_title, playlist_name):
    song = get_song(song_title)
    playlist_dictionary[playlist_name].remove(song)

# Task 2: Efficient Search and Sort Algorithms for Playlist Navigation:

def sort_playlist(song_list, sort_category):
    # song_list = playlist_dictionary[playlist_name]
    if len(song_list) > 1:
        mid = len(song_list) // 2
        left = song_list[:mid]
        right = song_list[mid:]

        sort_playlist(left, sort_category)
        sort_playlist(right, sort_category)

        left_index = right_index = main_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index][sort_category] < right[right_index][sort_category]:
                song_list[main_index] = left[left_index]
                left_index += 1
            else:
                song_list[main_index] = right[right_index]
                right_index += 1

            main_index += 1

        while left_index < len(left):
            song_list[main_index] = left[left_index]
            left_index += 1
            main_index += 1
            
        while right_index < len(right):
            song_list[main_index] = right[right_index]
            right_index += 1
            main_index += 1

# Task 3: Building a Flask API for Playlist Access and Management:
## Song Engpoints
# Create Song
@app.route('/songs', methods=['POST'])
def createSong():
    data = request.get_json()
    create_song(data['artist'], data['album'], data['title'], data['genre'])
# Update Song
@app.route('/songs', methods=['PUT'])
def updateSong():
    data = request.get_json()
    update_song(data['artist'], data['album'], data['title'], data['genre'])
# Delete Song
@app.route('/songs', methods=['DELETE'])
def deleteSong():
    data = request.get_json()
    delete_song(song = create_song(data['artist'], data['album'], data['title'], data['genre']))
# Seach/Get Song
@app.route('/songs', methods=['GET'])
def getSong():
    data = request.get_json()
    return jsonify(get_song(data['title']))

## Playlist Endpoints
# Create Playlist
@app.route('/playlists', methods=['POST'])
def sortPlaylist():
    data = request.get_json()
    create_playlist(data['name'])
# Get Playlist
@app.route('/playlists', methods=['Get'])
def getPlaylist():
    data = request.get_json()
    return jsonify(get_playlist(data['name']))
# Update Playlist
@app.route('/playlists/<string:playlist_name>', methods=['PUT'])
def updatePlaylist(playlist_name):
    data = request.get_json()
    update_playlist(playlist_name, data['name'])
# Delete Playlist
@app.route('/playlists', methods=['DELETE'])
def deletePlaylist():
    data = request.get_json()
    delete_playlist(data['name'])

## Additional Endpoints:
# Add song to Playlist
@app.route('/playlists/<string:playlist_name>', methods=['POST'])
def addToPlaylist(playlist_name):
    data = request.get_json()
    song_title = (data['song_title'])
    add_song_to_playlist(song_title, playlist_name)
# Remove song from Playlist
@app.route('/playlists/<string:playlist_name>', methods=['DELETE'])
def removeFromPlaylist(playlist_name):
    data = request.get_json()
    song_title = (data['song_title'])
    remove_song_from_playlist(song_title, playlist_name)
# Sort songs in Playlist by song name, genre, and artist
@app.route('/playlists/sort/<string:playlist_name>', methods=['PUT'])
def sortSelectedPlaylist(playlist_name):
    data = request.get_json()
    sort_playlist(playlist_name, data['sort_category'])

# Testing
# Creating songs
create_song("Artist 1", "Album 1", "A1A1T1", "Genre 1")
create_song("Artist 1", "Album 1", "A1A1T2", "Genre 1")
create_song("Artist 1", "Album 1", "A1A1T3", "Genre 1")

create_song("Artist 2", "Album 1", "A2A1T1", "Genre 1")
create_song("Artist 2", "Album 1", "A2A1T2", "Genre 1")
create_song("Artist 2", "Album 1", "A2A1T3", "Genre 1")

create_song("Artist 2", "Album 2", "A2A2T1", "Genre 2")
create_song("Artist 2", "Album 2", "A2A2T2", "Genre 2")
create_song("Artist 2", "Album 2", "A2A2T3", "Genre 2")

create_song("Artist 3", "Album 1", "A3A1T1", "Genre 3")
create_song("Artist 3", "Album 1", "A3A1T2", "Genre 4")
create_song("Artist 3", "Album 1", "A3A1T3", "Genre 2")

# Printing song list
print("All songs in song_list:")
for song in song_list:
    print(song)

# Printing result of get_song()
print("\nPrinting certain song:")
print(get_song('A2A2T2'))

# Creating playists
create_playlist("All of Artist 2")
create_playlist("All of Genre 2")
# Testing creation of existing playlist
create_playlist("All of Artist 2")
# Printing empty playlists
print("Empty playlists that exist:")
for playlist in playlist_dictionary:
    print(playlist)

# Populating playlists
add_song_to_playlist("A2A1T1", "All of Artist 2")
add_song_to_playlist("A2A1T2", "All of Artist 2")
add_song_to_playlist("A2A1T3", "All of Artist 2")
add_song_to_playlist("A2A2T1", "All of Artist 2")
add_song_to_playlist("A2A2T2", "All of Artist 2")
add_song_to_playlist("A2A2T3", "All of Artist 2")

add_song_to_playlist("A2A2T1", "All of Genre 2")
add_song_to_playlist("A2A2T2", "All of Genre 2")
add_song_to_playlist("A2A2T3", "All of Genre 2")
add_song_to_playlist("A3A1T3", "All of Genre 2")

# Testing song updating with songs in playlists
update_song("Update artist", "Update Album", "A2A2T2", "Update Genre")
# Printing song list
print("All songs in song_list after updated song:")
for song in song_list:
    print(song)
# Print playlists with updated song
print("Print playlists with updated song:")
for playlist, songs in playlist_dictionary.items():
    print(playlist)
    for song in songs:
        print(song)

# Deleting song
delete_song(title = "A2A2T3")
# Printing song list
print("All songs in song_list after deleting song:")
for song in song_list:
    print(song)
# Print playlists after deleting song
print("Print playlists with deleted song:")
for playlist, songs in playlist_dictionary.items():
    print(playlist)
    for song in songs:
        print(song)

# Updating a playlist name
update_playlist("All of Genre 2", "Genre 2 and Updated")
# Printing playlists after playlist update
print("Print playlists after updating playlist name:")
print(playlist_dictionary.keys())

# Removing song from playlist
remove_song_from_playlist("A2A2T2", "All of Artist 2")
# Printing playlist after deleting song from playlist
print("Printing songs in playlist after deleting song from playlist")
for song in playlist_dictionary["All of Artist 2"]:
    print(song)

# Playlist sorting test
create_playlist("Sorting Playlist")
add_song_to_playlist("A3A1T3", "Sorting Playlist")
add_song_to_playlist("A1A1T1", "Sorting Playlist")
add_song_to_playlist("A3A1T1", "Sorting Playlist")
add_song_to_playlist("A2A2T1", "Sorting Playlist")

# Sorting by each sort option (title, album, genre)
# title
sort_playlist(playlist_dictionary["Sorting Playlist"], 'title')
print("Printing songs in Sorting Playlist after sorting by title:")
for song in playlist_dictionary["Sorting Playlist"]:
    print(song)
# genre
sort_playlist(playlist_dictionary["Sorting Playlist"], 'genre')
print("Printing songs in Sorting Playlist after sorting by genre:")
for song in playlist_dictionary["Sorting Playlist"]:
    print(song)
# album
sort_playlist(playlist_dictionary["Sorting Playlist"], 'album')
print("Printing songs in Sorting Playlist after sorting by album:")
for song in playlist_dictionary["Sorting Playlist"]:
    print(song)


if __name__ == '__main__':
    app.run(debug=True)