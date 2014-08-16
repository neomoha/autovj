import codecs, argparse

from apis.YoutubeAPI import YoutubeAPI

def get_tag_video(tag):
    api = YoutubeAPI()
    return api.get_tag_top_video(tag)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get the top video of a tag')
    parser.add_argument('tag', help='tag (use quotes for tags with more than one word)')
    args = parser.parse_args()
    print args
    video = get_tag_video(args.tag)
    print video