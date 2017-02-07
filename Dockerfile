FROM python:2.7-alpine

WORKDIR /code

COPY requirements.txt /code
COPY reply_bot.py /code
COPY tweet_bot.py /code
COPY follow_bot.py /code

RUN pip install -r requirements.txt
CMD python tweet_bot.py && python follow_bot.py
