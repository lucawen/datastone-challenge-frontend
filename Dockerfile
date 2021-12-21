FROM python:3.9

RUN mkdir /app
COPY requirements.txt /app/.
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt
VOLUME /app
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
