#! /usr/bin/python2.7

import argparse
import fileinput
import os
import re
import shutil

declarations = []


def python_script_name(php_script):
    return php_script.split('.php')[0] + '.py'


def replace(f, o, n):
    php_file = fileinput.FileInput(f, inplace=True)
    for line in php_file:
        # sys.stdout.write('new text')
        print(line.replace(o, n)),

    php_file.close()


def remove_lines_bound(f, start, end=None):
    php_file = fileinput.FileInput(f, inplace=True)
    end = '[' + end + ']$' if end else ''
    for line in php_file:
        reg = '.*' + start + '.*' + end
        if re.match(reg, line):
            continue

        print(line),

    php_file.close()


def add_self_to_functions(f):
    process_class_declarations(f)

    php_file = fileinput.FileInput(f, inplace=True)
    for line in php_file:
        reg = r'(.*)(public|protected) function (.*)\((.*)\)$'
        match = re.match(reg, line)
        if match:

            groups = match.groups()
            function_indent = groups[0]
            function_name = '__init__' if groups[2] == '__construct' else groups[2]
            function_params = '(self,' + groups[3] + '):' if groups[3] else '(self):'

            function = function_indent + 'def ' + function_name + function_params
            print function

            if groups[2] == '__construct':
                for declaration in declarations:
                    print declaration
                print
                # todo case of no constructor
        else:
            print(line),

    php_file.close()


def process_class_declarations(f):
    php_file = fileinput.FileInput(f, inplace=True)
    for line in php_file:
        reg = r'(.*)(public|protected) \$(.*);$'
        match = re.match(reg, line)
        if match:

            groups = match.groups()
            declaration_indent = groups[0]
            declaration = (declaration_indent * 2) + 'self.' + groups[2] + ' = None'

            declarations.append(declaration)
            continue
        else:
            print(line),

    php_file.close()


def class_definition(f):
    php_file = fileinput.FileInput(f, inplace=True)
    for line in php_file:
        reg = r'class (.*)'
        match = re.match(reg, line)
        if match:
            groups = match.groups()
            class_name = groups[0]
            class_def = 'class ' + class_name + '(object):'

            print class_def

        else:
            print(line),

    php_file.close()


def convert2python(php_script, py_script, overwrite):
    if not os.path.exists(php_script):
        raise Exception("Could not locate PHP script: %s" % php_script)

    if os.path.exists(py_script):
        if not overwrite:
            print("Sorry, A python Script %s already exist, use -o to overwrite." % py_script)
            return

    print("Converting: %s. Output file will be: %s" % (php_script, py_script))
    shutil.copyfile(php_script, py_script)

    print '# Remove opening and closing <?php'
    replace(py_script, '<?php', '')

    print '# convert $this-> to self.'
    replace(py_script, '$this->', 'self.')

    print '# convert :: to .'
    replace(py_script, '::', '')

    print '# delete all }'
    print '# delete namespace|require_once|include_once'
    remove_lines_bound(py_script, "namespace", ";")
    remove_lines_bound(py_script, "require_once", ";")
    remove_lines_bound(py_script, "include_once", ";")
    remove_lines_bound(py_script, "\{", "")
    remove_lines_bound(py_script, "\}", "")

    print '# convert protected $var to self.var = None then move into __init__'
    print '# convert public|protected function to def'
    print '# add `self` to function signatures'
    add_self_to_functions(py_script)

    print '# classes not children to extend `object`'
    class_definition(py_script)

    print '# convert $ to \'\''
    replace(py_script, '$', '')

    print '# convert ; to \'\''
    replace(py_script, ';', '')

    print '# convert new to \'\''
    replace(py_script, 'new ', '')
    print("Converted: %s. to: %s. { Go on, Proof Check :) }" % (php_script, py_script))


def main():
    parser = argparse.ArgumentParser(description='PHP to PYTHON syntax converter.')
    parser.add_argument('-s', '--script', help='Path to PHP script', required=True)
    parser.add_argument('-o', '--overwrite', help='Overwrite Python script if exists', action='store_true')

    args = parser.parse_args()
    php_script = args.script
    py_script = python_script_name(php_script)

    convert2python(php_script, py_script, args.overwrite)


if __name__ == '__main__':
    main()
