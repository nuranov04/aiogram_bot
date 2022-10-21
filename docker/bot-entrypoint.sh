#!/bin/sh

until cd /telegram_bot/

do
    echo "Waiting for db to be ready..."
    sleep 2
done

#python3 telegram_bot/app.py
