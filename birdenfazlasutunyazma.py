import  pandas as pd

#birden fazla değişken olabilir
a = []
b = []

#her değişkeni dic ile 
df = pd.DataFrame[{'a': a, 'b':b}]
#dosya adı, indexing kapalı, encoding türkçe karakterler için, sep değişebilir.
df.to_csv('output.csv', index=False, encoding= 'utf-8-sig', sep='choose')