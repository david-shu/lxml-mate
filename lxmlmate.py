# -*- coding: utf-8 -*-

'''
lxml mate.
'''


__ver_major__ = 0
__ver_minor__ = 5
__ver_patch__ = 2
__ver_sub__ = ""
__version__ = "%d.%d.%d%s" % (__ver_major__,__ver_minor__,__ver_patch__,__ver_sub__) 



from lxml import etree, objectify
import types



class ObjectifiedElementProxy( object ):
    u'''Proxy class for objectify.ObjectifiedElement instance which can be created by objectify.Element() or SubElement() or XML() or fromstring().

    main purpose is to intercept AttributeException when access a non-existent tag.
    
    How to access xml tag
    ---------------------
    .
        such as root.element.name

    []
        such as root['element']['name']

    hybrid
        such as root['element'].name

    note
        The tag can only be accessed by [] when it is one of the reserved keywords.
        Tag not in the xml tree can be accessed directly. A new tag will be created. No exceptions will be raised.


    How to access xml tag's attributes
    ----------------------------------
    []
        .attrib['style'], an exception will be raised when style dos'nt exist.
        .attrib['style'] = 'big'
    .get/set
        .attrib.get( 'style', None )
        .attrib.set( 'style', 'big' )


    How to access class attributes and methods
    ------------------------------------------
    .
        attributes are reserved keywords and they can only be accessed by this way, for example
        .pyval
        .text
        .insert etc.
        or they are considered xml tags rather than attributes.
        

    Reserved keywords
    -----------------
    The following keywords are used as methods or attributes' names.
    
    **pyval** : returns the python value carried by leaf tag. read-only.
    
    **text** : returns leaf tag's text content. read-only.
    
    **obj** : returns ObjectifiedElement object referenced by this class instance. read-only.
    
    **tag** : returns tag names. can be modified by . way such as \*.tag='newTagName'. readable and writable.
    
    **attrib** : returns tag attributes dict. readable and writeable.
    
    **parent** : returns parent node. read-only.
    
    **children** : returns all children's list. read-only.
    
    **len** : returns the number of children.
    
    **insert** : insert a child node at the specified position.
    
    **remove** : remove a child node at the specified position.
    
    **index** : returns the position of the specified object.
    
    **swap** : swap two nodes' position.

    Examples
    --------

    create a brand new xml:

    >>> p = ObjectifiedElmentProxy( rootag='Person' )
    >>> p.name = 'peter'
    >>> p.age = 13
    >>> print( p )
    <Person>
        <name>peter</name>
        <age>13</age>
    </Person>

    create from xml string:

    >>> p = ObjectifiedElementProxy( xmlStr="<Person><name>peter</name><age>13</age></Person>" )
    >>> print( p )
    <Person>
        <name>peter</name>
        <age>13</age>
    </Person>

    multiple levels examples:

    >>> r = ObjectifiedElementProxy()
    >>> r.person.name = 'jack' 
    >>> r.person.age = 10
    >>> print( r )
    <root>
        <person>
            <name>jack</name>
            <age>10</age>
        </person>
    </root>

    to insert child like '<person><name>peter</name><age>13</age></person>':
    
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
    
    >>> print( r.station[1].name.pyval )
    peter
    
    
    Notes
    -----
    xml attrib names and tag names are case insensitive.
    
    Nodes with text attribute are called leaf nodes. Theoretically, leaf nodes should not have children, but not required.

    '''

    def __init__( self, objectifiedElement=None, xmlFileName=None, xmlStr=None, rootag='root', attrib=None, nsmap=None, **kwargs ):
        u'''

        initialize from ObjectifiedElement or xml file or xml string or create a brand new.
        
        Arguments
        ---------
        objectifiedElement : ObjectifiedElement, optional
            an ObjectifiedElement object.
            
        xmlFileName : str, optional
            xml's filename.
            
        xmlStr : str, optional
            xml's content.
            
        rootag : str, optional
            create ObjectifiedElement instance which root tag's name is rootag.
            
        attrib, nsmap, kwargs : optional
            refer to objectify.Element()
            
        '''
        
        self._____o____ = None
        
        if objectifiedElement is not None:
            self._____o____ = objectifiedElement
            
        elif xmlFileName:
            self._____o____ = objectify.XML( xmlFileName )
            
        elif xmlStr:
            self._____o____ = objectify.fromstring( xmlStr )
            
        else:
            self._____o____ = objectify.Element( rootag, attrib=attrib, nsmap=nsmap, **kwargs )
       

    def __call__( self, tag, pyval=None, attrib=None, nsmap=None, **kwargs ):
        u'''Insert a new child node.

        insert a new child node to the end.

        Arguments
        ---------
        e : str
            the new tag to be inserted.
        pyval : legal python data type
            tag's python value.
        attrib,nsmap,kwargs : optional
            attribs for the new tag. see also objectify.Element() or SubElement().

        Returns
        -------
        ObjectifiedElementProxy instance

        See Also
        --------
        insert
        
        note the difference between the two methods' return values.

        Examples
        --------
        >>> p=ObjectifiedElementProxy( rootag='Person' )
        >>> p( 'name', pyval='jack' )('age', pyval=13 )
        >>> print( p )
        <Person>
        	<name py:pytype="str">jack</name>
        	<age py:pytype="int">13</age>
        </Person>        
        '''

        self.insert( tag, None, attrib, nsmap, **kwargs )
        
        self [ tag ][-1] = pyval
        
        return self
        
        
    def __getattr__( self, name ):
        
        if name == '_____o____':
            return object.__getattribute__(name)

        if hasattr( self._____o____, name ):
            e = getattr( self._____o____, name )

            if  name in ( 'tag','pyval','text', 'attrib' ) or isinstance( e, ( types.FunctionType, types.BuiltinFunctionType ) ):
                return e
            
        else:
            #if has no attr named name, created a new one.
            e = objectify.SubElement( self._____o____, name )

        
        return ObjectifiedElementProxy( e )


    def __setattr__( self, name, value ):

        if name == '_____o____':
            object.__setattr__( self, name, value )
            return

        setattr( self._____o____, name, value )


    def __delattr__( self, e ):
        self._____o____.__delattr__( e )


    def __len__( self ):
        u'''children's number'''
        
        return len( self.children )


    def __getitem__( self, name ):
        if isinstance( name, int ):
            return ObjectifiedElementProxy( self._____o____[name] )

        if isinstance( name, slice ):
            return [ ObjectifiedElementProxy( o ) for o in  self._____o____[name] ]

        if isinstance( name, str ):
            if name == '_____o____':
                return object.__getattribute__( name )
            
            o = self._____o____
            try:
                e = o.__getitem__( name )
            except:
                e = objectify.SubElement( self._____o____, name )
                
            return ObjectifiedElementProxy( e )
                
        raise Exception


    def __setitem__( self, e, v ):
        if e == '_____o____':
            object.__setitem__( self, e, v )
            return

        self._____o____[e] = v


    def __delitem__( self, e ):
        if isinstance( e, ObjectifiedElementProxy ):
            self._____o____.__delattr__( e.tag )
        else:
            self._____o____.__delattr__( e )

            
    def insert( self, e, i=None, attrib=None, nsmap=None, **kwargs ):
        u'''Insert a new child node.

        insert a new child node at the specified position.

        Arguments
        ---------
        e : str
            the new tag to be inserted.
        i : int, optional
            if i is integer : position of the new tag. else append to the end.
        attrib,nsmap,kwargs : optional
            attribs for the new tag. see also objectify.Element() or SubElement().
		
        '''
        
        v = objectify.SubElement( self._____o____, e, attrib=attrib, nsmap=nsmap, **kwargs )
        s = ObjectifiedElementProxy( v )

        if i is not None:
            self._____o____.insert( i, v )
    
        return s


    def swap( self, i, j ):
        u'''swap two child nodes' position.

        Arguments
        ---------
        i,j : int
            position of the child nodes to be swapped.
        '''
        
        self._____o____[i] = self._____o____[j]


    def remove( self, i ):
        u'''remove the child node.

        Arguments
        ---------
        i : int or ObjectifiedElement or ObjectifiedElementProxy or list
            position of the child node or Element which will be removed.
            
        '''
        
        if isinstance( i, list ):
            for k in i:
                self.remove( k )
                
        elif isinstance( i, int ):
            return self.obj.remove( self.children[i].obj )
        
        elif isinstance( i, objectify.ObjectifiedElement ):
            return self.obj.remove( i )
        
        elif isinstance( i, ObjectifiedElementProxy ):
            return self.obj.remove( i.obj )
        

    def index( self, o ):
        u'''return the position of o.

        Arguments
        ---------
        o : ObjectifiedElementProxy
            the ObjectifiedElementProxy instance to be positioned.

        Returns
        -------
        int
        '''

        return self._____o____.index( o.obj )


    def xpath( self, path ):
        u'''find elements list in accordance with path.

        Arguments
        ---------
        path : str
            please refer to lxml.objectify.ObjectifiedElement.xpath.

        Returns
        -------
        list
            a list of ObjectifiedElementProxy instance.


        Xpath grammer review
        --------------------

        ==========  ===========
        expression  description
        ==========  ===========   
        nodename    to select all children of the node name
        /           select from root node.    
        //          select from current node
        .           select the current code.   
        ..          select the parent node of the current node.
        @           select attrib.
        []          condition
        text()      tag text
        *           arbitrary node
        ==========  ============
        '''
        
        return [ ObjectifiedElementProxy(k) for k in self._____o____.xpath( path ) ]
        
        
    @property
    def children( self, **kwargs ):
        return [ ObjectifiedElementProxy( e ) for e in self._____o____.getchildren( **kwargs ) ]


    @property
    def parent( self ):
        return ObjectifiedElementProxy( self._____o____.getparent() )


    @property
    def root( self):
        parent = self._____o____.getparent()
        while parent:
            parent1 = parent.getparent()
            if parent1 is None:
                break
            parent = parent1
            
        return ObjectifiedElementProxy( parent )

    
    @property
    def obj( self ):
        return self._____o____


    @property
    def pyval( self ):
        if hasattr( self._____o____, 'pyval' ):
            if isinstance( self._____o____, objectify.StringElement ):
                return self._____o____.pyval.strip()

            return self._____o____.pyval


    def __nonzero__( self ):
        return self.is_empty()


    def is_empty( self ):
        u'''To determine whether a null node.

        no text \ no attribs \ no children.
        '''

        o = self._____o____

        if o.text and o.text.strip():
            return False

        n = 0
        for k in o.attrib:
            if k[0] != '{':
                n += 1

        if n > 0:
            return False

        n = 0
        for c in self.children:
            if not c.is_empty():
                n += 1

        if n > 0:
            return False

        return True


    def clean( self ):
        u'''clean all null nodes.
        '''

        for c in self.children:
            if c.is_empty():
                c.parent.obj.__delattr__( c.tag )
            else:
                c.clean()


    def tostring( self, encoding='utf-8', xml_declaration=True, standalone=None, with_comments=True,
                  pytype=False, xsi=True, xsi_nil=True, cleanup_namespaces=True, doctype=None,
                  with_tail=True, exclusive=False, inclusive_ns_prefixes=None ):

        #self.clean()
            
        objectify.deannotate( self._____o____, pytype=pytype, xsi=xsi, xsi_nil=xsi_nil, cleanup_namespaces=cleanup_namespaces )
        
        s = etree.tostring( self._____o____, encoding=encoding, pretty_print= True,
                            xml_declaration=xml_declaration, with_tail=with_tail,
                            standalone=standalone, doctype=doctype,
                            exclusive=exclusive, with_comments=with_comments,
                            inclusive_ns_prefixes=inclusive_ns_prefixes  )
        
        return s


    def __str__( self ):
        #s = self.tostring( pytype=True, xml_declaration=False , encoding='unicode' )
        s = self.tostring( pytype=True, xml_declaration=False ).decode()
        return s


    def dump( self, xmlFile, encoding='utf-8' ):
        '''save xml to file.
        
        Arguments
        ---------
        xmlFile : str
            xml's filename.
            
        '''
        
        f = open( xmlFile, 'w' )
        s = self.tostring( encoding=encoding ).decode()
        f.write( s )
        f.close()
        
        

if __name__ == '__main__':
    r = ObjectifiedElementProxy()
    r.person.name = 'jack' 
    r.person.age = 10
    r.insert( 'person' )('name','peter')('age',13)
    p = r('person').person[-1]
    p.name = 'david'
    p.age = 16
    print( r )

    print( r.tostring().decode() )
    
    print( r.person[1].name.pyval )
    
    r.dump( 'x.xml' )




