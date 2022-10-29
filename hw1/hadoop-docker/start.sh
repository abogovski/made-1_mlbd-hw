cd $(dirname $0)
docker-compose down -v
docker-compose build
docker-compose up --force-recreate --always-recreate-deps
