import ffmpeg_streaming
import youtube_dl
from ffmpeg_streaming import Formats


def extractVideoFormats(input):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
    with ydl:
        result = ydl.extract_info(input, download=False)
    if 'entries' in result:
        video = result['entries'][0]
    else:
        video = result

    return video


def convertHLStoMP4(input, output):
    video = ffmpeg_streaming.input(input)
    stream = video.stream2file(Formats.h264())
    stream.output(output)
    return output
