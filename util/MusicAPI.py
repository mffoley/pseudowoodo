import urllib.request
import json
import random

#another key: f5362a758e0fb53042df13ded7a45825
# the key: 13ac239b500b6542edd7120afe6078e1

key = "f5362a758e0fb53042df13ded7a45825"

def get_song(genre):
    try:
        baseurl = "http://api.musixmatch.com/ws/1.1/"
        #f=open("./MusicKey.txt","r")
        #s=f.read().rsplit("\n")
        #f.close()
        url = baseurl+"track.search?f_lyrics_language=en&f_music_genre_id=" + genre + '&apikey=' + key

        httpresponse = urllib.request.urlopen(url) #this is initial httpresponse
        readresponse = httpresponse.read() #we are reading response
        decodedresponse = readresponse.decode() #we decode it for the json to load later
        #print(readresponse)

        data = json.loads(decodedresponse)['message']['body']['track_list']

        #print(data)

        song_choice = random.choice(data)

        #print(song_choice)

        #body = data["message"]["body"]["track_list"][0]["track"]["track_name"]
        return song_choice

    except Exception as e:
        raise


def get_genres():
    try:
        #f=open("./MusicKey.txt","r")
        #s=f.read().rsplit("\n")
        #f.close()
        baseurl = "http://api.musixmatch.com/ws/1.1/"
        url = baseurl +"music.genres.get?apikey="+key

        httpresponse = urllib.request.urlopen(url) #this is initial httpresponse
        readresponse = httpresponse.read() #we are reading response
        decodedresponse = readresponse.decode() #we decode it for the json to load later

        data = json.loads(decodedresponse)

        genres = []
        genres_encoded = []

        list = data['message']['body']['music_genre_list']

        for genre in list:
            if genre['music_genre']['music_genre_id'] != 34:
                genres.append(genre['music_genre']['music_genre_name'])
                genres_encoded.append(genre['music_genre']['music_genre_id'])

        return genres, genres_encoded

    except:
        raise


get_song('1086')
