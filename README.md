# twitch-python-irc
Extremely basic python3 twitch IRC connection with no Oauth requirement.

```python
import socket

s = socket.socket()
s.connect(('irc.chat.twitch.tv', 6667))
# justinfan<arbitrary number> gives you anonymous access to irc.
s.send(bytes('NICK ' + 'justinfan12345678009' + '\r\n', 'utf-8'))
s.send(bytes('JOIN ' + '#twitch_channel' + '\r\n', 'utf-8'))

while True:
    print(s.recv(1024))
````

