FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN mkdir requirements
COPY requirements/ /code/requirements
RUN pip install -r requirements/base.txt
COPY . /code/
