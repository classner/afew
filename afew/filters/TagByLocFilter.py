# coding=utf-8
from __future__ import print_function, absolute_import, unicode_literals


from .BaseFilter import Filter


class TagByLocFilter(Filter):
    message = 'Looks for messages in a certain location and adds a tag if they dont have it.'

    def __init__(self, database,
                 folder='', tag=''):
        super(TagByLocFilter, self).__init__(database)
        assert folder != ''
        assert tag != ''
        self._folders = folder.split(" ")
        self._tags = tag.split(" ")

    def run(self, query):
        self.log.info(self.message)

        for folder, tag in zip(self._folders, self._tags):
            query = self.database.get_messages('folder:%s AND NOT tag:%s' % (
                folder, tag))
            for message in query:
                self.add_tags(message, tag)
