# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin

import os
import datetime

class archiver(object):
    def __init__(self, content_root, exclude_list):
        self.root = content_root
        self.archive_root = os.path.join(self.root, 'archive')
        self.exclude_list = exclude_list
        self.exclude_list.append('archive')

    def extract_pub_date(self, path):
        for line in open(path).xreadlines():
            if line.startswith('pub_date:'):
                return datetime.datetime.strptime( line.split(':')[1].strip(), "%Y-%m-%d").date()
        return None

    def file_matches_archive_rules(self, path):
        pub_date = self.extract_pub_date(path)

        if pub_date == None: return False

        if pub_date < datetime.date.today(): return True

        return False

    def archive(self, dirname, filename='contents.lr'):
        if not self.file_matches_archive_rules(os.path.join(dirname, filename) ): return

        archive_date = self.extract_pub_date(os.path.join(dirname, filename))
        if archive_date == None: return


        if not os.path.isdir(self.archive_root) :
            os.makedirs(self.archive_root)


        archive_date_dir = os.path.join(self.archive_root, archive_date.strftime('%Y-%m-%d'))
        if not os.path.isdir(archive_date_dir) :
            os.makedirs(archive_date_dir)

        archive_dir = os.path.join(archive_date_dir, os.path.basename(dirname) )
        os.rename(dirname, archive_dir)

    def run(self):
        for directory_entry in os.listdir(self.root):
            full_path = os.path.join(self.root, directory_entry)

            if os.path.isdir(full_path) and directory_entry not in self.exclude_list :
                self.archive(full_path)

class ArchiverPlugin(Plugin):
    name = u'archiver'
    description = u'This plugin archives old articles.'

    def on_before_build_all(self, builder, **extra):
        ar = archiver('/Users/techops/projects/mast/brettMast/content', ['about', 'blog'])
        ar.run()
