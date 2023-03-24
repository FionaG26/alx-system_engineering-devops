# This puppet manifest creates a file names/tmp/school
file { '/tmp/school':
  content => "I love Puppet\n",
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  }
