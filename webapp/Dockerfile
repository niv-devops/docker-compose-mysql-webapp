# Stage 1: Build
FROM python:3.13-slim AS build
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final image
FROM python:3.13-slim
WORKDIR /app
COPY --from=build /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY app.py /app/
COPY templates/index.html /app/templates/
RUN useradd -m flaskuser
RUN chown -R flaskuser:flaskuser /app
USER flaskuser
EXPOSE 5000
CMD ["python", "app.py"]
