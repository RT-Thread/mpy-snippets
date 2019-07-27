# 
# Copyright (c) 2006-2019, RT-Thread Development Team
# 
# SPDX-License-Identifier: MIT License
# 
# Change Logs:
# Date           Author       Notes
# 2019-06-13     SummerGift   first version
#

import rtthread

# determine if code is running in a preemptible thread
print(rtthread.is_preempt_thread())
print(rtthread.current_tid())            # current thread id
rtthread.stacks_analyze()                 # show thread information
