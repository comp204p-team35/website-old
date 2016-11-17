from invoke import task


@task
def build_site(c, production=False):
    if production:
        c.run('jekyll build --config=_config.yml,_config_prod.yml')
    else:
        c.run('jekyll build')
