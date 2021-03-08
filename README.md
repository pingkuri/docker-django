# docker-django installation

    git clone https://github.com/zuzu1014/docker-django 

    docker-compose up --build


# you should do this first

    curl -fsSL https://get.docker.com/ | sudo sh  # docker install
    sudo usermod -aG docker $USER  # authorization

    sudo curl -L https://github.com/docker/compose/releases/download/1.25.0-rc2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose  # install docker-compose 설치
    sudo chmod +x /usr/local/bin/docker-compose  # authorization
