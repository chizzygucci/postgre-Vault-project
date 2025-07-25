import hvac
import os

client = hvac.Client(url=os.environ['VAULT_ADDR'], token=os.environ['VAULT_TOKEN'])
secret = client.secrets.kv.v2.read_secret_version(path='flaskapp')
print(secret)
