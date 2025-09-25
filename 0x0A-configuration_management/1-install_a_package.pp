#Using Puppet, install flask from pip3.

package { 'python3-pip3':
  ensure => installed,
}


package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => package['python3-pip3'],
}
