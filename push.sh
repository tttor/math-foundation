#!/bin/bash
#git remote add upstream git@github.com:tttor/math-foundation.git

echo '=== comitting ==='
git pull upstream master
bash list.sh

git add --all
git commit -a -m fix

echo '=== github.com ==='
git push upstream master
