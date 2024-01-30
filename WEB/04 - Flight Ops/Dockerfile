FROM tiangolo/uwsgi-nginx-flask:python3.11
COPY ./app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
# copy all the files to the container
COPY ./app /app
