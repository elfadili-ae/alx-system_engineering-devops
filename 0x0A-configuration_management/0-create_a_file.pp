file { '/tmp/school':
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  content => 'I love Puppet'
}
