FROM python:3.10
WORKDIR /server
COPY requirements.txt requirements.txt
# ENV PRISMA_SKIP_POSTINSTALL_GENERATE=true
RUN pip install --no-cache-dir -r requirements.txt 
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN  chmod +x /docker-entrypoint.sh
COPY . .
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["uvicorn", "main:app", "--host","0.0.0.0", "--port","8000"]
