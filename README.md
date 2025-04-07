# Python CI/CD Project 

This is a basic Python project structured for experimentation. It includes:
- Source package with modules
- Unit tests
- CI/CD setup via Jenkinsfile
- Poetry configuration
- Publishing to PyPI Sandbox


Oracle VM Box Manager - 6.1.2

Docker install in CentOS - https://docs.docker.com/engine/install/centos/#install-using-the-repository
Running docker in VM with non-root user - https://docs.docker.com/engine/install/linux-postinstall/
Install docker compose - https://docs.docker.com/compose/install/standalone/

Docker CICD Image - docker pull rahuldeyfb39/jenkins-cicd:latest or docker pull rahuldeyfb39/jenkins-cicd:2.42

<pre lang="md">
services:
  jenkins:
    container_name: jenkins-cicd-all
    image: rahuldeyfb39/jenkins-cicd:2.42
    ports:
      - "8080:8080"
    volumes:
      - $PWD/jenkins_home:/var/jenkins_home
    networks:
      - net
networks:
  net:
</pre>

<pre lang="md">
create $HOME/jenkins-data/jenkins_home
$HOME/jenkins-data/jenkins_home/docker-compose.yml
sudo chown 1000:1000 jenkins_home -R
</pre>

<pre lang="md">
Docker command -
docker-compose up -d
docker-compose down
docker logs -f <container_id or name>
docker exec -u root -it <container_id or name> /bin/bash
docker images
docker ps
docker ps -a
docker rmi <image_id>
docker image prune
docker container prune
</pre>