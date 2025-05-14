#!/bin/bash
cd /home/denis/adboard || exit 1
git pull --ff-only origen dev  || exit 1
#git pull origin tests  || exit 1
#git fetch origin tests
# git reset --hard origin/test
#git checkout remotes/origin/tests
#git add *
#git checkout tests
#git merge --no-ff --no-edit remotes/origin/tests
git add * || exit 1
git commit -m "Update" || exit 1
sudo systemctl restart gunicorn  || exit 1
echo "Deployment completed successfully"

