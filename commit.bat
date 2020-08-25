@echo off

git add *

SET /P commit_des = Commit Description:

git commit -m " 'commit_des' "

git push -u origin master