ansible-common
==============

Common ansible scripts to use with Django-projects


Run with:

./ansible/parse_current_settings.py development
ansible-playbook -i inventory.ansible ./ansible/deployment.yaml -l development
ansible-playbook -i inventory.ansible ./ansible/django_routines.yaml -l development

where inventory.ansible looks like:

[development]

somehost.cloudapp.net    ansible_ssh_user=azureuser  settings_file=development

Don't forget to setup authentication with ssh-copy-id!
