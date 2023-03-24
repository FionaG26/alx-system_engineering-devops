#This puppet mainfest installs flask from pip3
package { 'python3-pip':
  ensure => 'installed',
}

exec { 'install flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/usr/bin'],
  unless  => '/usr/bin/pip3 freeze | /bin/grep Flask | /bin/grep 2.1.0',
}
