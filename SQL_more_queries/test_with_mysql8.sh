#!/bin/bash
# Run a SQL file against MySQL 8.0.25 via Docker
# Usage: ./test_with_mysql8.sh <sql_file> [database]

SQL_FILE="${1:?Usage: $0 <sql_file> [database]}"
DB="${2}"

CONTAINER="mysql8_test_$$"

docker run --platform linux/amd64 -d \
  --name "$CONTAINER" \
  -e MYSQL_ALLOW_EMPTY_PASSWORD=yes \
  mysql:8.0.25 > /dev/null 2>&1

# Wait for MySQL to be ready
for i in $(seq 1 20); do
  docker exec "$CONTAINER" mysql -uroot -e "SELECT 1" > /dev/null 2>&1 && break
  sleep 2
done

if [ -n "$DB" ]; then
  docker exec -i "$CONTAINER" mysql -uroot "$DB" < "$SQL_FILE"
else
  docker exec -i "$CONTAINER" mysql -uroot < "$SQL_FILE"
fi

docker stop "$CONTAINER" > /dev/null 2>&1
docker rm "$CONTAINER" > /dev/null 2>&1
