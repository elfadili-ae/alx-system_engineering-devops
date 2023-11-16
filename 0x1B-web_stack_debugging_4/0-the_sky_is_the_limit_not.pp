# change limit of the default file for nginx

exec {'fix the limit':
  command => "sed -i 's/15/unlimited/' /etc/default/nginx",
  path    => ['/bin/', '/usr/bin/']
}

-> exec {'restart nginx':
  command => 'nginx restart',
  path    => '/etc/init.d',
}
