FROM python:3.11

RUN useradd --create-home userapi
WORKDIR /flaskapi

RUN pip install -u pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --system
COPY ./ .
RUN chown -R userapi:userapi ./
USER userapi

EXPOSE 5000
CMD ["gunicorn", "-b0.0.0.0:8000", "wsgi:app"]