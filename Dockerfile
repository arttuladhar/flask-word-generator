# Base Image
FROM alpine:3.1

# Update
RUN apk add --update python py-pip

ADD . /flask-word-generator

WORKDIR /flask-word-generator

EXPOSE 5000

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]