from pydub import AudioSegment
from pydub.silence import split_on_silence
import os


##NOTE 110th Sourate Issues !!!
id = "114"

# Chargement du fichier MP3
audio = AudioSegment.from_file('C:/Users/Adlane/Desktop/Projects/Medina-App/Ressources/Coran-MP3-Mishary-Al-Afasi/' + id +'.mp3')

# Conversion en audio mono
audio = audio.split_to_mono()[0]

# Définition des paramètres pour la division en fonction du niveau de dB et de la durée du silence
dBFS = -22  # niveau de dB
min_silence_len = 450  # durée minimale du silence en ms

# Division du fichier audio en plusieurs parties en fonction du niveau de dB et de la durée du silence
#, keep_silence=min_silence_len
segments = split_on_silence(audio, min_silence_len=min_silence_len, silence_thresh=dBFS)
os.mkdir('./../' + id )
# Sauvegarde de chaque partie dans un fichier audio séparé
for i, segment in enumerate(segments):
    segment.export(f"./../{id}/part_{i+1}.mp3", format="mp3")

