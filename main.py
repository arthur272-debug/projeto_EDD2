from app import App;

uri = "neo4j+s://022d3bae.databases.neo4j.io";
user = "neo4j";
password = "Rf_gN6gzpHdxIyY2igyj53n-W6SYo9YjlIucAOc8RMI"

app = App(
    uri=uri, 
    user=user, 
    password=password
);

app.deleteAll();

app.close();