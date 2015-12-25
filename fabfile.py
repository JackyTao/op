from fabric.api import (local,
                        run,
                        env,
                        task,
                        roles,
                        execute,
                        runs_once,
                        put)

from fabric.context_managers import cd, lcd

env.roledefs = {
    'test_back': [
        'root@10.16.4.157'
    ],
    'test_task': [
        'root@10.16.4.157'
    ],
    'online_back': [
        'root@10.16.5.160',
        'root@10.16.5.161',
    ], 
    'online_task': [
        'root@10.16.4.156'    
    ],
}


# Allow: online back
def copy_nginx_conf():
    put('./conf/nginx.conf',
        '/opt/conf/nginx/nginx.conf')
    put('./conf/mime.types',
        '/opt/conf/nginx/mime.types.pos')


# Allow: online back
def restart_nginx():
    run('if [[ -f /opt/conf/nginx/nginx.pid ]];'
        'then kill -HUP $(cat /opt/conf/nginx/nginx.pid);'
        'else /opt/sysapp/nginx/sbin/nginx -c /opt/conf/nginx/nginx.conf;'
        'fi;')
    run('sleep 3;'
        'ps -ef | grep nginx | grep -v grep;')


def copy_supervisor_conf():
    conf_name = {
        'online_back': 'supervisord.conf',
        'online_task': 'supervisord.conf.task',
        'test_back': 'supervisord.conf.test',
        'test_task': 'supervisord.conf.test',
    }
    put('./conf/{fn}'
        .format(fn=conf_name.get(env.roles[0])),
        '/opt/www/supervisor_rt/supervisord.conf.pos')


def restart_supervisor():
    run('if [[ -f /opt/www/supervisor_rt/supervisord.pid ]];'
        'then kill -HUP $(cat /opt/www/supervisor_rt/supervisord.pid);'
        'else supervisord -c /opt/www/supervisor_rt/supervisord.conf;'
        'fi;')
    run('sleep 3;'
        'ps -ef | grep webapp | grep -v grep;'
        'ps -ef | grep supervisor | grep -v grep;')


# Allow: online back
# $ fab pub_package:package_path=*** -R online_back
def pub_package(package_path):
    put(package_path,
        '/opt/www/pub/package/')
    import os
    package_name_real = os.path.split(package_path)[-1]
    package_name_fake = 'health_plus_latest-offical.apk'
    with cd('/opt/www/pub/package/'):
        run('ln -f -s {real} {fake}'
            .format(real=package_name_real, fake=package_name_fake))


# static_path is dirs under asset/static
# $ fab pub_static:static_path=./asset/static/imgs -R online_back
def pub_static(static_path):
    put(static_path, '/opt/www/pub/static/')


def pub_eguahao():
    put('./script/eguahao.js',
        '/opt/www/static/js/')


# static_path is dirs under asset/static
# $ fab pub_script:script_path=./script/log-rotate.sh -R online_back
def pub_script(script_path):
    put(script_path, '/opt/logs/')
