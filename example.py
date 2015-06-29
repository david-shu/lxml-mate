

from lxmlmate import ObjectifiedElementProxy


	
print("#To create a brand new xml:")

p = ObjectifiedElementProxy( rootag='Person' )
p.name = 'peter'
p.age = 13
print( p )

print('''
##<Person>
##    <name>peter</name>
##    <age>13</age>
##</Person>
''')

print('===================')

print( p.name )
print('''
##<name>peter</name>
''')

print('===================')

#To retrieve peter's name and age:

peter = p.name.pyval
age = p.age.pyval


print('#To create from xml string:')
p = ObjectifiedElementProxy( xmlStr="<Person><name>peter</name><age>13</age></Person>" )
print( p )
print('''
##<Person>
##    <name>peter</name>
##    <age>13</age>
##</Person>
''')


#Multiple levels' example:
r = ObjectifiedElementProxy()
r.person.name = 'jack' 
r.person.age = 10

print('===================')

print('''#To insert descedants like '<person><name>peter</name><age>13</age></person>':''')
r.insert( 'person' )('name','peter')('age',13)
p = r('person').person[-1]
p.name = 'david'
p.age = 16
print( r )
print('''
##<root>
##    <person>
##        <name>jack</name>
##        <age>10</age>
##    </person>
##    <person>
##        <name>peter</name>
##        <age>13</age>
##    </person>
##    <person>
##        <name>david</name>
##        <age>16</age>
##    </person>
##</root>
''')

print('===================')

print( r.person[1].name.pyval )
print('##peter')


##To retrieve the last person:
r.person[-1]


##To insert a new tag with attrib:
r.insert( 'person', attrib={ 'height' : "185cm" } )
    
##To modify a tag's attrib:
r.person[0].attrib['height'] = "170cm" 

##You can use lxml.ObjectifiedElement's methods directly like this:
r.addattr( 'kkk','vvv' )

##To modify tag:
r.person[-1].tag = 'person_new'

print('===================')

print( r.person[-1] )
print('''
##<person_new> 	    
##    <name>david</name>
##    <age>16</age>
##</person_new>
''')

print('===================')
print('#To insert a new tag with attrib:')
r.insert( 'person', attrib={ 'height':'185cm'} )("name","joe")
print( r.person[-1] )
print('''
##<person height="185cm">
##    <name>joe</name>
##</person>    
''')

##To dump to xml document:
r.dump( 'person.xml' ) 
