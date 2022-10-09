import pytube



save_path='django'
video_link='https://www.youtube.com/watch?v=P9-4xHVc7uk&list=RDMML2Ir7tDK3Mg&index=11'
playlist_link='https://www.youtube.com/playlist?list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh'
# -------------------------------------------------------------------------------------------
# 1 video
def download_video(link):
    link = pytube.YouTube(link)
    try:
        link.streams.filter(res='720p').first().download()
        print(link.title)
        print("ok")
    except :
        print(link.title)
        print('nope')

# -----------------------------------------------------------------------------------------
# Play list
def download_playlist(link):
    p=pytube.Playlist(link)
    print('download:  %s' %(p.title))
    for video in p.videos:
        video.streams.filter(res='720p',file_extension='mp4').first().download(output_path=save_path)
        print(video.title)

if __name__=='__main__':
    download_playlist(playlist_link)