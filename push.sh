#!/bin/bash
#git remote add upstream git@github.com:tttor/math-foundation.git

echo '=== comitting ==='
git pull origin master
bash list.sh

git add --all
git commit -a -m fix

echo '=== github.com ==='
git push upstream master
