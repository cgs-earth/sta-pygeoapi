FROM internetofwater/pygeoapi:sta

COPY sta.config.yml /pygeoapi/local.config.yml

COPY templates/* /pygeoapi/pygeoapi/templates/
