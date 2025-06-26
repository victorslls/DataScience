import pandas as pd
from sklearn.preprocessing import LabelEncoder

def carregar_dados(caminho):
    return pd.read_csv(caminho)

def tratar_nulos(df):
    return df.dropna()

def codificar_variaveis(df, colunas):
    encoder = LabelEncoder()
    for col in colunas:
        df[col] = encoder.fit_transform(df[col])
    return df

def salvar_dados(df, caminho):
    df.to_csv(caminho, index=False)