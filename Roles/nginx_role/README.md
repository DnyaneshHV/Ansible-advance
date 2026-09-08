Nginx Role Demo
===============

This role is a very simple example of how to install and start Nginx using Ansible.
The purpose is to show how a role can package tasks, variables, and handlers in a clean structure.

Requirements
------------

- Ansible installed on the control node
- Target machines running a Debian or Ubuntu-based system
- Root or sudo privileges on the managed nodes

Role Variables
--------------

The role uses default values defined in `defaults/main.yml`.
For this simple demo, the default behavior is to install the `nginx` package.

Example Playbook
----------------

```yaml
- name: Apply nginx role
  hosts: webservers
  become: true
  roles:
    - nginx_role
```

You can also see the demo playbook here:

- `demo.yml`

This role is useful for learning:

- task organization inside a role
- common directory layout
- using `become` for privileged actions
- role reuse across multiple playbooks
