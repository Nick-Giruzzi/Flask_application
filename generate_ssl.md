# How to generate self-signed certs for website

1. openssl genrsa -out server.key 2048
2. openssl req -new -key server.key -out server.csr
3. openssl x509 -req -days 3650 -in server.csr -signkey server.key -out server.crt
