from sshtunnel import SSHTunnelForwarder
import requests
import paramiko

pkey = paramiko.RSAKey.from_private_key_file(private_key_path , password = private_key_password)

server = SSHTunnelForwarder(
    (remote_host, ssh_port),
    ssh_username=remote_user,
    ssh_private_key=pkey,
    remote_bind_address=('localtest.com', 8080),
    local_bind_address=('localhost', 80)
)

server.start()
try:
    r = requests.get(url = 'https://localtest:80/some/endpoint', verify=False)
finally:
    server.stop()