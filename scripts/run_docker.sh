docker build -t reminder_image .
docker run -dit --name reminder_container -p 8502:8502 -v /c:/mnt/c -d reminder_image 


docker exec -it reminder_container /bin/sh

docker stop reminder_container
docker rm reminder_container