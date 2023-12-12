FROM ghcr.io/google/nsjail/nsjail:latest

RUN apt-get update

COPY meltdown.c /home/meltdown/
COPY flag.txt /home/meltdown/flag.txt

RUN gcc meltdown.c -o meltdown.sh

WORKDIR /home/meltdown/

CMD ["nsjail",                             \
        "-Ml",                            \
        "--hostname", "retro",           \
        "--port", "6666",               \
        "--chroot", "/",            \
        "--cwd", "/home/videorental/",        \
        "--",                     \
        "videorental0"  \
        ]
