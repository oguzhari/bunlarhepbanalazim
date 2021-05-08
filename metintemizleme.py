import pandas as pd

df = pd.read_csv('input.csv', header=None, sep =';')

with open('stopwords-tr.txt', 'r') as f:
    stop = [line.strip() for line in f]
 
df['arınmış'] = df['orijinal'].str.lower() #küçük yap
df['orijinal'] = df['orijinal'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)])) #stopwordleri çıkar
df['orijinal'] = df['orijinal'].str.replace('[^\w\s]','')