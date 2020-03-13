#! /usr/bin/env bash
# setup a mysql db in a docker container

# install docker if it isn't already
if ! sudo docker --version > /dev/null; then
    curl https://get.docker.com | sudo bash
fi

MYSQL_DATABASE="bookshelve"

create_container() {
    sudo docker run -d \
        --name mysql \
        -p 3306:3306 \
        --health-cmd='mysqladmin ping --silent' \
        -e MYSQL_DATABASE="${MYSQL_DATABASE}" \
        -e MYSQL_ROOT_PASSWORD="${MYSQL_ROOT_PASSWORD}" \
        -e MYSQL_USER="${MSQL_USER}" \
        -e MYSQL_PASSWORD="${MYSQL_PASSWORD}" \
        mysql:5.7
        #While [[ "$(sudo docker inspect --format "{{ .State.Health.Status }}" mysql)" != "healthy" ]]; do 
           # sleep 1;
           # echo "waiting for mysql db to start..."
        #done 
        echo "db started"
}

grant_user_read_access() {
    command="grant select on ${MYSQL_DATABASE}.* to '${MYSQL_USER}'@'%' identified by '${MYSQL_PASSWORD}'";
    sudo docker exec -i mysql mysql --connect-timeout=90 -uroot -p${MYSQL_ROOT_PASSWORD} -e  "${command}"
}

run_sql_scripts() {
    sudo docker exec -i mysql mysql bookshelve \
        -uroot -p${MYSQL_ROOT_PASSWORD} < setup.sql 
}

# if the container doesn't exist
if [ -z "$(sudo docker ps -qa -f name=mysql)" ]; then
    create_container
    grant_user_read_access
# if the container is stopped
elif [ -n "$(sudo docker ps -q -f status=exited -f name=mysql)" ]; then
    sudo docker start mysql
fi
run_sql_scripts

