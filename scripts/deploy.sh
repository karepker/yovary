#! /bin/bash

HOST=yovary

# change directory to the top of the git repo
cd "$(git rev-parse --show-toplevel)"

rsync -vruz --exclude=.git/ --exclude-from=.gitignore . "${HOST}:src/yovary"
echo "Successfully deployed!"
