#!/bin/bash
cd /home/denis/adboard || exit 1
git pull --ff-only origin dev  || exit 2
#git pull origin tests  || exit 1
#git fetch origin tests
# git reset --hard origin/test
#git checkout remotes/origin/tests
#git add *
#git checkout tests
#git merge --no-ff --no-edit remotes/origin/tests
git add * || exit 3
# git commit -m "Update" || exit 1
sudo systemctl restart gunicorn  || exit 5
sudo systemctl restart nginx  || exit 6
echo "Deployment completed successfully"

