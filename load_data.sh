#!/bin/bash

set -e  # Exit on error

DB_URL="postgres://myuser:mypassword@localhost:5432/mydatabase"

psql "$DB_URL" <<EOF
DROP TABLE IF EXISTS public.people;
CREATE TABLE public.people (
    regional_manager TEXT,
    region TEXT
);

DROP TABLE IF EXISTS public.returns;
CREATE TABLE public.returns (
    returned TEXT,
    order_id TEXT
);
EOF

psql "$DB_URL" -c "\COPY public.people FROM './people.csv' WITH CSV HEADER"
psql "$DB_URL" -c "\COPY public.returns FROM './returns.csv' WITH CSV HEADER"

