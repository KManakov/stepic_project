sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
# source web/myvenv/bin/activate
gunicorn -b 0.0.0.0:8080 --pythonpath /home/box/web/etc/gunicorn-wsgi.conf hello:app
gunicorn -b 0.0.0.0:8000 --pythonpath /home/box/web/etc/gunicorn-django.conf ask.wsgi:application
