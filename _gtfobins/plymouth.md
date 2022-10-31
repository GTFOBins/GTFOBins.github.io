---
description: |
  Plymouth is a bootsplash screen providing flicker free boot splash animations with native resolution. Plymouth works with
  a daemon (`plymouthd`) running in the background displaying the actual graphic to the TTY and the `plymouth` command is
  used to interact with the daemon. The `plymouth` command can be used to request the daemon to act, such as display splash
  screen, request user input or similar.
functions:
  sudo:
    - description: |
        To achieve code execution, it is required that `plymouthd` is already running as root or can be started as root (with sudo
        or equivalent). It is also required to have tty access to input characters such as keyboard access to the machine. It is
        usually best to save the following code snipet to a script (e.g. `priv-esc.sh`) and execute that as the first command
        will take over the TTY and you will loose terminal access (if executed from the same TTY) until `hide-splash`.

        `show-splash` is used to take control over the TTY and display the splash screen. `pause-progress` is used to prevent
        plymouth from automatically quiting in some cases as we are already booted. `ask-for-password` will ask the user for a
        text password (usually to decrypt a LUKS disk encryption). We can tell plymouth to send this input to any program, such
        as `/bin/sh` to execute whatever input we gave. Then run `hide-splash` to hide the splash screen and return to normal.
      code: |
        sudo plymouth show-splash
        sudo plymouth pause-progress
        sudo plymouth ask-for-password --prompt='Execute root command:' --command=/bin/sh
        sudo plymouth hide-splash
---
