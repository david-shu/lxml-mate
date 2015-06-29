
What is lxml-mate?
=================

The simplest Object-XML mapper for Python, yet it's powerful.

No class definitions are needed to define the expected structure of your XML document.

You can handle xml in very pythonic way.

See source code for more documents.


Example
-------

	Import lxmlmate first:

	>>> from lxmlmate import ObjectifiedElementProxy
	
	To create a brand new xml:

    >>> p = ObjectifiedElmentProxy( rootag='Person' )
    >>> p.name = 'peter'
    >>> p.age = 13
    >>> print( p )
    <Person>
        <name>peter</name>
        <age>13</age>
    </Person>
    
    >>> print( p.name )
    <name>peter</name>
    
    To retrieve peter's name and age:
    
    >>> peter = p.name.pyval
    >>> age = p.age.pyval

    To create from xml string:

    >>> p = ObjectifiedElementProxy( xmlStr="<Person><name>peter</name><age>13</age></Person>" )
    >>> print( p )
    <Person>
        <name>peter</name>
        <age>13</age>
    </Person>

    Multiple levels' example:

    >>> r = ObjectifiedElementProxy()
    >>> r.person.name = 'jack' 
    >>> r.person.age = 10

    To insert descedants like '<person><name>peter</name><age>13</age></person>':
    
    >>> r.insert( 'person' )('name','peter')('age',13)

    >>> p = r('person').person[-1]
    >>> p.name = 'david'
    >>> p.age = 16
    >>> print( r )
    <root>
        <person>
            <name>jack</name>
            <age>10</age>
        </person>
        <person>
            <name>peter</name>
            <age>13</age>
        </person>
        <person>
            <name>david</name>
            <age>16</age>
        </person>
    </root>
    
    >>> print( r.person[1].name.pyval )
    peter
    
    To retrieve the last person:
    
    >>> r.person[-1]
    
    To insert a new tag with attrib:
    
    >>> r.insert( 'person', attrib={ 'height' : "185cm" } )
	
	To modify a tag's attrib:
	
	>>> r.person[0].attrib['height'] = "170cm" 
    
	You can use lxml.ObjectifiedElement's methods directly like this:
	
	>>> r.addattr( 'kkk','vvv' )
	
	To modify tag:
	
	>>> r.person[-1].tag = 'person_new'
	>>> print r.person[-1]
	<person_new> 	    
        <name>david</name>
        <age>16</age>
	</person_new>
	
	To modify tag's value:
	
	>>> r.person[-1].age = 20
	
    To clean empty node:
    
    >>> r.clean()
    
	To dump to xml document:
	
	>>> r.dump( 'person.xml' ) 
    

Dependencies
------------
lxml https://github.com/lxml/lxml/

Installion
----------
	>>> pip install lxml-lite






