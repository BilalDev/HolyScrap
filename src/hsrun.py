# coding: utf-8 

import hsdb
import hsurl


def run(sc=None):
	"""This function starts the processus of downloading animes

	:param sc: Scheduler to execute this function every 60 seconds
	"""
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
				print manga[0] + " : pas de nouvel episode"
	if (sc != None):
		sc.enter(60, 1, run, (sc,))
