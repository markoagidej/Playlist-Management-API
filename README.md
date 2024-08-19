# Playlist Management API by Marko Gidej
This app allows the user to manage songs and playlists by using a RESTful API built with Flask.
There are 2 main data structure in the program, a song list and a playlist list.
The song list contains every song that can be used in the program.
Playlists contain a list chhosen of songs from the main song list.

Setup instructions are at the end of this readme.

You can do the folling operations:
1. Songs
    1.1 - Create a song
    1.2 - Update a song
    1.3 - Delete a song
    1.4 - Get a song
2. Playlists
    2.1 - Create a playlist
    2.2 - Update a playlist
    2.3 - Delete a playlist
    2.4 - Get a playlist
    2.5 - Add a song to a playlist
    2.6 - Remove a song from a playlist
    2.7 - Sort a playlist

# 1. Songs
## 1.1 - Create a song
To create a song you need 4 parameters: artist, album, title, and genre.
## 1.2 - Update a song
To update a song, you identify it by it's title, and you provide a new artist, album, and genre. These updates will effect all songs in all playlists.
## 1.3 - Delete a song
To delete a song, you can either use the title or a full song object. When you delete a song, it is deleted from teh song list and all playlists.
## 1.4 - Get a song
You can get a song by using its title, and this will return a song object.
# 2. Playlists
## 2.1 - Create a playlist
All you need to create a playlist is a name for the playlist.
## 2.2 - Update a playlist
To update the name of a playlist, enter the old name and new name.
## 2.3 - Delete a playlist
Using the name of a playlist, remove that playlist from the program. The songs in the playlist will remain in the song list.
## 2.4 - Get a playlist
Using the name of a playlist, return the name and songlist of a playlist.
## 2.5 - Add a song to a playlist
Add a song by title to a playlist of a name.
## 2.6 - Remove a song from a playlist
By song title, remove the first instance of that song in a playlist of a specified name.
## 2.7 - Sort a playlist
A specific playlist can have it's songs sorted by any song parameter.

# Setup
To set this up, create a virtual enviorment and place thes files in it. You will have to "pip install flask" in your console.