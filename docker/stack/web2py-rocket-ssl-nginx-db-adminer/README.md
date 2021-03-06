# Start Service
	systemctl start docker

# Docker
	cd /Docker/App/web2py-rocket-ssl-nginx-db-adminer
	chmod 775 run.sh
	./run.sh

# Docker Compose
	pip install docker-compose
	cd /Docker/App/web2py-rocket-ssl-nginx-db-adminer
	docker-compose up -d
	docker-compose ps
	docker network ls
	docker network inspect root_default
	docker volume ls
	docker volume inspect root_applications

# Docker Stack
	docker swarm init --advertise-addr $(hostname -i)
	docker stack deploy -c docker-compose.yml web2py-rocket-ssl-nginx-db-adminer
	docker stack ls
	docker stack ps web2py-rocket-ssl-nginx-db-adminer
	docker stack services web2py-rocket-ssl-nginx-db-adminer

# Shell (Copy the content of the file into this scaffolding shell and replace the variable text $ with \$ )
cat << EOF > docker-compose.yml

EOF
cat docker-compose.yml

cat << EOF > run.sh

EOF
cat run.sh

cat << EOF > w2p.conf

EOF
cat w2p.conf

cat << EOF > web2py-adminer

EOF
cat web2py-adminer

cat << EOF > web2py-db

EOF
cat web2py-db

cat << EOF > web2py-nginx

EOF
cat web2py-nginx

cat << EOF > web2py-rocket-ssl

EOF
cat web2py-rocket-ssl

chmod 755 run.sh
./run.sh

docker-compose up -d
docker-compose ps
