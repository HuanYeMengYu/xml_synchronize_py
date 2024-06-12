from lxml import etree

page = etree.Element( "root" )
doc = etree.ElementTree( page )

headElt = etree.SubElement ( page, 'head' )
bodyElt = etree.SubElement ( page, 'body' )
bodyElt.text = '222'
newComment = etree.Comment ( "test comment1" )
bodyElt.append ( newComment )

print( headElt.getparent().index(headElt) )
print( bodyElt.getparent().index(bodyElt) )

new0 = etree.Element( 'new0' )
new0.text = "000"
new1 = etree.Element( 'new1' )
new1.text = "111"
new2 = etree.Element( 'new2' )
new2.text = "222"
headElt.insert( 0, new0 )
headElt.insert( 1, new1 )
headElt.insert( 2, new2 )

doc.write ( 'learn.xml' , pretty_print=True )
