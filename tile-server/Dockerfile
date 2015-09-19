FROM milafrerichs/docker-tilestache

RUN pip install gunicorn jinja2 redis newrelic
RUN pip install python-memcached
RUN mkdir /tile-server
WORKDIR /tile-server

ADD tilestache.cfg /tile-server/tilestache.cfg
ADD wsgi.py /tile-server/wsgi.py

EXPOSE 8080
CMD gunicorn wsgi:application --bind 0.0.0.0:8080
