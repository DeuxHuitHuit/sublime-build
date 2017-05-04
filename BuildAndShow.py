import sublime
import sublime_plugin


class BuildAndShow(sublime_plugin.WindowCommand):
	def run(self):
		self.window.run_command("build")
		self.window.run_command("show_panel", {"panel": "output.exec"})
