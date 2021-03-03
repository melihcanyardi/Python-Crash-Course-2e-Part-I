def make_album(artist, title, num_songs=None):
    """Returns a dictionary of artist name, album title, and number of songs."""
    return {'artist_name': artist, 'album_title': title, 'number_of_songs': num_songs}


print(make_album('The Jimi Hendrix Experience', 'Electric Ladyland', 16))
print(make_album('Cream', 'Disraeli Gears', 11))
print(make_album('Traffic', 'Traffic', 15))
