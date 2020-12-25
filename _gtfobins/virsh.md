---
description: |
  This requires the user to be privileged enough to connect to the libvirt daemon, i.e. being in the `libvirt` group.

functions:
  command:
    - description: Execute a script stored on the libvirt server creating a VM using a `<script>` tag on the network interface definition.
      code: |
        SCRIPT=script_to_run
        TF=$(mktemp)
        cat > $TF << EOF
        <domain type='kvm'>
          <name>foo</name>
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
        virsh create $TF
        virsh destroy foo
  file-write:
    - description: Write a file by creating a storage pool on the target directory and uploading the file as a volume. If the target directory doesn't exist `pool-create-as` must be run with the `--build` option. Directories are created with permissions 711, and files with permissions 600. These can be modified using `pool-create|vol-create` with an XML definition file instead of using `pool-create-as|vol-create-as`. Sample XML files can be obtained with `pool-dumpxml|vol-dumpxml`.
      code: |
        LPATH=file_to_read
        RPATH=file_to_save
        virsh pool-create-as $(dirname $RPATH|tr / _) dir --target $(dirname $RPATH)
        virsh vol-create-as $(dirname $RPATH|tr / _) $(basename $RPATH) 0
        virsh vol-upload $RPATH $LPATH
        virsh pool-destroy $(dirname $RPATH|tr / _)
  file-read:
    - description: Read a file by creating a storage pool on the target directory and downloading the file as a volume.
      code: |
        RPATH=file_to_get
        LPATH=file_to_save
        virsh pool-create-as $(dirname $RPATH|tr / _) dir --target $(dirname $RPATH)
        virsh vol-download $RPATH $LPATH
        virsh pool-destroy $(dirname $RPATH|tr / _)
---
