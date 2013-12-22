from fabric.api import *
import fabtools.require

from fabtools.vagrant import vagrant


@task
def upgrade():

    # Update packages list and upgrade system before running install
    sudo("apt-get update")


@task
def install():

    fabtools.require.deb.packages([
        'build-essential',
        'devscripts',
        'locales',
        'nginx',
        'sqlite3',
        'ruby',
        'curl',
        'git',
        'gcc',
        'python-dev',
        'python-psycopg2',
        'libpq-dev',
        'memcached',
    ], update=False)

    fabtools.require.system.locale('fr_FR.UTF-8')
    fabtools.require.postgres.server()
    fabtools.require.postgres.user('vagrant', 'vagrant', createrole=True)
    fabtools.require.postgres.database('{{ project_name }}', 'vagrant')
    fabtools.require.redis.instance('{{ project_name }}')

    if not fabtools.files.is_file('.pgpass'):
        run('echo "*:*:{{ project_name }}:{{ project_name}}:{{ project_name}}" >> .pgpass')
        run('chmod 0600 .pgpass')

    with cd('/{{ project_name}}/'):
        run('./install.sh')


@task
def run_server():
    with cd('/{{ project_name }}/'):
        run('source ./venv/bin/activate && cd betmilk && ./manage.py runserver 0.0.0.0:8000')


@task
def run_celery():
    with cd('/{{ project_name }}/'):
        run('source ./venv/bin/activate && cd betmilk && ./manage.py celery worker')


@task
def deploy_dev():
    with cd('/{{ project_name }}/'):
        run('source ./venv/bin/activate && fab dev deploy')


@task
def deploy_prod():
    with cd('/{{ project_name }}/'):
        run('source ./venv/bin/activate && fab prod deploy')
