import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
module_name = '{{cookiecutter.project_slug}}'

if not module_name:
    print('ERROR: The project slug (%s) is not a valid Python module name.' % module_name)
    sys.exit(1)

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python module name.' % module_name)
    sys.exit(1)
