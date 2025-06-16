#!/bin/bash
cd /home/denis/adboard || exit 1
git pull --ff-only origin dev  || exit 1
sudo systemctl restart gunicorn  || exit 1
echo "Deployment completed successfully"


