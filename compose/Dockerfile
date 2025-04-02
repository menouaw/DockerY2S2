# spécifie la version de langage
FROM python:3.10

# définit le répertoire de travail
WORKDIR /app

# copie les fichiers nécessaires dans le répertoire de travail
COPY ./webapp/requirements.txt ./app/requirements.txt
COPY ./webapp/server.py /app/server.py
COPY ./webapp/index.html /app/index.html

# installe les dépendances
RUN pip install -r ./app/requirements.txt

# définit les variables d'environnement
ENV PORT=5000
ENV DB_HOST=localhost
ENV DB_PORT=3306
ENV DB_USER=root
ENV DB_PASSWORD=root
ENV DB_NAME=mydb

# définit le point d'entrée de l'application
ENTRYPOINT ["python", "/app/server.py"]