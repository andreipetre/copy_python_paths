# -*- coding: utf-8 -*-

import sublime
from .python_path import PythonPathCommand


class CopyImportPathCommand(PythonPathCommand):

    def run(self, edit):
        python_path_items, class_items = self.pre_run(edit)
        python_path_items += class_items
        import_item = python_path_items.pop()
        python_path = "from " + '.'.join(python_path_items) + ' import ' + import_item
        sublime.set_clipboard(python_path)
        sublime.status_message('"%s" copied to clipboard' % python_path)
