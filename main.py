import os
import subprocess
import rumps

class FinderTerminalOpenerApp(rumps.App):
    def __init__(self):
        super(FinderTerminalOpenerApp, self).__init__("Finder Terminal Opener", icon="icon.jpg")
        self.menu = [
            "open the terminal",
        ]

    @rumps.clicked("open the terminal")
    def open_terminal_here(self, sender):
        current_folder = self.get_current_folder()
        if current_folder:
            subprocess.run(["open", "-a", "Terminal", current_folder])

    def get_current_folder(self):
        try:
            folder_path = subprocess.check_output([
                "osascript",
                "-e", 'tell application "Finder" to get POSIX path of (target of front window as alias)'
            ]).decode("utf-8").strip()
            return folder_path
        except subprocess.CalledProcessError:
            rumps.alert("Error", "Could not determine current folder.")
            return None

if __name__ == "__main__":
    app = FinderTerminalOpenerApp()
    app.run()
