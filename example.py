# -*- coding: utf-8 -*-

# This file is part of AutoVJ.
#
# AutoVJ is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# AutoVJ is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with AutoVJ.  If not, see <http://www.gnu.org/licenses/>.

# Written by Mohamed Sordo (@neomoha)
# Email: mohamed ^dot^ sordo ^at^ gmail ^dot^ com
# Website: http://msordo.weebly.com

from get_top_genre import get_top_genre
from get_genre_instruments import get_genre_instruments
from get_tag_video import get_tag_video

'''
Given a song, this example will illustrate how to get a video for each one of
the most representative instruments of the song's music genre
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