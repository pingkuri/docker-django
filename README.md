# docker-django

    리눅스/우분투 환경에서 git clone https://github.com/pingkuri/docker-django.git 후에

    docker-compose up --build를 하시면

    웹페이지를 확인할 수 있습니다.

# 선행 작업

    우분투 환경에서 docker-compose를 실행하기 위해 docker와 docker-compose를 설치하고 권한을 부여해야합니다.

    curl -fsSL https://get.docker.com/ | sudo sh  # docker 설치
    sudo usermod -aG docker $USER  # 권한 부여

    sudo curl -L https://github.com/docker/compose/releases/download/1.25.0-rc2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose  # docker-compose 설치
    sudo chmod +x /usr/local/bin/docker-compose  # 권한 부여
