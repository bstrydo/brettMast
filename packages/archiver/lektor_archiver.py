# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin


class ArchiverPlugin(Plugin):
    name = u'archiver'
    description = u'This plugin archives old articles.'

    def on_before_build_all(self, builder, **extra):
        print 'hello world, brett is going wild'
