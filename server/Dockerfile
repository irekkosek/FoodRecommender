FROM python:3.10
WORKDIR /server
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir docker-entrypoint==0.1.6 && \
    pip install --no-cache-dir -r requirements.txt 
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN  chmod +x /docker-entrypoint.sh
COPY . .
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["uvicorn", "main:app", "--host","0.0.0.0", "--port","8000"]
