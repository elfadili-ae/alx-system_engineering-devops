# replace phpp with php in wp settings
exec { 'fix wp settings':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin', '/usr/bin/'],
}
