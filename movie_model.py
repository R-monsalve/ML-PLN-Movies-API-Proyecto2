import joblib

pipeline = joblib.load('pipeline_generos.pkl')
mlb = joblib.load('mlb_generos.pkl')

def predecir_generos(title: str, plot: str):
    texto = title + ' ' + plot
    proba = pipeline.predict_proba([texto])[0]
    resultado = {
        'p_' + genre: round(float(prob), 4)
        for genre, prob in zip(mlb.classes_, proba)
    }
    return resultado