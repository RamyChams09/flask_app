FROM ubuntu:latest
LABEL authors="rchamsed"

ENTRYPOINT ["top", "-b"]