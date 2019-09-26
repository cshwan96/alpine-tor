#!/usr/bin/env python3
import subprocess

print("HTTP testing")
pidlist = list()
for i in range(10):
	pidlist.append(subprocess.Popen("curl --proxy localhost:8118 http://httpbin.org/ip".split()))
list(map(lambda x: x.wait(), pidlist))

pidlist = list()

print("Socks testing")
for i in range(10):
	pidlist.append(subprocess.Popen("curl --proxy socks5h://localhost:5566 http://httpbin.org/ip".split()))
list(map(lambda x: x.wait(), pidlist))
