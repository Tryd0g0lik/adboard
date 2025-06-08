import os
from django.contrib.staticfiles.storage import StaticFilesStorage


class PathCustomisationStorage(StaticFilesStorage):
    def path(self, name):

        return os.path.join("/static", name)
