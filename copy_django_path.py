# -*- coding: utf-8 -*-

import sublime
from .python_path import PythonPathCommand


class CopyDjangoPathCommand(PythonPathCommand):

    def run(self, edit):
        python_path_items, class_items = self.pre_run(edit)
        python_path = '.'.join(python_path_items)
        if class_items:
            python_path += ":" + '.'.join(class_items)
        sublime.set_clipboard(python_path)
        sublime.status_message('"%s" copied to clipboard' % python_path)
