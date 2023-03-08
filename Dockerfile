FROM python:3.11.2-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install --no-install-recommends -y curl build-essential
RUN set -xe
ENV PATH="/root/.local/bin:$PATH"
WORKDIR app
COPY . .
RUN apt-get -y install binutils libproj-dev gdal-bin libsqlite3-mod-spatialite gdal-bin sqlite3
RUN pip install -r requirements.txt
EXPOSE 8000
RUN chmod 755 ./run.sh
RUN chmod +x ./run.sh
ENTRYPOINT ["./run.sh"]
CMD [""]
