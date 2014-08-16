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