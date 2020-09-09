---
functions:
  shell:
      code: |
	view whatever.txt
	:!sh
  command:
      code: |
	view whatever.txt
        :!whoami
  file-read:
      code: |
	LFILE=file_to_read
        view $LFILE
  file-write:
      code: |
	LFILE=file_to_write
	view $LFILE
	i
	This is a test!
	:wq!
  sudo:
      code: |
	sudo view whatever.txt
	:!whoami
  limited-suid:
      code: |
	LFILE=file_to_edit
	view $LFILE
	i
	This is testing data!
	:wq!
---
