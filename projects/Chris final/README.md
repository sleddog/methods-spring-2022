# Final Project

For my final project I chose to dockerize a simple Python script that pulls from a public weather API.
To run this Docker image you will need to have Docker installed on your machine.

The link to my DockerHub that contains the Docker image is: https://hub.docker.com/repository/docker/alligatordundee/chris-fizz


From here you can pull the image down to your machine.
Run the image with the command.
~~~
docker run -ti python-img
~~~
You will have to make sure and use '-ti' tag to make sure that the application runs in interactive mode or else it will not work.

from here you can enter a number and the program will output the fizz buzz