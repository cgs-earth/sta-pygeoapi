FROM geopython/pygeoapi:latest

RUN pip3 install https://github.com/cgs-earth/pygeoapi-plugins/archive/refs/heads/master.zip

COPY sta.config.yml /pygeoapi/local.config.yml

COPY templates/* /pygeoapi/pygeoapi/templates/
