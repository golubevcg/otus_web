FROM ubuntu:20.04

WORKDIR /otus_web/

RUN apt-get update && apt-get install -y python3-pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY src l2_lotto_game/src
COPY test l2_lotto_game/test
COPY main.py main.py
COPY start.sh start.sh

RUN chmod a+x start.sh

CMD ["sh", "./start.sh"]