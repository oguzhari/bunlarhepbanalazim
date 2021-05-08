import pandas as pd
#sürekli baslik yazmaktan kurtulmak için, header none. 
df = pd.read_csv('input.csv', sep=';', header=None ) 