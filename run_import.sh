
SQL_FILE="./init/import_data.sql"
CONTAINER_NAME="postgres"
DB_USER="superset"
DB_NAME="superset"

if [ ! -f "$SQL_FILE" ]; then
  echo "Error: SQL file '$SQL_FILE' not found."
  exit 1
fi

echo "Copying SQL file to Docker container..."
docker cp "$SQL_FILE" "$CONTAINER_NAME:/import_data.sql"


if [ $? -ne 0 ]; then
  echo "Error: Failed to copy SQL file to container."
  exit 1
fi


echo "Executing SQL script inside Docker container..."
docker exec -it "$CONTAINER_NAME" psql -U "$DB_USER" -d "$DB_NAME" -f /import_data.sql

if [ $? -ne 0 ]; then
  echo "Error: Failed to execute SQL script."
  exit 1
fi

echo "SQL script executed successfully."