# Kubernetes test service

Docker image: https://hub.docker.com/r/ullyzian/flask-app

## Rolling update locally:

Link: https://dzone.com/articles/running-local-docker-images-in-kubernetes-1

### Steps:

- Create new docker image build with new tag version:
  `docker build -t ullyzian/flask-app:<tag> . --rm`
- Update kubernetes web image:
  `kubectl set image deployments/web flask=flask-app:<tag> --record`