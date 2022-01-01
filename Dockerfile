FROM python:3.8-slim-buster
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/
EXPOSE 80
CMD  python mysite/manage.py migrate ; python mysite/manage.py runserver  0.0.0.0:80




