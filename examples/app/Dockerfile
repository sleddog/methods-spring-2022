FROM ubuntu:latest
RUN echo Updating existing packages, installing and upgrading python and pip.
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev
RUN pip install --upgrade pip
RUN echo Copying the Hello World Flask service into a service directory.
COPY ./service /HelloWorldService
WORKDIR /HelloWorldService
RUN echo Installing Python packages listed in requirements.txt
RUN pip install -r ./requirements.txt
RUN echo Starting python and starting the Flask service...
EXPOSE 8080/tcp
ENTRYPOINT ["python3"]
CMD ["hello_world_service.py"]
