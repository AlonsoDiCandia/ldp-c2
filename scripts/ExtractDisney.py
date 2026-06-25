# poblar_bd.py
import os, sys
import django
import pandas as pd 
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/c2' # Les habla su profesor, imaginen mi voz en sus mentes. Este es el path de mi computador, usted debe verificar que BASE_DIR corresponda al path de SU equipo. Recuerde que los comandos que le ayudan son pwd y ls. Recomendacion: printee harto el BASE_DIR
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "c2.settings")
django.setup()

url = 'https://api.disneyapi.dev/character'

response = requests.get(url).json()

print(response)