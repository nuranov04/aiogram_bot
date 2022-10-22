FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
USER root
WORKDIR /telegram_bot
ADD ./requirements.txt /telegram_bot/
RUN pip install --upgrade pip
RUN pip install -r /telegram_bot/requirements.txt
ADD . /telegram_bot/
CMD ["chmod", "+x", "/telegram_bot/docker/bot-entrypoint.sh"]
EXPOSE 8080