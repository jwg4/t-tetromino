FROM gcc:latest

COPY main.py /
COPY exact_cover_np /

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install -r dev_requirements.txt
RUN make install_exact_cover

CMD [ "python", "./main.py" ]

