FROM internetofwater/pygeoapi-plugins:edr

COPY sta.config.yml /pygeoapi/local.config.yml

COPY templates/* /pygeoapi/pygeoapi/templates/
