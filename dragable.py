import os, os.path
from string import Template
import random

class MyTemplate(Template):
	delimiter = '$$$'

imgs = []
path = os.path.dirname(os.path.realpath(__file__))
valid_images = [".jpg",".gif",".png",".tga", ".svg"]
filelist = []
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    filelist.append(f)

random.shuffle(filelist)

fhandle = open("drag.html", 'w')
s = MyTemplate("""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Draggable</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
  <style>
 .div { width: 100%; height: 100%; padding: 0.5em; }
 img {
    max-width: 500px;
}
  </style>
  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  <script>
  $( function() {
    $( ".draggable" ).draggable();
  } );
  </script>
</head>
<body>
 
$$$div
</body>
</html>""")
div = ""
for fl in filelist:
	div = div + """<div>"""+ """<img class="ui-widget-content draggable"  src=\"""" + fl + """\"/>""" + """</div>"""


st = s.substitute(div = div)


fhandle.write(st)
fhandle.close()

