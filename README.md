# PHP to PYTHON


A python script to convert simple php code to python,
It just converts the basic syntax
It is the one i use in the conversion mpg25/Instagram-API in PHP to danleyb2/Instagram-API in PYTHON 

## Installation
```
    
    pip install convert2php
```

## usage
```
    $ python php2python.py -h
   
    usage: php2python.py [-h] -s SCRIPT [-o]
    
    PHP to PYTHON syntax converter.
    
    optional arguments:
      -h, --help            show this help message and exit
      -s SCRIPT, --script SCRIPT
                            Path to PHP script
      -o, --overwrite       Overwrite Python script if exists


```

```
    $ python php2python.py -s test_scripts/Caption.php
    
    Converting: test_scripts/Caption.php. Output file will be: test_scripts/Caption.py
    # Remove opening and closing <?php
    # convert $this-> to self.
    # convert :: to .
    # delete all }
    # delete namespace|require_once|include_once
    # convert protected $var to self.var = None then move into __init__
    # convert public|protected function to def
    # add `self` to function signatures
    # classes not children to extend `object`
    # convert $ to ''
    # convert ; to ''
    # convert new to ''
    Converted: test_scripts/Caption.php. to: test_scripts/Caption.py. { Go on, Proof Check :) }

    
```

```
    $ python php2python.py -s test_scripts/Caption.php
    Sorry, A python Script test_scripts/Caption.py already exist, use -o to overwrite.
    
```