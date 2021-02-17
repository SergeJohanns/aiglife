FROM nginx

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip uwsgi
RUN pip3 install flask flask-sqlalchemy flask-restful uwsgi

COPY flaskr flaskr
COPY wsgi.py wsgi.py
COPY api.ini api.ini
COPY default.conf /etc/nginx/conf.d/default.conf

ENV FLASK_APP=flaskr
EXPOSE 5000

COPY startup.sh startup.sh
RUN chmod +x startup.sh
ENTRYPOINT /startup.sh