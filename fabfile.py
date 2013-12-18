from fabric.api import *
from fabric.colors import *

env.user = 'vagrant' #'asisco'
env.password = "vagrant"
env.hosts = ['vagrant@192.168.33.10'] #['asisco@198.199.106.64']
env.project_name = "asisco-orderofservice"
env.root_env = "/home/vagrant" #"/deploy"
env.project_env = "%(root_env)s/%(project_name)s/" % env 
env.git_host = "https://github.com/fabianogoes/"

@task
def install_tools(passwd):
    print(blue("**************************************************"))
    print(green("apt-get update..."))
    print(blue("**************************************************"))
    env.password = passwd
    sudo("apt-get update")
    
    print(blue("**************************************************"))
    print(green("install tools..."))
    print(blue("**************************************************"))    
    sudo("apt-get install python-dev -y")
    sudo("apt-get install python-setuptools -y")
    sudo("easy_install pip")
    sudo("pip install virtualenv")
    sudo("sudo apt-get install git-core -y")

    deploy(passwd)
    run_project()


@task
def create_virtualenv():
    with cd("%(root_env)s" % env):
        print(blue("**************************************************"))
        print(green("creating virtualenv..."))
        print(blue("**************************************************"))
        ################################################################################
        # The --no-site-packages flag is deprecated; it is now the default behavior.
        ################################################################################
        run('virtualenv %(project_name)s --clear --distribute' % env)    


@task
def git_clone():
    with cd("%(root_env)s" % env):
        print(blue("**************************************************"))
        print(green("executing git clone..."))    
        print(blue("**************************************************"))
        run('git clone %(git_host)s%(project_name)s.git' % env)


@task
def activate_env():
    with cd("%(project_env)s" % env):
        print(blue("**************************************************"))
        print(green("activating virtualenv..."))
        print(blue("**************************************************"))
        run('source bin/activate')


@task
def install_requirements():
    with cd("%(project_env)s" % env):
        print(blue("**************************************************"))
        print(green("instaling requirements..."))
        print(blue("**************************************************"))
        run('bin/pip install -r requirements.txt')    


@task
def execute_syncdb():
    with cd("%(project_env)s" % env):
        print(blue("**************************************************"))
        print(green("executing syncdb..."))
        print(blue("**************************************************"))
        run('bin/python manage.py syncdb --noinput')


@task
def execute_migrate():
    with cd("%(project_env)s" % env):
        print(blue("**************************************************"))
        print(green("executing migrate..."))
        print(blue("**************************************************"))
        run('bin/python manage.py migrate --noinput')
        run('bin/python manage.py migrate --list')


@task
def run_project():
    with cd("%(project_env)s" % env):
        print(blue("**************************************************"))
        print(green("run project..."))
        print(blue("**************************************************"))
        run('DEBUG=True bin/python manage.py runserver 0.0.0.0:9090')


@task
def deploy(passwd=None):
    #exemplo de uso: fab deploy:password=152776
    env.password = passwd
    with hide('running'):
        print(green("instaling environment of deploy..."))
        git_clone()

        create_virtualenv()

        activate_env()

        install_requirements()

        execute_syncdb()

        execute_migrate()
