#This puppet manifest configures private key ~/.ssh/school
class { 'ssh':
  client::ensure            => 'running',
  client::password_auth     => 'no',
  client::private_key       => '~/.ssh/school',
}
 
