from flask import Flask
import psycopg2
import hvac
import os

app = Flask(__name__)

def get_db_uri():
    client = hvac.Client(url=os.environ['VAULT_ADDR'], token=os.environ['VAULT_TOKEN'])
    secret = client.secrets.kv.v2.read_secret_version(path='flaskapp')
    return secret['data']['data']['connection_string']

@app.route("/")
def index():
    conn = psycopg2.connect(get_db_uri())
    cur = conn.cursor()
    cur.execute("SELECT 'Hello from RDS!'")
    result = cur.fetchone()
    return result[0]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
