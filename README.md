# Sublime Build

> How to setup your Sublime Text 3 auto-build, that uploads the file that was saved.

1. Install [Package Control](https://packagecontrol.io/)
1. Install [SublimeOnSaveBuild](https://packagecontrol.io/packages/SublimeOnSaveBuild)
1. Create the new build:
    1. In Sublime, go to `Tools > Build System > New Build System`
    1. Set the content like [this file](https://github.com/DeuxHuitHuit/sublime-build/blob/master/288.sublime-build)
    1. Save it as `288.sublime-build`
    1. Go select `Tools > Build System > 288`
1. Create a new build and show plugin
    1. In Sublime, go to `Tools > New Plugin` or (`Tools > Developer > New Plugin`)
    1. Set the content like [this file](https://github.com/DeuxHuitHuit/sublime-build/blob/master/BuildAndShow.py)
    1. Save it as `BuildAndShow.py`
1. Customize the files which triggers the build on save
    1. In Sublime, go to `Preferences > Package Settings > SublimeOnSaveBuild > Settings - User`
    1. Set the content like [this file](https://github.com/DeuxHuitHuit/sublime-build/blob/master/SublimeOnSaveBuild.sublime-settings)
    1. Save it
1. Go to `Preferences > Settings - User`
    1. Add this line: `"show_panel_on_build": false`
1. Go to `Preferences > Key Bindings - User`
1. Add those two lines:
    1. On Windows/Linux
    ```
    { "keys": ["f12"], "command": "show_panel", "args": {"panel": "output.exec"} },
    { "keys": ["ctrl+b"], "command": "build_and_show" }
    ```
    1. On macOS
    ```
    { "keys": ["ctrl+super+b"], "command": "show_panel", "args": {"panel": "output.exec"} },
    { "keys": ["super+b"], "command": "build_and_show" }
    ```
1. Make sure to have the latest [ftps_deploy grunt task in your project](https://github.com/DeuxHuitHuit/symphony-2-template/blob/58b6ae0befba795d23c72a04ccf26d61c4f42401/workspace/assets/tasks/ftps_deploy.js#L72) plus [this](https://github.com/DeuxHuitHuit/symphony-2-template/blob/58b6ae0befba795d23c72a04ccf26d61c4f42401/workspace/assets/tasks/ftps_deploy.js#L46-L54) and [this](https://github.com/DeuxHuitHuit/symphony-2-template/blob/0150e0a92cad7c6330374f7f3e96b0d38da8440f/workspace/assets/Gruntfile.js#L198).
