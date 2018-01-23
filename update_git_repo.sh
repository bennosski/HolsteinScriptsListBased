#!/bin/bash


echo "updating the repo"

git add -u
git status
git commit -m "update"
#git push -u origin master
git push -u origin master:auto
