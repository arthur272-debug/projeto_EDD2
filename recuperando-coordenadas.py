import pandas as pd;
import logging;
from here_api import geocode;

headers = pd.read_csv("escolas_ideb_v2.csv", nrows=0).columns;

data = pd.read_csv("escolas_ideb_v2.csv", skiprows=866, names=headers, nrows=1000);

data = data.assign(latitude=None);
data = data.assign(longitude=None);

for i, linha in data.iterrows():
    endereco = {
        "cidade": linha["NO_MUNICIPIO"], 
        "bairro": linha["NO_BAIRRO"],
        "rua": linha["DS_ENDERECO"],
        "cep": linha["CO_CEP"],
        "numero": linha["NU_ENDERECO"]
    };
    
    resultado = geocode(endereco);
    
    if resultado.status_code == 200:
        resultado = resultado.json();
        
        try:    
            latitude = resultado["items"][0]["position"]["lat"];
            longitude = resultado["items"][0]["position"]["lng"];
            
            data.at[i, "latitude"] = latitude;
            data.at[i, "longitude"] = longitude;
        except Exception as e:
            logging.error(e);
    

data.to_csv("escolas_ideb_coordenadas2.csv");

