# coding: utf-8 

import hsdb, hsurl
from time import sleep

def run(thread):
	"""This function starts the processus of downloading animes"""
	mangas = hsdb.get_animes()
	for manga in mangas:
		if thread.stopped() == False:
			episode_name = manga[0] + ' ' + str(manga[1]).zfill(2)
			html = hsurl.get_html_from_anime(episode_name)
			if html:
				query = [manga[0], str(manga[1]).zfill(2)]
				torrent = hsurl.search_result(html, query)
				if torrent and len(torrent) == 4:
					hsurl.download_torrent(torrent)
				else:
					print manga[0] + " : pas de nouvel episode"

	if (thread.stopped() == False):
		sleep(3600)
		run(thread)

