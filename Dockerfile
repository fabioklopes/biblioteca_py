# Use a imagem oficial do Python como base
FROM python:3.11-slim-bookworm

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da sua aplicação
COPY . .

# Opcional: Definir variáveis de ambiente Django
ENV DJANGO_SETTINGS_MODULE=myproject.settings.production

# Expor a porta que o seu servidor Django (Gunicorn/UWSGI) irá escutar
EXPOSE 8000

# Comando para iniciar a aplicação Django (usando Gunicorn como exemplo)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]