import json
import os

import requests

PINK_FLOYD_YT_ID = 'UCY2qt3dw2TQJxvBrDiYGHdQ'

def play_song(songname):
    results = requests.get(f'https://youtube.googleapis.com/youtube/v3/search?part=snippet&channelId={PINK_FLOYD_YT_ID}&maxResults=3&q={songname}&key=AIzaSyAwBFTOeeKCpFAvzOJ3wzlJD7tIiG4zCF0').json()['items']
    names = [result['snippet']['title'] for result in results]
    has_official = any('official' in name.lower() for name in names)
    for result in results:
        if result['snippet']['channelId'] == PINK_FLOYD_YT_ID:
            if has_official:
                if 'official' in result['snippet']['title'].lower():
                    os.system(f'start /max https://www.youtube.com/watch?v={result["id"]["videoId"]}')
                    break
            else:
                os.system(f'start /max https://www.youtube.com/watch?v={result["id"]["videoId"]}')
                break



def main():
    play_song('Money')

if __name__ == "__main__":
    main()