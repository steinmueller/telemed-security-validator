su - tna
createdb -O tna tnadb
dropdb -U tna -i tnadb
psql tnadb
\dt


dbname=telemed-validation-database host=telemed-validation-server.postgres.database.azure.com 
port=5432 sslmode=require user=pkszjgkyih password=TC8TM8RIN1LEM473$
# in ssh web console
psql -h telemed-validation-server.postgres.database.azure.com -U pkszjgkyih telemed-validation-database
psql -h telemed-validation-server.postgres.database.azure.com -U pkszjgkyih postgres
# restart web app
drop database "telemed-validation-database";
create database "telemed-validation-database" with owner pkszjgkyih;