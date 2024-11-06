---
functions:
  reverse-shell:
    - description: |
        Create a tunnel to `vscode.dev`, then complete Github device registration and browse `https://vscode.dev/tunnel/my-tunnel-name`.
        
        Select `View \ Terminal` to spawn a shell on remote.
      code: code tunnel -name 'my-tunnel-name'
  file-upload:
    - description: |
        Create a tunnel to `vscode.dev`, then complete Github device registration and browse `https://vscode.dev/tunnel/my-tunnel-name`.
        
        In the `Explorer` tab, select `Open Folder`, then right-click on the folder and select `Upload`.
        
        Select file from the local file browser.
      code: code tunnel -name 'my-tunnel-name'
  file-download:
    - description: |
        Create a tunnel to `vscode.dev`, then complete Github device registration and browse `https://vscode.dev/tunnel/my-tunnel-name`.
        
        In the `Explorer` tab, select `Open Folder`, then select a file, right-click and select `Download`.
      code: code tunnel -name 'my-tunnel-name'
---
