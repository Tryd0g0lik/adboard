#!/bin/bash
cd /home/denis/adboard || exit 1
git pull --ff-only origin dev  || exit 1
sudo docker compose down || exit 1
sudo docker rmi $(sudo docker images -q) || exit 1
sudo docker compose -f ./docker-compos* up -d || exit 1
echo "Deployment completed successfully"


