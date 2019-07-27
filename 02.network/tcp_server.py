# 
# Copyright (c) 2006-2019, RT-Thread Development Team
# 
# SPDX-License-Identifier: MIT License
# 
# Change Logs:
# Date           Author       Notes
# 2019-06-13     SummerGift   first version
#

import usocket

# Create STREAM TCP socket
server = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
server.bind(('192.168.12.203', 6001))
server.listen(5)
server.setblocking(True)

while True:
    # Wait for client connection
    clientsocket, addr = server.accept()
    print("connect address: %s" % str(addr))
    clientsocket.send('welcome to rt-thread micropython!')
    clientsocket.close()
