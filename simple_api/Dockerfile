# Utilise une image Python légère officielle
FROM python:3.11-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier requirements.txt et installe les dépendances
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copie tout le contenu du dossier courant (ton code Flask)
COPY . .

# Expose le port sur lequel l’application Flask tourne
EXPOSE 5000

# Commande pour lancer ton API Flask
CMD ["python", "student_age.py"]
