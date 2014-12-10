ansible-common
==============

Common ansible scripts to use with Django-projects


Run with:

./ansible/deploy_server.sh development app

where inventory.ansible looks like:

[development]

somehost.com ansible_ssh_host=somehost.cloudapp.net    ansible_ssh_user=azureuser  settings_file=development

Don't forget to setup authentication with ssh-copy-id!
