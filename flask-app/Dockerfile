FROM python:3.7
RUN apt-get update && apt-get install -y python3-pip
COPY . .
RUN pip3 install flask
EXPOSE 5000
ENTRYPOINT ["usr/local/bin/python3","app.py"]
