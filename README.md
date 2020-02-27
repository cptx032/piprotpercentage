# piprotpercentage
Your requirements.txt file is rotten by how many percent?

## Goal
The goal is to create a number/percentage to indicate how rotten is your requirements file (and in the future support pipenv too). This Package is inspired by https://github.com/sesh/piprot

## Usage
```sh
$ cd my-project/
$ ls
. .. requirements.txt
$ pip install git+https://github.com/cptx032/piprotpercentage.git
$ ROTTEN_PERCENTAGE=$(piprotpercentage.py ./requirements.txt)
$ echo My project is $ROTTEN_PERCENTAGE% rotten
```

## .gitlab-ci job example
```yml
piprotpercentage:
  stage: metrics
  image: python:2.7
  script:
    - pip install -r requirements.txt
    - pip install git+https://github.com/cptx032/piprotpercentage.git anybadge
    - anybadge --suffix='%' -l piprot --value=$(piprotpercentage.py requirements.txt) --file=piprotpercentage.svg 100=red 80=orange 60=yellow 50=green
  artifacts:
    paths:
      - piprotpercentage.svg
```
