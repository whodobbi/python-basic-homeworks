FROM python:3.10.12-bookworm

WORKDIR /app

RUN pip install "poetry==1.7.1"
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root

COPY app.py ./

CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]

EXPOSE 8000