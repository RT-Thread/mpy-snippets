# 
# Copyright (c) 2006-2019, RT-Thread Development Team
# 
# SPDX-License-Identifier: MIT License
# 
# Change Logs:
# Date           Author       Notes
# 2019-06-13     SummerGift   first version
#

import random

for j in range(0, 2):
    random.seed(13)                   # Specify random number seed
    for i in range(0, 10):            # Generate random sequences in the range of 0 to 10
        print(random.randint(1, 10))
    print("end")
