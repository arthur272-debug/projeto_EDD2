import requests;
from dotenv import load_dotenv;
import os;

load_dotenv();

api_key = os.getenv("HERE_API_KEY");

base_url = f"https://geocode.search.hereapi.com/v1/geocode?apiKey={api_key}&qq=";

def geocode(endereco: dict):
    
    cidade = endereco["cidade"];
    bairro = endereco["bairro"];
    rua = endereco["rua"];
    numero = endereco["numero"];
    cep = endereco["cep"];
    
    response = requests.get(f"{base_url}city={cidade};country=Brasil;street={rua};destrict={bairro};postalCode={cep};houseNumber={numero}");
    
    return response.json();