from neo4j import GraphDatabase;
from pandas import pd;

class App:
    
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password));
        self.session = self.driver.session();
                  
    def close(self):
        self.driver.close();
        
    def create(self, name):            
        
        query = "CREATE (n:Node { name: $name })"
        
        self.session.run(query, name=name);
        
    def delete(self, name):
        
        query = "MATCH (n:Node) WHERE n.name = $name DETACH DELETE n";
        
        self.session.run(query, name=name);
        
    def deleteAll(self):
        
        query = "MATCH (n) DETACH DELETE n";
        
        self.session.run(query);
        
