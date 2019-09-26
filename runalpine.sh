#!/bin/zsh
exec sudo docker run -d -p 5566:5566 -p 8118:8118 -p 2090:2090 -e tors=25 -e privoxy=1 -e test_url=http://httpbin.org/ip zeta0/alpine-tor:latest3
