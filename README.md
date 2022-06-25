# Machine-Learning-Project
this is 1st machine learning project







Creating conda enviroment

conda create -p venv python==3.7 -y
...
to add file to git
...
git add <filename>
...
to ignore file or folder grom git we can writename of file/folder in .gitignore file

to check git status
...
git status

....
to check all version maintained by git 
...

git log

....

To create git version/ commit all changes dn by git
..
git commit -m 'message'
...
to send version/changes to github
...
git push origin main
....
to check remote url 
....
git remote -v

...

to setup CI/CO pipeline in heroku we need 3 thing

1. HEROKU_EMAIL -vijitkumar699@gmail.com
2. HEROKU_APIKEY -1789d192-84d3-44a0-8534-081197e5bf12
3. HEROKU_APP_NAME -hello-ml

BUILD DOCKER IMAGE
.....

docker build -t <image_name>:<tagname> .
....
~note = name of image always be in small letter for docker

to list docker image
...

docker images
...

Run docker images
....

docker run -p 5000:5000 -e PORT=5000 <imageid>
....

to check running container 
...
docker ps

..
to stop container 
...

docker stop container_id


....

pip install ipykernel
...
