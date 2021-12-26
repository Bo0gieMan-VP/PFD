import os
import json
import lyricsgenius
import requests
from lxml import html
from server import get_string

BAD_ALBUM_WORDS = [
    'live',
    'the later years',
    'delicate sound of thunder',
    'work in progress',
    'the best',
    'collection',
    'film',
    'works',
    'complete',
    'relics',
    'early',
    'shine on',
    'pulse',
    'pair',
    'julia',
    'apples',
    'arnold'
] + [i for i in "0123456789()[]"]

# Pink Floyd ID - 694

def clean_name(name):
    found = False
    special_characters = "!@#$%^&*()+'?_=,:.<>/"
    for i in range(len(name)):
        if name[i] in special_characters:
            name = name[0:i] + name[i+1:]
            found = True
            break
    if found:
        name = clean_name(name)
    return name

def get_lyrics_from_web(path):
    uri = f'https://genius.com' + path
    page = requests.get(uri)
    tree = html.fromstring(page.content)
    ID = tree.xpath("/html/body/div[1]/main/div[2]/div[2]/div[2]/div/div[not(contains(@class, 'ShareButtons__Root-jws18q-0')) "
                    "and not(contains(@class, 'Lyrics__Footer-sc-1ynbvzw-2')) ]//text()")
    lyrics = ""
    for i in ID:
        lyrics += i + "\n"
    return lyrics

genius = lyricsgenius.Genius(access_token='mviROzWLzm_ygPnLMVaghIXr5xEPCPFUfWi_zZQTR5tGTap6PU6Me34impgkXpIO',
                             excluded_terms=["Remix", "Live"], remove_section_headers=True, verbose=False)

def update_db():
    print(get_string('GENIUS', "Gathering information..."))
    pink_floyd = {}
    counter = 0
    albums = genius.artist_albums(artist_id=694, per_page=50)
    for album in albums['albums']:
        name = album['name'].replace("/", "")
        if 'more' in name.lower():
            name = 'More'

        if not any(word in name.lower() for word in BAD_ALBUM_WORDS):
            album_info = {'name': name, 'id': album['id']}
            pink_floyd[counter] = album_info
            counter += 1
    del albums, album_info

    print(get_string('GENIUS', "Got all albums"))

    for album in pink_floyd.keys():
        songs = genius.album_tracks(album_id=pink_floyd[album]['id'])
        songs_ids = {}
        for song in songs['tracks']:
            song_num = song['number']
            name = song['song']['title'].replace('\xa0', ' ')
            songs_ids[song_num] = {name: song['song']['id'] , 'path' : song['song']['path']}
        pink_floyd[album]['songs'] = songs_ids
    del songs, songs_ids, song, album, song_num, name

    print(get_string('GENIUS', "Got all songs"))

    with open('genius_database.json', 'w') as f:
        json_data = json.dumps(pink_floyd, indent=4)
        f.write(json_data)

    create_database()

def create_database():
    with open('genius_database.json', 'r') as f:
        pink_floyd_db = json.loads(f.read())

    print(get_string('GENIUS', "Working on lyrics..."))
    for album in pink_floyd_db.keys():
        album_name = clean_name(pink_floyd_db[album]['name'])
        if not os.path.exists('albums_genius/' + album_name):
            os.mkdir('albums_genius/' + album_name)
        for (song_num, value) in pink_floyd_db[album]['songs'].items():
            songname, path = list(value.keys())[0], list(value.values())[1]
            if not os.path.exists('albums_genius/' +album_name + "/" + clean_name(songname) + ".txt"):
                lyrics = get_lyrics_from_web(path)
                with open('albums_genius/' +album_name + "/" + clean_name(songname) + ".txt", 'w') as f:
                    f.write(lyrics)
    print(get_string('GENIUS', "Done updating!"))

def fix_file_names():
    for folder in os.listdir('albums_genius'):
        try:
            os.chdir('albums_genius')
        except:
            pass
        for file in os.listdir(folder):
            try:
                os.chdir(folder)
            except:
                pass
            new_name = file.replace(" by Pink Floyd", "")
            os.rename(file, new_name)
        os.chdir("..")

def main():
   # create_database()
    pass

if __name__ == "__main__":
    main()