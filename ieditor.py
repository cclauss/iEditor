#!/usr/bin/env python3
import editor, console
def main():
	
  
	name = console.input_alert("Name", 'Choose a name for your new file with an extension (e.g. .txt | .html | .py | .md)')
	firstline = console.input_alert("First line", "Type the first line of your program. Examples:\nPython2: #!/usr/bin/env python2\nPython3: #!/usr/bin/env python3\nNote: HTML, CSS, MarkDown and TxT files are pre-loaded with a simple template.\n----------\niEditor for Pythonista by GoDzM4TT3O.")
	if '.md' in name:
		firstline = "# " + name + "\n\n"
	elif '.html' in name:
		firstline = "<!--iEditor by GoDzM4TT3O / iGoDz.pw / GoDzM4TT3O.js.org-->\n<!DOCTYPE html>\n<html>\n<head>\n<title>Site title</title>\n</head>\n<body>\n<p>iEditor for Pythonista by <a href=\"https://godzm4tt3o.js.org\">GoDzM4TT3O</a>. <a href=\"https://iGoDz.pw\">Website</a>.</p>\n</body>\n</html>"
	elif '.txt' in name:
		firstline = name + "\n" + ("-" * 10) + "\n\n"
	elif '.css' in name:
		firstline = "/* iEditor for Pythonista by GoDzM4TT3O */\nhead, body {\n	background-color: blue;\n}"
	editor.make_new_file(name, firstline)
	
  
if __name__ == '__main__':
	main()
  
# iEditor for Pythonista by GoDzM4TT3O
