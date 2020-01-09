FROM python:3.8-alpine

WORKDIR /app

RUN apk add npm
RUN npm install -g localtunnel

RUN pip install pipenv

ADD Pipfile /app/
ADD Pipfile.lock /app/

RUN pipenv install

ADD localtunnel.py /app/
ADD pytunnel.py /app/

CMD pipenv run pytunnel
