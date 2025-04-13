def make_album(artist, album_name, tracks):
    album = {'artist': artist, 'album_name': album_name, 'tracks': tracks}
    return album

def add_tracks(album, new_tracks):
    album['tracks'].extend(new_tracks)
    #extend()方法用于在列表末尾一次性追加另一个序列中的多个值
    return album

def remove_tracks(album, track_indices):
    for index in sorted(track_indices, reverse=True):
        #sorted()方法用于对序列进行排序，reverse=True表示降序排序
        del album['tracks'][index]#del语句用于删除列表中的元素
    return album

album = make_album('The Beatles', 'Abbey Road', ['Please Please Me', 'With the Beatles', 'A Hard Day\'s Night'])
print(album)

album = add_tracks(album, ['Beatles for Sale', 'Twist and Shout'])
print(album)

album = remove_tracks(album, [1, 2])
print(album)

while True:
    print('Please enter the command:')
    command = input()
    if command == 'exit':
        break
    elif command == 'add_tracks':
        new_tracks = input('Enter new tracks separated by comma:').split(',')#split()方法用于分割字符串，并返回列表
        album = add_tracks(album, new_tracks)
        print(album)
    elif command =='remove_tracks':
        track_indices = input('Enter track indices separated by comma:').split(',')
        track_indices = [int(index) for index in track_indices]
        album = remove_tracks(album, track_indices)
        print(album)
    else:
        print('Invalid command')