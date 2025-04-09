FROM ghcr.io/dbt-labs/dbt-postgres:latest

WORKDIR /app
COPY . .

# Optional: install dbt dependencies
RUN dbt deps
