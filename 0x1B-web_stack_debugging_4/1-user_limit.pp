# Fix limits for the user holberton

exec {'change limits':
  command => "sed -i 's/nofile [0-9]\+$/nofile unlimited/g' /etc/security/limits.conf",
  path    => ['/bin/','/usr/bin/']
}
