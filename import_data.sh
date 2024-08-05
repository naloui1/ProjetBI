docker cp ./init/import_data.sql postgres:/import_data.sql

sleep 20

docker exec -it postgres psql -U superset -d superset -f /import_data.sql