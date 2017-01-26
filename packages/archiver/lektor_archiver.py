# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin


class ArchiverPlugin(Plugin):
    name = u'archiver'
    description = u'This plugin archives old articles.'

    def on_process_template_context(self, context, **extra):
        def test_function():
            return 'Value from plugin %s' % self.name
        context['test_function'] = test_function
