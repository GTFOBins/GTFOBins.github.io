---
functions:
  sudo:
    - code: |
        SCRIPT=script_to_run
        TF=$(mktemp)
        cat > $TF << EOF
        <domain type='kvm'>
          <name>x</name>
          <os>
            <type arch='x86_64'>hvm</type>
          </os>
          <memory unit='KiB'>1</memory>
          <devices>
            <interface type='ethernet'>
              <script path='$SCRIPT'/>
            </interface>
          </devices>
        </domain>
        EOF
        sudo virsh -c qemu:///system create $TF
        virsh -c qemu:///system destroy x
  file-write:
    - description: This requires the user to be in the `libvirt` group. If the target directory doesn't exist `pool-create-as` must be run with the `--build` option. The destination file permissions can be tuned in the XML file. 
      code: |
        LFILE_DIR=/root
        LFILE_NAME=file_to_write

        echo 'data' > data_to_write

        TF=$(mktemp)
        cat > $TF <<EOF
        <volume type='file'>
          <name>y</name>
          <key>$LFILE_DIR/$LFILE_NAME</key>
          <source>
          </source>
          <capacity unit='bytes'>5</capacity>
          <allocation unit='bytes'>4096</allocation>
          <physical unit='bytes'>5</physical>
          <target>
            <path>$LFILE_DIR/$LFILE_NAME</path>
            <format type='raw'/>
            <permissions>
              <mode>0600</mode>
              <owner>0</owner>
              <group>0</group>
            </permissions>
          </target>
        </volume>
        EOF

        virsh -c qemu:///system pool-create-as x dir --target $LFILE_DIR
        virsh -c qemu:///system vol-create --pool x --file $TF
        virsh -c qemu:///system vol-upload --pool x $LFILE_DIR/$LFILE_NAME data_to_write
        virsh -c qemu:///system pool-destroy x
  file-read:
    - description: This requires the user to be in the `libvirt` group.
      code: |
        LFILE_DIR=/root
        LFILE_NAME=file_to_read

        SPATH=file_to_save

        virsh -c qemu:///system pool-create-as x dir --target $LFILE_DIR
        virsh -c qemu:///system vol-download --pool x $LFILE_NAME $SPATH
        virsh -c qemu:///system pool-destroy x
---
