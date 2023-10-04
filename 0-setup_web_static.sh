#!/usr/bin/env bash
# A Bash script that sets up  web servers for the deployment of a static web.

apt -y update
apt -y install nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "hello world!" | sudo tee /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

printf %s "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By $HOSTNAME;
	root /var/www/html;
	index index.html index.htm;

	location /hbnb_static {
		alias /data/web_static/current;
		index index.html index.htm;
	}
	rewrite ^/redirect_me https://google.com;
	error_page 404 /404.html;
	location /404 {
		root /var/www/html;
		internal;
	}
}" > /etc/nginx/sites-available/default
service nginx restart
