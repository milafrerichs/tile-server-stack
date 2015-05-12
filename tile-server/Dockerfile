FROM milafrerichs/docker-tilestache

RUN pip install gunicorn jinja2 redis

RUN mkdir /nepal-tiles
WORKDIR /nepal-tiles

ADD tilestache.cfg /nepal-tiles/tilestache.cfg
ADD wsgi.py /nepal-tiles/wsgi.py
ADD app.ini /nepal-tiles/app.ini
ADD gunicorn.py /nepal-tiles/gunicorn.py
ADD data /nepal-tiles/data

EXPOSE 8080
CMD gunicorn wsgi.py --bind 0.0.0.0:8080
