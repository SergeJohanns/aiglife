FROM python:3
RUN pip install flask flask-sqlalchemy flask-restful
COPY flaskr flaskr
ENV FLASK_APP=flaskr
ENV FLASK_ENV=dev
EXPOSE 5000
RUN flask run --host=0.0.0.0