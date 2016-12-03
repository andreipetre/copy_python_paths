# -*- coding: utf-8 -*-

import os

import sublime_plugin


class PythonPathCommand(sublime_plugin.TextCommand):

    def pre_run(self, edit):
        python_path_items = []
        class_items = []
        head, tail = os.path.split(self.view.file_name())

        module = tail.rsplit('.', 1)[0]
        if module != '__init__':
            python_path_items.append(module)

        head, tail = os.path.split(head)

        while tail:
            if '__init__.py' in os.listdir(os.path.join(head, tail)):
                python_path_items.insert(0, tail)
            else:
                break

            head, tail = os.path.split(head)

        caret_point = self.view.sel()[0].begin()
        if 'entity.name.class.python' in self.view.scope_name(caret_point):
            class_items.append(self.view.substr(self.view.word(caret_point)))

        if 'entity.name.function.python' in self.view.scope_name(caret_point):
            method_name = self.view.substr(self.view.word(caret_point))
            if self.view.indentation_level(caret_point) > 0:
                regions = self.view.find_by_selector('entity.name.class.python')
                possible_class_point = 0
                for region in regions:
                    if region.b < caret_point:
                        possible_class_point = region.a
                    else:
                        break

                class_name = self.view.substr(self.view.word(possible_class_point))

                class_items.append(class_name)

            class_items.append(method_name)
        return python_path_items, class_items

    def is_enabled(self):
        matcher = 'source.python'
        return self.view.match_selector(self.view.sel()[0].begin(), matcher)
