FROM ghcr.io/google/nsjail/nsjail:latest

RUN apt-get update

COPY meltdown.c /home/meltdown/meltdown.c
COPY flag.txt /home/meltdown/flag.txt

RUN gcc meltdown.c -o meltdown.sh

WORKDIR /home/meltdown/

CMD ["nsjail",                             \
        "-Ml",                            \
        "--hostname", "melt",           \
        "--port", "6666",               \
        "--chroot", "/",            \
        "--cwd", "/home/meltdown/",        \
        "--",                     \
        "./meltdown.sh"  \
        ]
