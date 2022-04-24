# Final Project

For my final project I chose to dockerize a simple Python script that pulls from a public weather API.
To run this Docker image you will need to have Docker installed on your machine. Having the Docker GUI application is also recommended.
https://docs.docker.com/get-docker/

The link to my DockerHub that contains the Docker image is: https://hub.docker.com/repository/docker/cweedster1/python-img

From here you can pull the image down to your machine.
Run the image with the command.
~~~
docker run -ti python-img
~~~
You will have to make sure and use '-ti' tag to make sure that the application runs in interactive mode or else it will not work.

From here you can enter the name of a city and the program will return the forecast for that city.
Make sure and spell the city name correctly or you will have to deal with my creative error handling.
