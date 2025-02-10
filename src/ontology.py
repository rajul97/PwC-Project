from neo4j import GraphDatabase

URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "password")

def create_data(tx):
    tx.run("CREATE (u:User {name: 'Alice', age: 30})")

driver = GraphDatabase.driver(URI, auth=AUTH)
with driver.session() as session:
    session.write_transaction(create_data)

print("✅ Data inserted into Neo4j")
