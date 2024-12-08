
FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Install PostgreSQL
RUN apt-get update && \
    apt-get install -y postgresql postgresql-contrib && \
    apt-get clean

# Start PostgreSQL
RUN service postgresql start

# Set up PostgreSQL
USER postgres
RUN /etc/init.d/postgresql start && \
    psql --command "CREATE USER codespaces WITH SUPERUSER PASSWORD 'password';" && \
    createdb codespaces

USER vscode
