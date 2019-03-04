#!/usr/local/bin/python3
# Encoding: UTF-8
# Style guide: pep8
"""
Created: 01 February 2019
Author: Sai Sugeeth Kamineni
"""

from random import randint
from random import seed
from random import SystemRandom
from scipy.stats import chi2
from collections import Counter

ITERATIONS = 13
n = 5000
a = 1
b = 1000
conf1 = 95
conf2 = 99


def gen_seed_arr(iter):
    arr = []
    for i in range(iter):
        arr.append(randint(-1000000, 1000000))
    return arr


def data_gen_py(n, a, b, s):
    data = []
    seed(s)
    for j in range(n):
        data.append(randint(a, b))
    return data


def data_gen_os(n, a, b, s):
    data = []
    rand = SystemRandom()
    rand.seed(s)
    for j in range(n):
        data.append(rand.randint(a, b))
    return data


def chi_sq_stat(data, n, a, b):
    freq = Counter(data)
    chi2stat = 0
    exp = n / (b - a + 1)
    for i in range(a, b + 1):
        if i in freq:
            chi2stat += (freq[i] - exp)**2 / exp
        else:
            chi2stat += exp
    return chi2stat


def chi_sq_test(chi2stat, a, b, conf):
    df = b - a
    alpha = 1 - float(conf) / 100
    chi2crit = chi2.ppf(alpha, df)
    if chi2stat < chi2crit:
        return 1
    else:
        return 0


if __name__ == '__main__':
    seeds = gen_seed_arr(ITERATIONS)
    total_result_py_conf1 = 0
    total_result_os_conf1 = 0
    total_result_py_conf2 = 0
    total_result_os_conf2 = 0
    for i in range(ITERATIONS):
        s = seeds[i]
        data_py = data_gen_py(n, a, b, s)
        data_os = data_gen_os(n, a, b, s)
        chi2stat_py = chi_sq_stat(data_py, n, a, b)
        chi2stat_os = chi_sq_stat(data_os, n, a, b)
        print("Chi2 stat. for python iteration no.", i, "is", chi2stat_py, ".")
        print("Chi2 stat. for OS iteration no.", i, "is", chi2stat_os, ".")
        total_result_py_conf1 += chi_sq_test(chi2stat_py, a, b, conf1)
        total_result_os_conf1 += chi_sq_test(chi2stat_os, a, b, conf1)
        total_result_py_conf2 += chi_sq_test(chi2stat_py, a, b, conf2)
        total_result_os_conf2 += chi_sq_test(chi2stat_os, a, b, conf2)
    print(">Result of Python for 95 percent confidence:",
          total_result_py_conf1, "out of", ITERATIONS)
    print(">Result of OS for 95 percent confidence:",
          total_result_os_conf1, "out of", ITERATIONS)
    print(">Result of Python for 99 percent confidence:",
          total_result_py_conf2, "out of", ITERATIONS)
    print(">Result of OS for 99 percent confidence:",
          total_result_os_conf2, "out of", ITERATIONS)
