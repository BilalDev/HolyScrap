import os
import urllib2
from bs4 import BeautifulSoup
import subprocess
import hsdb, hshelper


def download_torrent(torrent):
	"""This function downloads a torrent

	:param torrent: Name of the torrent to be downloaded
	"""
	fname = os.getcwd() + '/' + hshelper.replace_special_chars(torrent[0]) + '.torrent'
	with open (fname, 'wb') as f:
		f.write(urllib2.urlopen(torrent[1]).read())
	f.close()
	subprocess.call(["C:\\Program Files (x86)\\uTorrent\\uTorrent.exe", fname])
	hsdb.update_anime(str(torrent[2]), str(int(torrent[3]) + 1))


def get_html_from_anime(name):
	"""This function gets the content of an HTML page

	:param name: The anime name (e.g: One Piece 717)
	:returns: The readed response or false
	"""
	name += ' vostfr'
	url = 'https://www.nyaa.eu/?page=search&sort=2&term=' + name
	try:
		response = urllib2.urlopen(url)
		if response.getcode() == 200:
			return response.read()
		else:
			return False
	except:
		print "Probleme lors de l'ouverture de l'url de recherche: " + name
		pass


def search_result(html, query):
	"""This function searchs for torrent file in an HTML document

	:param html: The HTML document
	:param query: Tuple containing information about the anime (name, episod number)
	:returns: A tuple containing the HTML name, link of the torrent, name of the anime and the episod number
	"""
	try:
		name_lower = query[0].lower()
		name_lower_underscore = query[0].lower().replace(" ", "_")
		findNumberAndVostfr = False
		soup = BeautifulSoup(html, 'lxml')
		rows = soup.find('table', {'class': 'tlist'}).find_all('tr', {'class': 'tlistrow'})
		for row in rows:
			name = row.find('td', {'class': 'tlistname'}).get_text().lower()
			href = row.find('td', {'class': 'tlistdownload'}).find('a')['href']

			# find episode number and vostfr in the name
			try:
				find_numero_episode = name.index(query[1].lower())
				find_vostfr = name.index('vostfr')
				findNumberAndVostfr = True
			except:
				pass
			if findNumberAndVostfr:
				# find name in lower case in the name
				try:
					find_name = name.index(name_lower)
					return [name, href, query[0], query[1]]
				# find name in lower with underscore instead of space in the name
				except ValueError as ve:
					find_name = name.index(name_lower_underscore)
					return [name, href, query[0], query[1]]
				# doesn't find, pass to the next
				except:
					pass
	except:
		pass

	return False
