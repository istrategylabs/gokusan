import aws_helper


class S3Deploy(object):
    """ `S3Deploy` is the main class responsible for handling the management and deployment of a static site """

    def __init__(self, repo_name):
        self.project_name = convert_project_name(repo_name)

    def convert_project_name(self, repo_name):
        pass

    def build_project(self):
        pass
