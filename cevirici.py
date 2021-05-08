from mtranslate import translate
import pandas as pd

df = pd.read_csv('input.csv', header= None, sep = ';')
cevirilmis = []

for yorum in df['orijinal']:
    cevirilmis.append(translate(yorum, "en","tr"))
