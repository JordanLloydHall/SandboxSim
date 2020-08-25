@echo off

git add *

SET /P commit_des=Commit Description:

git commit -m %commit_des%

SET /P bool_commit="R u sure u wanna commit? y/n"

if "%bool_commit%"=="y" goto end
echo "hello"

:end