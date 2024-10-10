# Usar uma imagem oficial do Python
FROM python:3.9-slim

# Configurar diretório de trabalho
WORKDIR /app

# Instalar as dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar o código do projeto
COPY . .

# Rodar as migrações e iniciar o servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
