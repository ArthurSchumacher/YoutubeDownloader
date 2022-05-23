from pytube import YouTube
import moviepy.editor

path = 'C:\\Users\\Arthur Schumacher\\Documents\\Code\\Python\\Projects\\YoutubeDownloader'

with open('Python\Projects\YoutubeDownloader\links.txt', 'r+') as arquivo:
    for musica in arquivo:
        yt = YouTube(str(musica))

        print('Baixando: ', yt.title)

        ys = yt.streams.get_highest_resolution()
        ys.download(path + '\\videos\\')

        video = moviepy.editor.VideoFileClip(path + '\\videos\\' + yt.title + '.mp4')
        audioData = video.audio
        audioData.write_audiofile(path + '\\musicas\\' + yt.title + '.mp3')
