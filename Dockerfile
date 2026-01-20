#Установка зависимостей uv
FROM python:3.9

RUN pip install uv

COPY pyproject.toml .
COPY uv.lock .
RUN uv sync --frozen

ENV PATH = "/.venv/bin:$PATH"

COPY . .

CMD ["uv", "run", "python", "main.py"]