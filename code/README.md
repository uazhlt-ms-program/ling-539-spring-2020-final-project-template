# Code

_TODO: Describe how your code is organized and provide step-by-step instructions for running your code.  All dependencies should be containerized (using either [Docker](https://www.docker.com/why-docker) or [Singularity](https://sylabs.io/guides/latest/user-guide/)).  Feel free to modify the example [`Dockerfile`](https://docs.docker.com/engine/reference/builder/) and [`requirements.txt`](https://pip.readthedocs.io/en/1.1/requirements.html#requirements-files) (or replace with a [Singularity definition file](https://sylabs.io/guides/3.4/user-guide/quick_start.html#singularity-definition-files)) to suit your project's needs.  NOTE: You are not required to use a particular programming language, so long as your you provide intstructions for building and running a working container._

## Building the container

_TODO: Correct this to reflect the name of your team._

```
docker build -f Dockerfile -t "ling-539/final-project:latest" .
```

### Removing old docker containers, images, etc.

If you want to save some space on your machine by removing images and containers you're no longer using, [see the instructions here](https://docs.docker.com/config/pruning/).  As always, use caution when deleting things.
