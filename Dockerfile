FROM python:3.10.7
LABEL author="yechan24680@gmail.com"

RUN pip3 install django==4.1

COPY ./mysite /app
WORKDIR /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
