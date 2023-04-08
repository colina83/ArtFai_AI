#Pull base image
FROM python:3.8

# Set Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set Working Directory
WORKDIR /project

#Install Dependencies
COPY Pipfile Pipfile.lock /project/
RUN pip install pipenv && pipenv install --system

#Copy Project

COPY . /project/