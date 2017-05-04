# Sublime Build

> How to setup your Sublime Text 3 auto-build

1. Install [Package Control](https://packagecontrol.io/)
1. Install [SublimeOnSaveBuild](https://packagecontrol.io/packages/SublimeOnSaveBuild)
1. Create the new build:
    1. In Sublime, go to `Tools > Build System > New Build System`
    1. Set the content like this file
    1. Save it as `288.sublime-build`
    1. Go select `Tools > Build System > 288`
1. Customize the files which triggers the build on save
    1. In Sublime, go to `Preferences > Package Settings > SublimeOnSaveBuild > Settings - User`
    1. Set the content like this file
1. Go to `Preferences > Settings - User`
1. Add this line: `"show_panel_on_build": false`
1. Go to `Key Bindings > Settings - User`
1. Add those two lines:
    ```
    { "keys": ["f12"], "command": "show_panel", "args": {"panel": "output.exec"} },
    { "keys": ["ctrl+b"], "command": "build_and_show" }
    ```
1. Make sure to have the latest grunt files in your project
