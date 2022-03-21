from django_hosts import patterns, host

host_patterns = patterns('',
    # Bonus domain patterns to handle.
    host(r'registration.localhost:8000', 'hunt.deploy.urls.registration', name="registration-dev"),
    host(r'localhost:8000', 'hunt.deploy.urls.site', name="site-dev"),

    host(r'pure-journey-13265.herokuapp.com', 'hunt.deploy.urls.unified', name='heroku', scheme='https://'),

    # Our real domains.
    # host(r'www.mitmh2022.com', 'hunt.deploy.urls.registration', name='registration', scheme='https://'),
    # host(r'mitmh2022.com', 'hunt.deploy.urls.registration', name='registration-no-www'),
    # host(r'www.starrats.org', 'hunt.deploy.urls.site', name='site-1', scheme='https://'),
    # host(r'starrats.org', 'hunt.deploy.urls.site', name='site-1-no-www'),
    # host(r'www.bookspace.world', 'hunt.deploy.urls.site', name='site-2', scheme='https://'),
    # host(r'bookspace.world', 'hunt.deploy.urls.site', name='site-2-no-www'),

    # Our heroku-provided domain.
    # host(r'palindrome-hunt-prod.herokuapp.com', 'hunt.deploy.urls.unified', name='heroku', scheme='https://'),

    # The host to use by default.
    host(r'pure-journey-13265.herokuapp.com', 'hunt.deploy.urls.unified', name='default', scheme='https://'),
    # host(r'www.mitmh2022.com', 'hunt.deploy.urls.registration', name='default', scheme='https://'),
)
