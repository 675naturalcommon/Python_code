def make_album(artist, album_name, songs):
    album = {'artist': artist, 'album_name': album_name,'songs': songs}
    return album

album = make_album('The Beatles', 'Please Please Me', ['Please Please Me', 'With the Beatles', 'A Hard Day\'s Night'])
print(album)

# Output: {'artist': 'The Beatles', 'album_name': 'Please Please Me','songs': ['Please Please Me', 'With the Beatles', 'A Hard Day\'s Night']}