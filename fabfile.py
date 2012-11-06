import os
import fileinput
import shutil
import time
from fabric.api import local, task, cd, run, env, get, lcd
from fabric.colors import red, green

#-------
# Tasks
#--------


@task
def ls_remote():
    """
    List remote default directory
    Usage: fab ls_remote -H <host> -u <user>
    """
    with cd('.'):
        run('ls -l')


@task
def install_req():
    """
    Install all required Django packages reading a requirement file
    """
    local('pip install -r requirements/project.txt')


@task
def create_req_file():
    """
    Create a requirements file for pip
    """
    local('pip freeze > requirements/project.txt')


@task
def generate_static():
    """
    Run collectstatic and compress Django commands
    """
    local('python manage.py collectstatic --noinput && python manage.py compress --force')


@task
def gen_key():
    """
    Generates a new Django secret key
    """
    local('python manage.py generate_secret_key')


@task
def del_pyc():
    """
    Delete *.pyc of your project
    """
    local('find . -name \*.pyc | xargs rm')
