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

