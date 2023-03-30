# # from pydub import AudioSegment

# # # Chargement du fichier MP3
# # audio = AudioSegment.from_file('audioFile.mp3')


# # # Liste des timestamps pour chaque verset
# # timestamps = [
# #     (0, 5000), # Timestamp pour le premier verset (0 à 5 secondes)
# #     (5000, 10000), # Timestamp pour le deuxième verset (5 à 10 secondes)
# #     # Ajouter d'autres timestamps pour les autres versets...
# # ]

# # # Boucle sur chaque timestamp pour extraire chaque verset
# # for i, ts in enumerate(timestamps):
# #     start, end = ts
# #     # Extraction du verset courant
# #     extract = audio[start:end]
# #     # Sauvegarde du fichier extrait avec un nom de fichier correspondant au numéro du verset
# #     extract.export(f"verset_{i+1}.mp3", format="mp3")



# from pydub import AudioSegment
# from pydub.silence import split_on_silence
# import os



# ##NOTE 110th Sourate Issues !!!
# id = "114"

# # Chargement du fichier MP3
# audio = AudioSegment.from_file('C:/Users/Adlane/Desktop/Projects/Medina-App/Ressources/Coran-MP3-Mishary-Al-Afasi/' + id +'.mp3')

# # Conversion en audio mono
# audio = audio.split_to_mono()[0]

# # Définition des paramètres pour la division en fonction du niveau de dB et de la durée du silence
# dBFS = -22  # niveau de dB
# min_silence_len = 450  # durée minimale du silence en ms

# # Division du fichier audio en plusieurs parties en fonction du niveau de dB et de la durée du silence
# #, keep_silence=min_silence_len
# segments = split_on_silence(audio, min_silence_len=min_silence_len, silence_thresh=dBFS)
# os.mkdir('./../' + id )
# # Sauvegarde de chaque partie dans un fichier audio séparé
# for i, segment in enumerate(segments):
#     segment.export(f"./../{id}/part_{i+1}.mp3", format="mp3")


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
# print(timestamps)

VersetsTs = [0]

for i in range(len(timestamps)):
    VersetsTs.append(timestamps[i][1])
    
    
print (VersetsTs)

