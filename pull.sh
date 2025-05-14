#!/bin/bash
cd /home/denis/adboard || exit 1
git pull --ff-only origin dev  || exit 2
# git commit -m "Update" || exit 1
sudo systemctl restart gunicorn  || exit 5
sudo systemctl restart nginx  || exit 4
echo "Deployment completed successfully"
#git fetch origin tests
# git reset --hard origin/test

