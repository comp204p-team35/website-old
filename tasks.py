from invoke import task


@task
def build_site(c, production=False):
    if production:
        print('building production site...')
        c.run('jekyll build --config=_config.yml,_config_prod.yml')
    else:
        print('building development site...')
        c.run('jekyll build')
    print('done')
