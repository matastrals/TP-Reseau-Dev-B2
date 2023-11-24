##### Important : avant de commencer il faut veiller a bien config les ip client et server

```
[matastral@server TP4]$ python bs_server_I1.py
Connected by ('10.33.76.235', 37654)
b'Meooooo !'
```

```
[matastral@client TP4]$ python bs_client_I1.py
b'Hi mate !'
```

```
[matastral@server ~]$ ss -alp | grep python
tcp   LISTEN 0      1                                    10.33.76.234:13337                   0.0.0.0:*    users:(("python",pid=1434,fd=3))
```

### Partie 2 - A : Serveur

A la création du fichier server.log, il est nécessaire de faire des commandes sinon le programme plantera

```
sudo chown {utilisateur}:{utilisateur} /var/log/bs_server -R
sudo chmod 700 /var/log/bs_server/
sudo chmod 600 /var/log/bs_server/bs_server.log
```
### Partie 2 - B : Client

