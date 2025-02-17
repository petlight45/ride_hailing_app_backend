FROM ubuntu:latest
FROM python:3.11

WORKDIR /django
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Installing Project Requirements
ADD requirements requirements
RUN pip install -r requirements/test.txt

RUN addgroup --system django \
    && adduser --system --ingroup django django

COPY --chown=django:django ./devops/docker/django/start.sh /django/start.sh
RUN sed -i 's/\r$//g' /django/start.sh
RUN chmod +x /django/start.sh

COPY --chown=django:django ./devops/docker/django/test/start_test.sh /django/start_test.sh
RUN sed -i 's/\r$//g' /django/start_test.sh
RUN chmod +x /django/start_test.sh


# Copying other files
ADD . .

RUN python manage.py check
EXPOSE 8000
CMD ["/django/start.sh"]
