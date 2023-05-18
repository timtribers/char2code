import sublime
import sublime_plugin


class ShowCodepointCommand(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        sel = view.sel()

        if len(sel) == 1 and not sel[0].empty():
            region = sel[0]
            selected_text = view.substr(region)

            if len(selected_text) == 1:
                codepoint = ord(selected_text)
                status_text = selected_text + "<" + hex(codepoint) + ">"
                view.set_status("codepoint", status_text)
            else:
                view.erase_status("codepoint")
        else:
            view.erase_status("codepoint")
