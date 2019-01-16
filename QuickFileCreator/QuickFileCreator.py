import sublime
import sublime_plugin
import os
import re

class QuickCreateFileCreatorBase(sublime_plugin.WindowCommand):
    relative_paths = []
    full_torelative_paths = {}
    

    def doCommand(self):
        self.construct_excluded_pattern()
        self.build_relative_paths()
        if len(self.relative_paths) == 1:
            self.selected_dir = self.relative_paths[0]
            self.selected_dir = self.full_torelative_paths[self.selected_dir]
            self.window.show_input_panel(self.INPUT_PANEL_CAPTION, '', self.file_name_input, None, None)
        elif len(self.relative_paths) > 1:
            self.move_current_directory_to_top()
            self.window.show_quick_panel(self.relative_paths, self.dir_selected)
        else:
            view = self.window.active_view()
            self.selected_dir = os.path.dirname(view.file_name())
            self.window.show_input_panel(self.INPUT_PANEL_CAPTION, '', self.file_name_input, None, None)
