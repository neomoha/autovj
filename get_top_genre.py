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

import codecs, argparse

from apis.LastfmAPI import LastfmAPI

def _load_genres():
    genres = []
    with codecs.open('data/genres.tsv', 'r', 'utf-8') as f:
        genres = dict([line.strip().split("\t") for line in f])
    return genres

def _clean_tag(tag):
    return tag.lower().replace("-", "").replace(" ", "")

def get_top_genre(artist, title):
    api = LastfmAPI()
    genres = _load_genres()
    for tag in api.get_track_top_tags(artist, title):
        if _clean_tag(tag[0]) in genres:
            return tag[0]
    return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get the top genre of a track')
    parser.add_argument('artist', help='Song artist (use quotes for artist names with more than one word)')
    parser.add_argument('title', help='Song title (use quotes for song titles with more than one word)')
    args = parser.parse_args()
    print args
    genre = get_top_genre(args.artist, args.title)
    print genre