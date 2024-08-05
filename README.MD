1. open application Docker ( as an administrator )
2. open console as an administrator ----> navigate to the folder PROJETBI
3. command: docker-compose up -d
4. we have now 3 containers ( for PostgreSQL, port=5432  and Superset, port=8088 and web app PGADMIN for operating with DBs, port=5050 )

links and logins:
    - Superset : 
        -   http://localhost:8088/
        -   login: admin
        -   pwd: admin

    - PGadmin: 
        -   http://localhost:5050/
        -   login: admin@admin.com
        -   pwd:   admin



CREATING CONNECTION WITH DB:

1. open PGadmin and login
2. select "Add New Server"
    General:
        name: superset
    Connection:
        host name: postgres
        port: 5432
        Maintenance db: superset
        username: superset
        pwd: superset

CONNECTION TO SUPERSET:
1. open Superset : http://localhost:8088/
2. login: admin, pwd: admin
3. press '+ ' button on the top right --> Data --> Connect Database
4. Select PosetgreSQL
5. on the bottom select 'Connect this db with a SQLAlchemy'
6. insert this link --> postgresql+psycopg2://superset:superset@postgres:5432/superset
6. press connect
7. then go to DATASETS
8. press '+DATASET'
9. Now u can select on the left: 
    db: PostgreSQL
    schema: public
    table: 

postgresql+psycopg2://superset:superset@postgres:5432/superset