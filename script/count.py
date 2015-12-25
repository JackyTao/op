#!/usr/bin/env python

import sys

log_file_name = sys.argv[1]


def count_api_time():
    lines = []
    for line in file(log_file_name):
        line = line.strip()
        if line.endswith('ms'):
            _, rt = line[:-2].rsplit(' ', 1)
            try:
                rt = float(rt)
                if rt > 500:
                    lines.append([rt, line])
            except:
                continue
    rst = sorted(lines, key=lambda x: x[0])
    for i in rst:
        print i


def count_nginx_time():
    lines = []
    for line in file(log_file_name):
        fields = line.strip().split(',,')

        try:
            req_time, up_res_time = map(float, fields[11:13])
            if req_time > 0.001 or up_res_time > 0.001:
                lines.append([req_time, up_res_time, line.strip()])
        except:
            continue
    rst = sorted(lines, key=lambda x: x[0])
    for i in rst:
        print i


if __name__ == '__main__':
    count_nginx_time()
    #count_api_time()
