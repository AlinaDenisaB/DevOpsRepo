FROM python:3.7
WORKDIR /flask-app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]
