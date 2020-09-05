FROM python


RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
COPY requirements.txt /
RUN pip install -r requirements.txt
WORKDIR /app
COPY app /app
COPY start.sh /

EXPOSE 9090 9191 5000
USER uwsgi

CMD ["/start.sh"]
