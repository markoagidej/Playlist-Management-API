# Songs
def create_song(song_list, artist, album, title, genre):
    new_song = {
                    'artist': artist,
                    'album': album,
                    'title': title,
                    'genre': genre
                }
    if new_song in song_list:
        print("Song already exists!")
    else:
        song_list.append(new_song)
        return new_song

def update_song(song_list, playlist_dictionary, artist, album, title, genre):
    song_to_update = get_song(song_list, title)
    if song_to_update:
        new_song = create_song(song_list, artist, album, title, genre)
        if new_song:
            for playlist, songList in playlist_dictionary.items():
                for song in songList:
                    if song == song_to_update:
                        playlist_dictionary[playlist].append(new_song)
            delete_song(song_list, playlist_dictionary, song = song_to_update)

def delete_song(song_list, playlist_dictionary, **kwargs):
    song = kwargs.get("song", None)
    title = kwargs.get("title", None)
    if song:
        song_list.remove(song)
        for playlist in playlist_dictionary.values():
            while song in playlist:
                playlist.remove(song)
    elif title:
        song = get_song(song_list, title)
        if song:
            delete_song(song_list, playlist_dictionary, song = song)

def get_song(song_list, title):
    for song in song_list:
        if song['title'] == title:
            return song
        else:
            print(f"No song found with title of: {title}")

# Playlists
def create_playlist(playlist_dictionary, name):
    if name in playlist_dictionary:
        print(f"Playlist titled '{name}' already exists!")
    else:
        playlist_dictionary[name] = []

def update_playlist(playlist_dictionary, old_name, new_name):
    playlist_to_update, song_list = get_playlist(playlist_dictionary, old_name)
    if playlist_to_update:
        playlist_dictionary[new_name] = song_list
        delete_playlist(playlist_dictionary, playlist_to_update)

def get_playlist(playlist_dictionary, name):
    if name in playlist_dictionary:
        return name, playlist_dictionary[name]
    else:
        print(f"No playlist found with name of \"{name}\"")

def delete_playlist(playlist_dictionary, name):
    if name in playlist_dictionary:
        del playlist_dictionary[name]
    else:
        print(f"No playlist found with name of \"{name}\"")

# Song/Playlist interactions
def add_song_to_playlist(song_list, playlist_dictionary, song_title, playlist_name):
    song_to_add = get_song(song_list, song_title)
    playlist = get_playlist(playlist_dictionary, playlist_name)[1]
    if song_to_add and playlist:
        playlist.append(song_to_add)
        playlist_dictionary[playlist_name] = playlist
        print(f"{song_title} added to playlist: {playlist_name}")

def remove_song_from_playlist(song_list, playlist_dictionary, song_title, playlist_name):
    song = get_song(song_list, song_title)
    playlist = get_playlist(playlist_dictionary, playlist_name)[1]
    if song and playlist:        
        playlist_dictionary[playlist_name].remove(song)

# Task 2: Efficient Search and Sort Algorithms for Playlist Navigation:

def sort_playlist(song_list, sort_category):
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