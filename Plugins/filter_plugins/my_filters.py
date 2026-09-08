# Custom filter plugin for Ansible demo
# Place this file inside a folder named filter_plugins.
# Ansible automatically loads filter functions from this folder.

class FilterModule(object):
    def filters(self):
        return {
            'reverse_text': self.reverse_text,
            'add_prefix': self.add_prefix,
        }

    def reverse_text(self, value):
        # Reverse a string example: 'nginx' -> 'xignn'
        return value[::-1]

    def add_prefix(self, value, prefix):
        # Add a prefix to a value, for example 'nginx' -> 'service:nginx'
        return prefix + str(value)
