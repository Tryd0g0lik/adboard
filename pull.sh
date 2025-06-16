#!/bin/bash
cd /home/denis/adboard || exit 1
git pull --ff-only origin dev  || exit 1
# sudo docker compose down || exit 1
if [ "$(sudo docker ps -aq)" ]; then
    echo "Found running containers, stopping them..."
    sudo docker compose down || exit 1
else
    echo "No running containers found"
fi

# sudo docker rmi $(sudo docker images -q) || exit 1
if [ "$(sudo docker images -q)" ]; then
    echo "Found docker images, removing them..."
    sudo docker rmi $(sudo docker images -q) || exit 1
else
    echo "No docker images found"
fi

sudo docker compose -f ./docker-compose.yml up -d --build --force-recreate
echo "Deployment completed successfully"


