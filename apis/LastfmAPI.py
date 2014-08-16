import pylast
from time import sleep

import config
from MusicMetadataAPI import MusicMetadataAPI

class LastfmAPI(MusicMetadataAPI):
    def __init__(self):
        self.network = pylast.LastFMNetwork(api_key = config.LASTFM_API_KEY, api_secret = config.LASTFM_API_SECRET)
    
    def get_track_top_tags(self, artist, title):
        lastfm_track = self.network.get_track(artist, title)
        top_tags = [(res.item.name, int(res.weight)) for res in lastfm_track.get_top_tags() if int(res.weight) > 0]
        return top_tags