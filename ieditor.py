import console, editor

def main():
	name = console.input_alert("Name", 'Choose a name for your new file with an extension (e.g. .txt | .html | .py | .md)')
	firstline = {
		'md': "# " + name + "\n\n",
		'html': ("<!--iEditor by GoDzM4TT3O / iGoDz.pw / GoDzM4TT3O.js.org-->\n"
			 "<!DOCTYPE html>\n<html>\n<head>\n<title>Site title</title>\n</head>\n<body>\n"
			 "<p>iEditor for Pythonista by <a href=\"https://godzm4tt3o.js.org\">GoDzM4TT3O</a>. "
			 "<a href=\"https://iGoDz.pw\">Website</a>.</p>\n</body>\n</html>"),
		'txt': name + "\n" + ("-" * 10) + "\n\n",
		'css': "/* iEditor for Pythonista by GoDzM4TT3O */\nhead, body {\n	background-color: blue;\n}"
	}.get(name.split('.')[-1].lower(),
	      console.input_alert("First line", "Type the first line of your program. Examples:\nPython2: #!/usr/bin/env python2\nPython3: #!/usr/bin/env python3\nNote: HTML, CSS, MarkDown and TxT files are pre-loaded with a simple template.\n----------\niEditor for Pythonista by GoDzM4TT3O."))
	editor.make_new_file(name, firstline)
  
if __name__ == '__main__':
	main()
  
# iEditor for Pythonista by GoDzM4TT3O, thanks to cclauss for dictionary lookup
