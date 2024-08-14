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
    delete_song(song_to_update)
    new_song = create_song(artist, album, title, genre)
    for playlist in playlist_dictionary.values():
        for song in playlist:
            if song == song_to_update:
                song = new_song

def delete_song(song):
    song_list.remove(song)
    for playlist in playlist_dictionary.values():
        while song in playlist:
            playlist.remove(song)

def get_song(title):
    for song in song_list:
        if song['title'] == title:
            return song

# Playlists
def create_playlist(name):
    if not playlist_dictionary[name]:
        playlist_dictionary[name] = []
    else:
        print(f"Playlist titled '{name}' already exists!")

def update_playlist(name):
    playlist_to_update, song_list = get_playlist(name)
    playlist_dictionary[name] = song_list
    delete_playlist(playlist_to_update)

def get_playlist(name):
    return name, playlist_dictionary[name]

def delete_playlist(name):
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

def sort_playlist(playlist_name, sort_category):
    song_list = playlist_dictionary[playlist_name]
    if len(song_list) > 1:
        mid = len(song_list) // 2
        left = song_list[:mid]
        right = song_list[mid:]

        sort_playlist(left)
        sort_playlist(right)

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
    delete_song(create_song(data['artist'], data['album'], data['title'], data['genre']))
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
@app.route('/playlists', methods=['PUT'])
def updatePlaylist():
    data = request.get_json()
    update_playlist(data['name'])
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
@app.route('/playlists/<string:playlist_name>', methods=['PUT'])
def sortPlaylist(playlist_name):
    data = request.get_json()
    sort_playlist(playlist_name, data['sort_category'])

if __name__ == '__main__':
    app.run(debug=True)