From python:3.7
WORKDIR /app/
COPY . /app/
EXPOSE 8000
run pip install -r requirements.txt

ENTRYPOINT ["uwsgi", "--ini", "hellodocker.ini"]
#ENTRYPOINT ["sh","-c", "cd helloworld && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
