# using alpine since its small
FROM python:3.9.2

# declare envs
ARG MYSQL_DB_HOST
ARG MYSQL_DATABASE
ARG MYSQL_USER
ARG MYSQL_PASSWORD


# load envs
ENV  MYSQL_DB_HOST=${MYSQL_DB_HOST} \
    MYSQL_DATABASE=${MYSQL_DATABASE} \
    MYSQL_USER=${MYSQL_USER} \ 
    MYSQL_PASSWORD=${MYSQL_PASSWORD}


RUN python3 -m pip install --upgrade pip setuptools wheel

RUN apt-get update &&  apt-get install -y git-all python3-dev python3-pip python3-setuptools cmake build-essential libssl-dev

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# exposing the port
EXPOSE 8000