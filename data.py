import pandas as pd

# Cargar datos desde el archivo CSV
data = pd.read_csv('IMDB Dataset.csv')

# Echar un vistazo a los primeros registros para entender su estructura
print(data.head())

data = data.dropna(subset=['review', 'sentiment'])

