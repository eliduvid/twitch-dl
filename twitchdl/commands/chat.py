from twitchdl import utils
from twitchdl.twitch import get_video_chat


def chat(args):
    video_id = utils.parse_video_identifier(args.video)
    chat = get_video_chat(video_id)
    from pprint import pprint
    pprint(chat)
