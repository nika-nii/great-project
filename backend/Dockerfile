FROM python:3.10-slim
WORKDIR /code/app
COPY ./requirements.txt /code/requirements.txt
RUN pip install --disable-pip-version-check --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
