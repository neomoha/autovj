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