# Trivial Docker Demo

Trivial demo for [scratch](https://hub.docker.com/_/scratch/) docker construction.

Static compiles are required for inserting binaries directly into a scratch docker:
```commandline
gcc hello.c -o hello -static
```

Test the compiled executable:
```commandline
./hello
```

Build and run the docker:
```commandline
sudo docker build -t hello_image .
sudo docker create --name hello_container hello_image
sudo docker start -i hello_container
```
