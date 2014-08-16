from get_top_genre import get_top_genre
from get_genre_instruments import get_genre_instruments
from get_tag_video import get_tag_video

'''
Given a song, this example will illustrate how to get a video for each one of the most representative instruments of the song's music genre
'''

artist = "Mos Def"
title = "Oh No"

#Get the top genre of the song
genre = get_top_genre(artist, title)
print genre

#Get the genre's most representative instruments
instruments = get_genre_instruments(genre)
print instruments

#Get a Youtube videoID for each instrument
for instrument in instruments:
    videoID = get_tag_video(instrument)
    youtube_url = "https://www.youtube.com/watch?v="+videoID
    print "%s - %s" % (instrument, youtube_url)

#Get a Youtube videoID for the genre
videoID = get_tag_video(genre)
youtube_url = "https://www.youtube.com/watch?v="+videoID
print "%s - %s" % (genre, youtube_url)