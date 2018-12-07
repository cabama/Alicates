docker-compose build --no-cache nginx
docker service rm alicates_nginx
docker stack deploy -c docker-compose.yml alicates 
