# Project: flask-postgres-integration-with-vault-secrets


# problem encounterd and solutions


 Problem: Virtual Environment Files Committed to Git
After running git commit, I noticed hundreds of create mode entries like this:

create mode 100644 venv/lib/python3.12/site-packages/werkzeug/middleware/http_proxy.py
create mode 100644 venv/lib/python3.12/site-packages

This meant that the entire venv/ (Python virtual environment) directory was mistakenly committed to the Git repository.

# Solution: Remove venv/ from Git Tracking

stop tracking the venv/ directory

git rm -r --cached venv/
Add venv/ to .gitignore
created nano .gitignore
git add .gitignore
git commit -m 

# Vault Connection Refused

 requests.exceptions.ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=8200): Max retries exceeded with url: /v1/secret/data/flaskapp
(Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f964b792b70>: Failed to establish a new connection: [Errno 111] Connection refused'))

Solution:

1. Vault server was not running. I resolved this by starting the development Vault server:
vault server -dev

Ensure the following environment variables are set after Vault is running:

export VAULT_ADDR=http://127.0.0.1:8200



# PostgreSQL Password Authentication Failed

psycopg2.OperationalError: connection to server at "database-1.c4hqgo48oo80.us-east-1.rds.amazonaws.com" (98.85.235.233), port 5432 failed:
FATAL: password authentication failed for user "postgres"

Double-checked the password stored in Vault and updated it using:
vault kv put secret/flaskapp connection_string="postgresql://postgres:<correct-password>@<RDS-ENDPOINT>:5432/postgres"


# No pg_hba.conf Entry

try for host "102.88.114.64", user "postgres", database "postgres", no encryption

# Solution:

This issue occurred because the RDS PostgreSQL instance did not allow connections from my machine's public IP.

I resolved it by:

Logging into the AWS Console.

Modifying the RDS security group to allow inbound connections from my IP address on port 5432.



export VAULT_TOKEN=<your-root-token>
