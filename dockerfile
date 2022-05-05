FROM python:3.9.1-alpine

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip 
COPY  . . 
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app

ENV FLASK_APP=model.py FLASK_ENV=development

#CMD ["flask", "run"]