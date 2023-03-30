
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
segments = split_on_silence(audio, min_silence_len=min_silence_len, silence_thresh=dBFS)

# Obtention des timestamps de début et de fin de chaque segment silencieux
timestamps = []
prev_end = 0
for segment in segments:
    start = prev_end + len(segment)  # timestamp de début
    end = start + min_silence_len  # timestamp de fin
    timestamps.append([start, end])
    prev_end = end

# Affichage des timestamps

#On Commence à 0
VersetsTs = [0]

for i in range(len(timestamps)):
#On récupere la fin du silence qui correspond donc au début du prochain verset
    VersetsTs.append(timestamps[i][1])
print (VersetsTs)

