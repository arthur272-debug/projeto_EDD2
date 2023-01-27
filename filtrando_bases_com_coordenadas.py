import pandas as pd;

base1 = pd.read_csv("escolas_ideb_coordenadas.csv", nrows=865, index_col=0);
base2 = pd.read_csv("escolas_ideb_coordenadas2.csv", index_col=0);
base3 = pd.read_csv("escolas_ideb_coordenadas3.csv", index_col=0);

base1 = base1.drop(columns=["Unnamed: 0"]);
base2 = base2.drop(columns=["Unnamed: 0"]);
base3 = base3.drop(columns=["Unnamed: 0"]);

tabela = pd.concat([base1, base2, base3], ignore_index=True);

print(tabela);
tabela.to_csv("base.csv");
