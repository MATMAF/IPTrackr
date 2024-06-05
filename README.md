# What's my IP address ?
What's my IP address in python and html.

I use Flask as backend to get the IP address and the others informations.

Url of the latest version hosted: https://ip.matmaf.xyz

You can retrieve only the IP address: https://ip.matmaf.xyz/ip

## Features
* IP address
* Internet provider
* Country

## Build the docker image
`docker build -t whatsmyipaddress .`

## Docker compose
```
services:
  whatsmyipaddress:
    image: whatsmyipaddress
    container_name: whatsmyipaddress
    ports:
      - 8000:8000
```
