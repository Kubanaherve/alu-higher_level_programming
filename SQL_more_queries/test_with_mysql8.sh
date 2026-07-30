#!/bin/bash
# Run a SQL file against MySQL via Docker (defaults to 5.7)
# Usage: ./test_with_mysql.sh <sql_file> [database] [mysql_version]
#   mysql_version defaults to 5.7 (use 8.0.25 to test MySQL 8)

SQL_FILE="${1:?Usage: $0 <sql_file> [database] [mysql_version]}"
DB="${2}"
MYSQL_VERSION="${3:-5.7}"

CONTAINER="mysql_test_$$_${MYSQL_VERSION//./_}"

docker run --platform linux/amd64 -d \
  --name "$CONTAINER" \
  -e MYSQL_ALLOW_EMPTY_PASSWORD=yes \
  "mysql:${MYSQL_VERSION}" > /dev/null 2>&1

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
