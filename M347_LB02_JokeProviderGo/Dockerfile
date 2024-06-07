# Hier verwende ich das offizielle Golang 1.19-Image als Basis.
FROM golang:1.19

# Hier setze ich das Arbeitsverzeichnis innerhalb des Containers auf /app.
WORKDIR /app

# Hier kopiere ich den aktuellen Inhalt des lokalen Verzeichnisses (Dockerfile-Verzeichnis) in das Arbeitsverzeichnis des Containers (/app).
COPY . .

# Hier wird der Befehl 'go build' ausgeführt, um die Go-Anwendung zu kompilieren und um die Ausgabedatei "jokeprovider" zu nennen.
RUN go build -o jokeprovider .

# Dies ist der Befehl, der auf der Konsole ausgeführt wird, wenn der Container gestartet wird und somit den "jokeprovider" startet.
CMD go run .

