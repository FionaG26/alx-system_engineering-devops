#This puppet manifest configures private key ~/.ssh/school
file { '/alx-system_engineering-devops/0x0B-ssh/100-puppet_ssh_config.pp':
  ensure  => present,
  mode    => '0600',
  content => "
    Host 124704-web-01
      Hostname 54.90.3.58
      User ubuntu
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
