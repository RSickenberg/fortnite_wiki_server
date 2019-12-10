FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN mkdir requirements
COPY . /code/
RUN pip install -r requirements/base.txt
