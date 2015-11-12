from string import maketrans

def usage():
	print '''Usage:\n
- Add a manga:
\tmain.py -a "name of the manga in double quote" episode_number
- Delete a manga:
\tmain.py -da "name of the manga in double quote"
- List all mangas:
\tmain.py -la
- Update a manga:
\tmain.py -ua "name of the manga in double quote" episode_number
- List all series:
\tmain.py -ls
- Run application:
\tmain.py -r
- Run application 'cron' way:
\tmain.py -rb
'''

def replace_special_chars(str_to_translate):
	str_to_translate = str(str_to_translate)
	special_chars = "<>:\"/\|?*"
	empty_chars = '_________'
	translatable = maketrans(str(special_chars), str(empty_chars))
	return str_to_translate.translate(translatable)
