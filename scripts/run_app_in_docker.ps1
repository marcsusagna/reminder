docker build -t reminder_image .
docker run -dit --name reminder_container -p 8502:8502 -d reminder_image 
docker exec -it reminder_container poetry run start_app