FROM python:3.7


WORKDIR /tmp/working

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
ENV DEST_FOLDER /aci/output
CMD [ "python", "./main.py" ]

