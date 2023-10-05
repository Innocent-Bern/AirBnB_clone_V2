#!/usr/bin/env bash
# sets up web servers for deployment of web_static

if ! which nginx > /dev/null 2>&1; then
	sudo apt-get -y update
	sudo apt-get -y install nginx
	service nginx start
fi

if [ ! -d "/data" ]; then
	sudo mkdir /data
fi
if [ ! -d "/data/web_static" ]; then
	sudo mkdir /data/web_static
fi
if [ ! -d "/data/web_static/shared" ]; then
	sudo mkdir /data/web_static/shared
fi
if [ ! -d "/data/web_static/releases" ]; then
	sudo mkdir /data/web_static/releases
fi
if [ ! -d "/data/web_static/releases/test" ]; then
	sudo mkdir /data/web_static/releases/test
fi
echo "Test file" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

echo "
server {
        listen 80 default_server;
        listen [::]:80 default_server;
	root /data/web_static/current;
	index index.html;

	location /hbnb_static {
        	alias /data/web_static/current;
	        index index.html;
	}
        location /redirect_me {
                return 301  https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
	add_header X-Served-By 223183-web-01;
}
" > /etc/nginx/sites-available/default
service nginx restart
