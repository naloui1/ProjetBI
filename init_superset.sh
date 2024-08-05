#!/bin/bash

echo "Waiting for 20 seconds before checking database readiness..."
sleep 20

superset db upgrade

# Create an admin user
superset fab create-admin --username admin --firstname Admin --lastname User --email admin@admin.com --password admin

superset init

superset run -p 8088 -h 0.0.0.0 --with-threads --reload --debugger
