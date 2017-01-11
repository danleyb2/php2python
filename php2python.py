import argparse


def python_script_name(php_script):
    return php_script.split('.php')[0]+'.py'


def convert2python(php_script,py_script):
    #todo convert $this-> to self.
    #todo convert :: to .
    #todo convert public|protected function to def
    #todo delete all ;|}
    #todo delete namespace|require_once|include_once
    #todo add `self` to function signatures
    #todo classes not children to extend `object`

    pass


def main():
    parser = argparse.ArgumentParser(description='PHP to PYTHON syntax converter.')
    parser.add_argument('-s', '--script', help='Path to PHP script', required=True)

    args = parser.parse_args()
    php_script = args.script
    py_script = python_script_name(php_script)

    print("Converting: %s. Output file will be: %s" % (php_script, py_script))

    convert2python(php_script,py_script)


if __name__ == '__main__':
    main()
