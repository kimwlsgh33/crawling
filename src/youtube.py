from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# yt = YouTube('https://www.youtube.com/watch?v=m4ZVHMoPcnc')

def get_data(url):
    yt = YouTube(url)
    return yt

####################################################################################################
def stream_type_menu():
    print('Choose a stream type:')
    print('0: Video and Audio')
    print('1: Video')
    print('2: Audio')
    print('3: Mp4')
    return int(input())

def get_normal_stream(yt):
    return yt.streams.filter(progressive=True)

def get_adaptive_stream(yt):
    return yt.streams.filter(adaptive=True)

def get_audio_stream(yt):
    return yt.streams.filter(only_audio=True)

def get_mp4_stream(yt):
    return yt.streams.filter(file_extension='mp4')
####################################################################################################

def stream_menu(yt, type):
    streams = []
    if type == 0:
        streams = get_normal_stream(yt)
    elif type == 1:
        streams = get_adaptive_stream(yt)
    elif type == 2:
        streams = get_audio_stream(yt)
    elif type == 3:
        streams = get_mp4_stream(yt)
    print('Choose a stream:')
    for i in range(len(streams)):
        print(str(i) + ': ' + str(streams[i]))
    # enumerate : 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아, 인덱스 값을 포함하는 enumerate 객체를 리턴
    # for i, stream in enumerate(streams):
    selected = int(input())
    return streams[selected]

def download(stream):
    print('Downloading...')
    stream.download()
    print('Downloaded!')
