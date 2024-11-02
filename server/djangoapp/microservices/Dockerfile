FROM python:3.9.18-slim-bookworm

ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

ENV APP=/app

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . $APP

EXPOSE 8000

ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]

RUN chmod +x /app/entrypoint.sh
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
