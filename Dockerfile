FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt update
RUN apt install -y python3-venv && \
    pip
RUN mkdir /www && \
    mkdir /www/src && \
    mkdir /www/src/weather && \
    mkdir /www/src/weather/static
WORKDIR /www/src
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn
COPY . .
#RUN python manage.py collectstatic --noinput
#CMD ["gunicorn", "-w", "4", "--bind", ":8000", "weather.wsgi:application"]

