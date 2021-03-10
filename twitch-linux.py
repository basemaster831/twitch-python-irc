#!/bin/env python3
import socket

channel = "#channel_name"

s = socket.socket();
s.connect(('irc.chat.twitch.tv', 6667));

# justinfan<arbitrary number> gives us anonymous read access to IRC.
s.send(bytes('NICK ' + 'justinfan1238912381' + '\r\n', 'utf-8'));
s.send(bytes('JOIN ' + channel + '\r\n', 'utf-8'));

while True:
    # Twitch chat max is 500 characters + user name + IRC format, stays under 1024
    data = str(s.recv(1024));
    # Only looking for chat messages.
    if 'PRIVMSG' in data:
        #username provided between the first : and ! character.
        usr = data[data.find(':')+1:data.find('!')];
        # We can find the message by finding the first occurrence of '#'
        # and adding channel name length + 2 to skip over extra characters.
        # Then we are left with the "message\r\n" and we strip them with rstrip()
        msg = data[data.find('#')+len(channel)+2:data.find('\\r')].rstrip();
        print(f"{usr}: {msg}");


# Note: I am not very experienced with IRC, if you get randomly disconnected,
# it may be because twitch expects a PONG reply to their PING.
