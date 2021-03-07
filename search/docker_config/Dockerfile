FROM etiennenapoleone/docker-python-poetry:3.7-rc


WORKDIR /tmp/working

COPY poetry.lock .
COPY pyproject.toml .
RUN poetry install --no-virtualenv --no-dev

COPY main.py .
COPY spec.py .
ENV DEST_FOLDER /aci/output
CMD [ "python", "./main.py" ]

