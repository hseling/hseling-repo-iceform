FROM hseling/hseling-api-base:python3.6-alpine3.7 as hseling_api_build

LABEL maintainer="Evgenii Glazunov <e.glznv@yandex.ru>"

RUN mkdir /dependencies
COPY ./hseling-api-iceform/requirements.txt /dependencies/requirements.txt
COPY ./hseling-api-iceform/setup.py /dependencies/setup.py

RUN pip install -r /dependencies/requirements.txt

FROM hseling/hseling-api-base:python3.6-alpine3.7 as production

COPY --from=hseling_api_build /usr/local/lib/python3.6/site-packages /usr/local/lib/python3.6/site-packages
COPY --from=hseling_api_build /usr/lib/python3.6/site-packages /usr/lib/python3.6/site-packages

COPY --from=hseling_api_build /dependencies /dependencies

COPY ./hseling-lib-iceform /dependencies/hseling-lib-iceform
RUN pip install /dependencies/hseling-lib-iceform

COPY ./hseling-api-iceform/hseling_api_iceform /app/hseling_api_iceform
COPY ./hseling-api-iceform/main.py /app/main.py

RUN mkdir -p /data

ENV HSELING_API_ICEFORM_SETTINGS="/app/hseling_api_iceform/default_settings.py"

HEALTHCHECK CMD curl --fail http://localhost:5000/api/healthz || exit 1

