import string
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Cargar datos desde el archivo CSV
data = pd.read_csv('IMDB Dataset.csv')

# Echar un vistazo a los primeros registros para entender su estructura
print(data.head())

data = data.dropna(subset=['review', 'sentiment'])


# Descargar las stop words
nltk.download('stopwords')
nltk.download('punkt')

# Función para limpiar y procesar el texto
def clean_text(text):
    text = text.lower()  # convertir a minúsculas
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)  # eliminar puntuación
    text = re.sub(r'\w*\d\w*', '', text)
    tokens = word_tokenize(text)  # tokenización
    tokens = [word for word in tokens if word not in stopwords.words('english')]  # eliminar stop words
    return tokens

# Aplicar la función de limpieza a cada reseña
data['processed_review'] = data['review'].apply(lambda x: clean_text(x))


