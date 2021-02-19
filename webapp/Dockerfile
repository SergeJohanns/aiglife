FROM nginx

COPY data data
RUN chmod -R +r /data
COPY default.conf /etc/nginx/conf.d/default.conf

EXPOSE 5000

COPY startup.sh startup.sh
RUN chmod +x startup.sh
ENTRYPOINT /startup.sh