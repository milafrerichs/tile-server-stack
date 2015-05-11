FROM ubuntu:14.04
MAINTAINER James Gregory <james@jagregory.com>

# install Python and all the mapnik dependencies
RUN apt-get update -y && apt-get install -y libjpeg-dev zlib1g-dev python python-setuptools python-dev python-pip python-gdal libboost-python-dev software-properties-common libmapnik2.2 libmapnik-dev mapnik-utils python-mapnik

# symlink the native extensions so Python can pick them up
RUN ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
RUN ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib
RUN ln -s /usr/lib/x86_64-linux-gnu/libboost_python.so /usr/lib
RUN ln -s /usr/lib/x86_64-linux-gnu/libboost_thread.so /usr/lib

# install tilestache, mapnik, and dependencies
RUN pip install --allow-external PIL --allow-unverified PIL PIL tilestache simplejson werkzeug sympy Blit mapnik2 jinja2 uwsgi

RUN mkdir /nepal-tiles
WORKDIR /nepal-tiles

RUN pip install gunicorn
ADD tilestache.cfg /nepal-tiles/tilestache.cfg
ADD wsgi.py /nepal-tiles/wsgi.py
ADD app.ini /nepal-tiles/app.ini
ADD gunicorn.py /nepal-tiles/gunicorn.py
ADD data /nepal-tiles/data

EXPOSE 8080
CMD ["gunicorn", "app.py", '--config=gunicorn.pry']
