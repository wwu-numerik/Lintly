# Merge config with configuration pulled from CI providers


class Config(object):
    """A Config object that knows how to return configuration from the CLI or Continuous Integration services"""

    def __init__(self, cli_config, ci=None):
        self.cli_config = cli_config
        self.ci = ci

    def as_dict(self):
        return {
            'pr': self.pr,
            'repo': self.repo,
            'commit_sha': self.commit_sha,
            'api_key': self.api_key,
            'format': self.format,
            'site_url': self.site_url,
            'fail_on': self.fail_on,
            'post_status': self.post_status,
        }

    @property
    def pr(self):
        return self.cli_config['pr'] or getattr(self.ci, 'pr')

    @property
    def repo(self):
        return self.cli_config['repo'] or getattr(self.ci, 'repo')

    @property
    def commit_sha(self):
        return self.cli_config['commit_sha'] or getattr(self.ci, 'commit_sha')

    @property
    def api_key(self):
        return self.cli_config['api_key']

    @property
    def format(self):
        return self.cli_config['format']

    @property
    def site_url(self):
        return self.cli_config['site_url']

    @property
    def fail_on(self):
        return self.cli_config['fail_on']

    @property
    def post_status(self):
        return self.cli_config['post_status']
