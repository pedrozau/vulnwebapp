# Usando uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo de requisitos do Python
COPY requirements.txt .

# Instalar as dependências
RUN pip install -r requirements.txt

# Copiar todo o conteúdo da aplicação para dentro do contêiner
COPY . .



# Comando para rodar a aplicação Flask
CMD ["python", "app.py"]
