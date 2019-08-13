
from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
#DOMTree = xml.dom.minidom.parse("C:\\Users\\Jessicah Princess\\Desktop\\course.xml")
DOMTree = xml.dom.minidom.parse("//Users//keshavkummari//6am_python_nit_3rdJuly2019//xml//movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print ("Root element : %s" % collection.getAttribute("shelf"))

# Get all the movies in the collection
movies = collection.getElementsByTagName("title")

# Print detail of each movie.
for movie in movies:
   print ("********")
   if movie.hasAttribute("title"):
      print ("Title: %s" % movie.getAttribute("title"))

   type = movie.getElementsByTagName('type')[0]
   print ("Type: %s" % type.childNodes[0].data)
   format = movie.getElementsByTagName('format')[0]
   print ("Format: %s" % format.childNodes[0].data)
   rating = movie.getElementsByTagName('rating')[0]
   print ("Rating: %s" % rating.childNodes[0].data)
   description = movie.getElementsByTagName('description')[0]
   print ("Description: %s" % description.childNodes[0].data)