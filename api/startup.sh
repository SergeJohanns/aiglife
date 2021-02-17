#!/bin/sh
uwsgi -d --ini api.ini
nginx -g 'daemon off;'