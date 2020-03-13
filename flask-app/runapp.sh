#!/bin/bash
if [ ! -x "$(command -v docker)" ]; then
curl https://get.docker.com | sudo bash
fi
if [[ "$(docker images -q flaskapp 2> /dev/null)" == "" ]]; then
docker build -t flaskapp .
fi
docker run -d -p 5000:5000 --network flaskapp -e DATABASE_URI=mysql+pymysql://root:${rootpass}@mysql:3306/${dbname} -e SECRET_KEY =${SECRET_KEY} --name flaskapp flaskapp
