from invoke import task
import server_keys


@task
def publish(c):
    with c.cd('i:\\Romeno\\Projects\\PyCharm\\chronotrack'):
        c.run("python setup.py sdist bdist_wheel")
        c.run("twine upload dist/* -u {} -p {}".format(server_keys.PYPI_USERNAME, server_keys.PYPI_PASSWORD))


