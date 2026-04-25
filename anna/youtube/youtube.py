# autor : anna
# projeto sistema para 
# download de videos do youtube 

# import dos recursos da biblioteca
from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input('digite a url do video')
yt = YouTube(url,on_progress_callback=on_progress)
ys = yt.streams.get_highest_resolution()
print("baixando vídeo")
ys.download()
print("download concluído com sucesso!")