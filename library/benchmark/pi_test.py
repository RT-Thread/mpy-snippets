import time
import machine
import gc


def pi(places=100):
    extra = 8
    one = 10 ** (places + extra)
    t, c, n, na, d, da = 3 * one, 3 * one, 1, 0, 0, 24

    while t > 1:
        n, na, d, da = n + na, na + 8, d + da, da + 32
    t = t * n // d
    c += t
    return c // (10 ** extra)


def pi_test(n=5000):
    t1 = time.ticks_ms()
    pi(n)
    t2 = time.ticks_ms()
    r = time.ticks_diff(t2, t1) / 1000
    print(' Pi', n, 'digit calculation: ', r, 's')
    return '%.2f' % r


gc.collect()

try:
    d1 = pi_test(1000)
    d2 = pi_test(1000)
    d3 = pi_test(1000)
    r_pi_1000 = min(d1, d2, d3)
    print('1000 digit Pi calculation result: ', r_pi_1000, 's')
except:
    r_pi_1000 = None
    print(' calculation error')

print('\nCalcaulate Pi 5000 digit')
gc.collect()

try:
    d1 = pi_test(5000)
    d2 = pi_test(5000)
    d3 = pi_test(5000)
    r_pi_5000 = min(d1, d2, d3)
    print('5000 digit Pi calculation result: ', r_pi_5000, 's')
except:
    r_pi_5000 = None
    print(' calculation error')

print('\nCalcaulate Pi 100,000 digit')

gc.collect()
try:
    d1 = pi_test(100000)
    d2 = pi_test(100000)
    d3 = pi_test(100000)
    r_pi_100000 = min(d1, d2, d3)
    print('100000 digit Pi calculation result: ', r_pi_100000, 's')
except:
    r_pi_100000 = None
    print(' calculation error')

if r_pi_1000:
    print(' 1000 digit Pi calculation result: ', r_pi_1000, 's')
if r_pi_5000:
    print(' 5000 digit Pi calculation result: ', r_pi_5000, 's')
if r_pi_100000:
    print(' 100000 digit Pi calculation result: ', r_pi_100000, 's')
