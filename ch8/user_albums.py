def make_album(artist, title, num_songs=None):
    """Returns a dictionary of artist name, album title, and number of songs."""
    return {'artist_name': artist, 'album_title': title, 'number_of_songs': num_songs}


while True:
    print("Please enter the details of the album.")
    print("(enter 'q' at any time to quit.")

    artist = input('Enter artist name: ')
    if artist == 'q':
        break
    title = input('Enter album title: ')
    if title == 'q':
        break
    num_songs = input('Enter the number of songs in the album: ')
    if num_songs == 'q':
        break
    print(make_album(artist, title, num_songs))
