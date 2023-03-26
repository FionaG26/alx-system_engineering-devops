#This puppet manifest configures private key ~/.ssh/school
 ensure  => present,
 content => "\
  Hostname <124704-web-01>
  Username <ubuntu>
  IP adress <54.90.3.58>
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
"
}

