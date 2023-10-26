FROM python:3.8

COPY requirements.txt ./requirements.txt

RUN python -m pip install -U pip && \
    python -m pip install -r requirements.txt && \
    python -m pip cache purge

COPY ./ /app/

WORKDIR /app/

CMD uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5011}