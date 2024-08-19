from flask import Flask, jsonify, request
import helpers

app = Flask(__name__)

# Task 1: Data Organization with Lists and Dictionaries:
song_list = []
playlist_dictionary = {}

# Task 3: Building a Flask API for Playlist Access and Management:
## Song Engpoints
# Create Song
@app.route('/songs', methods=['POST'])
def createSong():
    data = request.get_json()
    song = helpers.create_song(song_list, data['artist'], data['album'], data['title'], data['genre'])
    return jsonify(song)
# Update Song
@app.route('/songs', methods=['PUT'])
def updateSong():
    data = request.get_json()
    helpers.update_song(song_list, playlist_dictionary, data['artist'], data['album'], data['title'], data['genre'])
    return jsonify({"success": "Song updated"})
# Delete Song
@app.route('/songs/<string:title>', methods=['DELETE'])
def deleteSong(title):
    helpers.delete_song(song_list, playlist_dictionary, title = title)
    return jsonify({"success": "Song deleted"})
# Seach/Get Song
@app.route('/songs/<string:title>', methods=['GET'])
def getSong(title):
    return jsonify(helpers.get_song(song_list, title))

## Playlist Endpoints
# Create Playlist
@app.route('/playlists', methods=['POST'])
def sortPlaylist():
    data = request.get_json()
    helpers.create_playlist(playlist_dictionary, data['name'])
    return jsonify({"success": "Playlist created"})
# Get Playlist
@app.route('/playlists/<string:name>', methods=['GET'])
def getPlaylist(name):
    return jsonify(helpers.get_playlist(playlist_dictionary, name))
# Update Playlist
@app.route('/playlists/<string:playlist_name>', methods=['PUT'])
def updatePlaylist(playlist_name):
    data = request.get_json()
    helpers.update_playlist(playlist_dictionary, playlist_name, data['name'])
    return jsonify({"success": "Playlist updated"})
# Delete Playlist
@app.route('/playlists/<string:name>', methods=['DELETE'])
def deletePlaylist(name):
    helpers.delete_playlist(playlist_dictionary, name)
    return jsonify({"success": "Playlist deleted"})

## Additional Endpoints:
# Add song to Playlist
@app.route('/playlists/<string:playlist_name>', methods=['POST'])
def addToPlaylist(playlist_name):
    data = request.get_json()
    song_title = (data['song_title'])
    helpers.add_song_to_playlist(song_list, playlist_dictionary, song_title, playlist_name)
    return jsonify({"success": "Song added to Playlist"})
# Remove song from Playlist
@app.route('/playlists/<string:playlist_name>', methods=['DELETE'])
def removeFromPlaylist(playlist_name):
    data = request.get_json()
    song_title = (data['song_title'])
    helpers.remove_song_from_playlist(song_list, playlist_dictionary, song_title, playlist_name)
    return jsonify({"success": "Song removed from Playlist"})
# Sort songs in Playlist by song name, genre, and artist
@app.route('/playlists/sort/<string:playlist_name>', methods=['PUT'])
def sortSelectedPlaylist(playlist_name):
    data = request.get_json()
    helpers.sort_playlist(playlist_name, data['sort_category'])
    return jsonify({"success": "Playlist sorted"})

# Testing
# Creating songs
helpers.create_song(song_list, "Artist 1", "Album 1", "A1A1T1", "Genre 1")
helpers.create_song(song_list, "Artist 1", "Album 1", "A1A1T2", "Genre 1")
helpers.create_song(song_list, "Artist 1", "Album 1", "A1A1T3", "Genre 1")

helpers.create_song(song_list, "Artist 2", "Album 1", "A2A1T1", "Genre 1")
helpers.create_song(song_list, "Artist 2", "Album 1", "A2A1T2", "Genre 1")
helpers.create_song(song_list, "Artist 2", "Album 1", "A2A1T3", "Genre 1")

helpers.create_song(song_list, "Artist 2", "Album 2", "A2A2T1", "Genre 2")
helpers.create_song(song_list, "Artist 2", "Album 2", "A2A2T2", "Genre 2")
helpers.create_song(song_list, "Artist 2", "Album 2", "A2A2T3", "Genre 2")

helpers.create_song(song_list, "Artist 3", "Album 1", "A3A1T1", "Genre 3")
helpers.create_song(song_list, "Artist 3", "Album 1", "A3A1T2", "Genre 4")
helpers.create_song(song_list, "Artist 3", "Album 1", "A3A1T3", "Genre 2")

# Printing song list
print("All songs in song_list:")
for song in song_list:
    print(song)

# Printing result of helpers.get_song(song_list, )
print("\nPrinting certain song:")
print(helpers.get_song(song_list, 'A2A2T2'))

# Creating playists
helpers.create_playlist(playlist_dictionary, "All of Artist 2")
helpers.create_playlist(playlist_dictionary, "All of Genre 2")
# Testing creation of existing playlist
helpers.create_playlist(playlist_dictionary, "All of Artist 2")
# Printing empty playlists
print("Empty playlists that exist:")
for playlist in playlist_dictionary:
    print(playlist)

# Populating playlists
helpers.add_song_to_playlist(song_list, playlist_dictionary, "A2A1T1", "All of Artist 2")
helpers.add_song_to_playlist(song_list, playlist_dictionary, "A2A1T2", "All of Artist 2")
helpers.add_song_to_playlist(song_list, playlist_dictionary, "A2A1T3", "All of Artist 2")
helpers.add_song_to_playlist(song_list, playlist_dictionary, "A2A2T1", "All of Artist 2")
helpers.add_song_to_playlist(song_list, playlist_dictionary, "A2A2T2", "All of Artist 2")
helpers.add_song_to_playlist(song_list, playlist_dictionary, "A2A2T3", "All of Artist 2")

helpers.add_song_to_playlist(song_list, playlist_dictionary, "A2A2T1", "All of Genre 2")
helpers.add_song_to_playlist(song_list, playlist_dictionary, "A2A2T2", "All of Genre 2")
helpers.add_song_to_playlist(song_list, playlist_dictionary, "A2A2T3", "All of Genre 2")
helpers.add_song_to_playlist(song_list, playlist_dictionary, "A3A1T3", "All of Genre 2")

# Testing song updating with songs in playlists
helpers.update_song(song_list, playlist_dictionary, "Update artist", "Update Album", "A2A2T2", "Update Genre")
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
helpers.delete_song(song_list, playlist_dictionary, title = "A2A2T3")
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
helpers.update_playlist(playlist_dictionary, "All of Genre 2", "Genre 2 and Updated")
# Printing playlists after playlist update
print("Print playlists after updating playlist name:")
print(playlist_dictionary.keys())

# Removing song from playlist
helpers.remove_song_from_playlist(song_list, playlist_dictionary, "A2A2T2", "All of Artist 2")
# Printing playlist after deleting song from playlist
print("Printing songs in playlist after deleting song from playlist")
for song in playlist_dictionary["All of Artist 2"]:
    print(song)

# Playlist sorting test
helpers.create_playlist(playlist_dictionary, "Sorting Playlist")
helpers.add_song_to_playlist(song_list, playlist_dictionary, "A3A1T3", "Sorting Playlist")
helpers.add_song_to_playlist(song_list, playlist_dictionary, "A1A1T1", "Sorting Playlist")
helpers.add_song_to_playlist(song_list, playlist_dictionary, "A3A1T1", "Sorting Playlist")
helpers.add_song_to_playlist(song_list, playlist_dictionary, "A2A2T1", "Sorting Playlist")

# Sorting by each sort option (title, album, genre)
# title
helpers.sort_playlist(playlist_dictionary["Sorting Playlist"], 'title')
print("Printing songs in Sorting Playlist after sorting by title:")
for song in playlist_dictionary["Sorting Playlist"]:
    print(song)
# genre
helpers.sort_playlist(playlist_dictionary["Sorting Playlist"], 'genre')
print("Printing songs in Sorting Playlist after sorting by genre:")
for song in playlist_dictionary["Sorting Playlist"]:
    print(song)
# album
helpers.sort_playlist(playlist_dictionary["Sorting Playlist"], 'album')
print("Printing songs in Sorting Playlist after sorting by album:")
for song in playlist_dictionary["Sorting Playlist"]:
    print(song)


if __name__ == '__main__':
    app.run(debug=True)