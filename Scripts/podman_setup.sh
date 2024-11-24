#!/bin/bash
# podman_setup.sh

# Pull a container image (example: Python 3.9)
podman pull python:3.9

# Run the Podman container with your code mounted
podman run -d --name my-python-container -v /path/to/your/code:/container/code python:3.9

# Access the running container's shell
podman exec -it my-python-container bash
