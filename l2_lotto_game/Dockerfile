FROM python:3

WORKDIR /otus_web/

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY src ./l2_lotto_game/src
COPY test ./l2_lotto_game/test
COPY main.py main.py

CMD [ "python", "./main.py" ]