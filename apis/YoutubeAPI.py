from apiclient.discovery import build
from apiclient.errors import HttpError

import config
from VideoAPI import VideoAPI

class YoutubeAPI(VideoAPI):
    def __init__(self):
        self.api = build(config.YOUTUBE_API_SERVICE_NAME, config.YOUTUBE_API_VERSION, developerKey=config.YOUTUBE_API_KEY)
    
    def get_tag_top_video(self, tag):
        try:
            search_response = self.api.search().list(
                q=tag,
                part="id,snippet",
                maxResults=1
            ).execute()
            for search_result in search_response.get("items", []):
                if search_result["id"]["kind"] == "youtube#video":
                    return search_result["id"]["videoId"]
        except HttpError, e:
            print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
        return None