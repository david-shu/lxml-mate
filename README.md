
What is lxml-mate?
==================

The simplest XML-Object mapper for Python powered by lxml. It’s powerful.

No class definitions are needed to define structure of your XML document.

You can create a brand new xml, or create from string, xml document and handle it in very pythonic way.

See source code for more documents.



Features
========
Intercept AttributeError when access a non-existent tag in order to access more easily.

For exmaple:

	>>> s = '''
	...	<root>
	...		<person height='180cm'>
	...			<name>jack</name>
	...			<age>18</age>
	...		</person>
	...		<person>
	...			<name>peter</name>
	...		</person>
	...	</root>
	>>>	'''
	
	when we access the second person's age, lxml.objectify.ObjectifiedElement will raise 
	an AttributeError. lxml-mate will create an null node instead of raising an exception.
	
	*lxml*
	
	>>> r = objectify.fromstring( s )
	>>> ages = [ ( p.name, p.age ) for p in r.person ] #AttributeError be raised.
	>>> r.person[0].else.mother = 'jerry' #AttributeError be raised.
	
	*lxml-mate*
	
	>>> r = ObjectifiedElementProxy( xmlstr = s )
	>>> ages = [ ( p.name.pyval, p.age.pyval ) for p in r.person[:] ] #dose work
	>>> r.person[0].else.mother = 'jerry' #doses work


Usage
=====

#. create

	to create a new xml like::

	<root>
		<person height='180cm'>
			<name>jack</name>
			<age>18</age>
		</person>
	</root>
	
	*lxml*

	>>> from lxml import objectify, etree
	>>> r = objectify.Element('root')
	>>> person = objectify.SubElement( r, 'person', attrib={'height':'180cm'} )
	>>> name = objectify.SubElement( person, 'name' )
	>>> person.name = 'jack'
	>>> age = objectify.SubElement( person, 'age' )
	>>> person.age = 18
	
	or use E-factory
	
	>>> E = objectify.E
	>>> E.root( E.person( E.name('jack'), E.age(18), height='180cm' ) )
	
	*lxml-mate*

	>>> from lxmlmate import ObjectifiedElementProxy
	>>> rm = ObjectifiedElementProxy( rootag='root' )
	>>> rm.append( E.person( E.name('jack'), E.age(18), height='180cm' ) )
	
	or
	
	>>> rm = ObjectifiedElementProxy( objectifiedElement = E.root( E.person( E.name('jack'), E.age(18), height='180cm', height='180cm' ) ) )
	
	or
	
	>>> rm = ObjectifiedElementProxy( rootag='root' )
	>>> rm.person.name = 'jack'
	>>> rm.person.age = 18
	>>> rm.person.attrib[ 'height' ] = '180cm'
	
	
#. append

	to append xml snippet like:
	
	<person>
		<name>peter</name>
		<age>45</age>
	</person>
	<person>
		<name>joe</name>
		<age>25</age>
	</person>
	
	*lxml*
	
	>>> r.append( E.person( E.name( 'peter' ), E.age( 45 ) ),
	...           E.person( E.name( 'joe' ), E.age( 25 ) )
	...          )
	>>>
	
	*lxml-mate*
		
	>>> rm.append( E.person( E.name( 'peter' ), E.age( 45 ) ),
	...            E.person( E.name( 'joe' ), E.age( 25 ) )
	...           )
	>>>

	or
	 
	>>> rm.insert( 'person', i=None )( 'name', 'peter' )( 'age', 45 )
	>>> rm.insert( 'person', i=None )( 'name', 'joe' )( 'age', 25 )

	
#. select
	 
	*lxml*
	
	to select the last person ( named joe )
	
	>>> r.person[-1] #return an ObjectifiedElement instance.
	
	to find persons named joe::

	>>> r.xpath( '//person[name="joe"]' )  # return ObjectifiedElement instances list

	*lxml-mate*
	
	>>> rm.person[-1]  #return an ObjectifiedElementProxy instance.
	>>> rm.xpath( '//person[name="joe"]' )  # return ObjectifiedElementProxy objects list
	
		
#. remove

	to remove all persons named joe:
	
	*lxml*
	
	>>> p = r.xpath( '//person[name="joe"]' )
	>>> for k in p: r.remove( k )
	
	*lxml-mate*
	
	>>> pm = rm.xpath( '//person[name="joe"]' )
	>>> rm.remove( pm )
	
	or 
	
	>>> rm.remove( [ p for p in rm.person[:] if p.name.pyval == 'joe' ] )
	
	to remove the first person: 
	
	*lxml
	
	>>> p = r.person[0]
	>>> r.remove( p )
	
	*lxml-mate
	>>> rm.remove( 0 )  
	
	
#. dump to file

	*lxml*
	
	>>> f = open( 'person.xml', 'w' )
	>>> s = etree.tostring( r )
	>>> f.write( s )
	>>> f.close()
	
	*lxml-mate*
	
	>>> rm.dump( 'person.xml' )
	
	
#. load from file

	*lxml*
	
	>>> r = objectify.XML( 'person.xml' )
	
	*lxml-mate*
	
	>>> rm = ObjectifiedElementProxy( xmlFile = 'person.xml' ) 


#. create a brand new xml
	
	*lxml*
	
	>>> r = objectify.Element('root')
	
	*lxml-mate*
	
	>>> rm = ObjectifiedElementProxy( rootag='root' )

    
#. Else

	to access a tag:
	
	>>> rm.person[0]
	>>> rm[ 'person' ][0]
	>>> rm.person
	>>> rm.person[ 'name' ]
	
	to modify a tag's value:
	
	>>> rm.person.age = 23
	
	to get a tag's pyval:
	
	>>> rm.person.age.pyval

	to modify a tag's attrib:
    
        >>> rm.person[0].attrib['height'] = "170cm" 
    
	to modify tag:
    
        >>> rm.person[-1].tag = 'people'
    
        to clean empty node ( no attributes & no children ):
    
        >>> rm.clean()
    
        You can use lxml.objectify.ObjectifiedElement's methods directly like this:
    
        >>> rm.addattr( 'kkk','vvv' )
    


Dependencies
============
lxml https://github.com/lxml/lxml/



Installion
==========
	>>> pip install lxml-mate
	
	





