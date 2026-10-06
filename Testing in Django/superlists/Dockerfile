FROM python:3.13-slim
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY packages /packages
RUN pip install --no-index --find-links=/packages "django>=4.2,<6"
COPY src /src
WORKDIR /src
CMD ["python", "manage.py", "runserver", "8888"]


