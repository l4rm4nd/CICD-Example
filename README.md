# CICD-Example
Basic example of CI/CD for an Nginx Docker image

````
# pull latest image; pushed by github action runner
docker pull ghcr.io/l4rm4nd/cicd-example:latest

# run the container via docker run
docker run --rm -p 8888:80 ghcr.io/l4rm4nd/cicd-example:latest
````
