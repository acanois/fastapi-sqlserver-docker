# Use amd64 base
FROM --platform=linux/amd64 python:3.11-bookworm

WORKDIR /src

# Install packages
RUN apt-get update && apt-get install -y curl gnupg2 apt-transport-https

# Add Microsoft repo and install msodbcsql17
RUN curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg && \
    echo "deb [arch=amd64] https://packages.microsoft.com/debian/12/prod bookworm main" > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev g++

# App and pip deps
COPY . /src
COPY requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /src/requirements.txt

CMD ["fastapi", "run", "app.py", "--proxy-headers", "--port", "80"]
