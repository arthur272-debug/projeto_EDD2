import pandas as pd;

caminho_bases = "/content/drive/MyDrive/projeto_edd2/bases_de_dados/";

## pulando as primeiras linhas, porque elas sao apenas cabeçalhos com informaçoe irrelevantes
ideb = pd.read_excel(caminho_bases + "ideb.xlsx", skiprows=9);

id_escola = "ID_ESCOLA";
nota_ideb = "VL_OBSERVADO_2021";

## filtrando apenas as escolas que possuem um id.
ideb = ideb[ideb[id_escola].notna()];

## convertendo o tipo do id para int (é float por padrão)
ideb[id_escola] = ideb[id_escola].astype(int);

## filtrando apenas colunas relevantes.
ideb = ideb[[id_escola, nota_ideb]];

## filtrando apenas as escolas que possuem uma nota.
ideb = ideb[(ideb[nota_ideb] != "-") & (ideb[nota_ideb].notna())];

ideb = ideb.rename(columns={"VL_OBSERVADO_2021": "NOTA_IDEB"})
ideb = ideb.reset_index(drop=True);

print(ideb);

escolas = pd.read_csv(caminho_bases + "escolas.csv", sep=";", encoding="latin-1");

nome_uf = "NO_UF";
sigla_uf = "SG_UF";
regiao = "NO_REGIAO";
nome_municipio = "NO_MUNICIPIO";
nome_bairro = "NO_BAIRRO";
cep = "CO_CEP";
endereco = "DS_ENDERECO";
numero_endereco = "NU_ENDERECO"

nome_entidade = "NO_ENTIDADE";
id_entidade = "CO_ENTIDADE";

## filtrando apenas as colunas relevantes.
escolas = escolas[[id_entidade, nome_entidade, nome_uf, sigla_uf, regiao, nome_municipio, nome_bairro, cep, endereco, numero_endereco]];
print(escolas[escolas[id_entidade] == 31034533]);

## filtrando apenas as escolas da regiao Sudeste.
escolas = escolas[(escolas[regiao] == "Sudeste")];

## filtrando as escolas que possuem endereço completo.
escolas = escolas[(escolas[nome_bairro].notna()) & (escolas[endereco].notna()) & (escolas[numero_endereco] != "S/N") & (escolas[numero_endereco] != "SN") & (escolas[numero_endereco] != "S/Nº")];


escolas = escolas.rename(columns={"CO_ENTIDADE": "ID_ESCOLA"});
escolas = escolas.reset_index(drop=True);

print(escolas);

escolas_ideb = pd.merge(ideb, escolas, on="ID_ESCOLA", how="inner");

# escolas_ideb.to_csv(caminho_bases + "escolas_ideb_v2.csv");

print(escolas_ideb);