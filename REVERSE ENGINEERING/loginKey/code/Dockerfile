# Use an official GCC image as the base
FROM gcc:latest

# Set the working directory in the container
WORKDIR /usr/src/myapp

# Copy the source files into the container
COPY main.c .
COPY users.c .
COPY users.h .

# Compile the C program
RUN gcc -o myapp main.c users.c

# Indicate the port on which your app will run
EXPOSE 1234

# When the container launches, run the compiled program
CMD ["./myapp"]
