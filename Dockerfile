#Установка зависимостей uv
FROM python:3.9-slim

RUN pip install uv

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

ENV PATH="/.venv/bin:$PATH"

COPY . .

CMD ["python", "main.py"]
