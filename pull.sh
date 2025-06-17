#!/bin/bash
cd /home/denis/adboard || exit 1
git pull --ff-only origin cicd  || exit 1
# sudo docker compose down || exit 1
if [ "$(sudo docker ps -aq)" ]; then
    echo "Found running containers, stopping them..."
    sudo docker compose down || exit 1
    sudo docker builder prune -af  || exit 1
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


#sudo docker compose -f ./docker-compose.yml build --no-cache  # Пересборка всех сервисов
sudo docker compose -f ./docker-compose.yml up -d

echo "Deployment completed successfully"
