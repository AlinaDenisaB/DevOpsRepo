#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3 && python3-venv 

if [ ! -x "$(command -v docker)" ]; then
curl https://get.docker.com | sudo bash
sudo usermod -aG docker $(whoami)
fi

if [ ! -x "$(command -v docker-compose)" ]; then
sudo apt install -y curl jq
# set which version to download (latest)
version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
# download to /usr/local/bin/docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
# make the file executable
sudo chmod +x /usr/local/bin/docker-compose
fi
