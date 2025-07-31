FROM internetofwater/pygeoapi:latest

COPY sta.config.yml /pygeoapi/local.config.yml

COPY templates/jsonld /pygeoapi/pygeoapi/templates/jsonld
