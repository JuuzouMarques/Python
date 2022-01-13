from pytube import YouTube

print('-'*20)
print('YOUTUBE DOWNLOADER')
print('-'*20)
link = input('Enter URL of video: ')
video = YouTube(link)
stream = video.streams.get_highest_resolution()
print('Downloading...')
stream.download()
print('\033[1;32mDownload Completed\033[m')
