# Hier verwende ich das offizielle Python 3.12-Image als Basis.
FROM python:3.7

# Hier setze ich das Arbeitsverzeichnis innerhalb des Containers auf /app.
WORKDIR /app

# Hier füge ich  den aktuellen Inhalt des lokalen Verzeichnisses (Dockerfile-Verzeichnis) in das Arbeitsverzeichnis des Containers (/app).
ADD . /app

# Hier wird der Port 5002 im Container geöffnet.
EXPOSE 5002

# Dies ist der Befehl, der auf der Konsole ausgeführt wird, wenn der Container gestartet wird und somit den "jokeconsumer" startet.
CMD python app.py
