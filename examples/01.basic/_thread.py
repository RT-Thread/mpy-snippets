#
# Copyright (c) 2006-2019, RT-Thread Development Team
#
# SPDX-License-Identifier: MIT License
#
# Change Logs:
# Date           Author       Notes
# 2019-06-13     SummerGift   first version
#

import gc
import _thread

def testThread():
    count = 0
    while (count < 9):
        print("Hello rt-thread!")
        count += 1

    print("Thread exit!")
    gc.collect()    # Free the memory space requested by the thread

# TestThread thread is created with an empty argument
_thread.start_new_thread(testThread, ())
