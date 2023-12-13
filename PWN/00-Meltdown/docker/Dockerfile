FROM ghcr.io/google/nsjail/nsjail:latest

RUN apt-get update

COPY testOldSource.c /home/meltdown/testOldSource.c
COPY flag.txt /home/meltdown/flag.txt

WORKDIR /home/meltdown/

RUN gcc testOldSource.c -o testOldMeltdown.sh

CMD ["nsjail",                             \
        "-Ml",                            \
        "--hostname", "melt",           \
        "--port", "6666",               \
        "--chroot", "/",            \
        "--cwd", "/home/meltdown/",        \
        "--",                     \
        "./testOldMeltdown.sh"  \
        ]
