import hsdb
import hsurl

import threading

def run(sc=None):
	mangas = hsdb.get_animes()
	for manga in mangas:
		episode_name = manga[0] + ' ' + str(manga[1]).zfill(2)
		html = hsurl.get_html_from_anime(episode_name)
		if html:
			query = [manga[0], str(manga[1]).zfill(2)]
			torrent = hsurl.search_result(html, query)
			if torrent and len(torrent) == 4:
				hsurl.download_torrent(torrent)
			else:
				print "Nothing to do"
	if (sc != None):
		sc.enter(60, 1, run, (sc,))
