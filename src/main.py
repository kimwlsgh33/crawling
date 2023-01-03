import youtube

# url = input('Enter a YouTube URL: ')
url = 'https://www.youtube.com/watch?v=m4ZVHMoPcnc'

yt = youtube.get_data(url)

# 메뉴를 출력하고 사용자로부터 원하는 타입을 입력 받는다.
type = youtube.stream_type_menu()

# 사용자가 입력한 값을 이용해, 해당 타입의 스트림을 출력
stream = youtube.stream_menu(yt, type)

# 스트림을 다운로드
youtube.download(stream)
