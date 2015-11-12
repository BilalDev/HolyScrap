# coding: utf-8 

import sys
import threading
import Tkinter as tk

import hsdb, hshelper, hsrun

labels = []

class MainApplication(tk.Tk):
	"""Main user interface"""
	def __init__(self):
		tk.Tk.__init__(self)
		# Window maximized
		self.winfo_toplevel().wm_state('zoomed')

		self.create_canvas()

		self.MenuBar()
		self.config(menu=self.menuBar)

		# run download torrent every hour
		try:
			self.scrapThread = RunThread()
			self.scrapThread.start()
		except(SystemExit):
			self.scrapThread.stop()
			sys.exit(0)


	def create_canvas(self):
		self.mainFrame = tk.Frame(self)
		self.mainFrame.pack(fill=tk.BOTH, expand=tk.YES)

		self.canvas = ResizingCanvas(self.mainFrame, width=800, height=600, highlightthickness=0)
		self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
		self.canvas.addtag_all('all')


	def list_anime(self):
		for label in labels:
			label.destroy()

		del labels[:]

		mangas = hsdb.get_animes()

		labels.append(tk.Label(self.canvas, text='Liste des animés:', font='Helvetica 16 bold').grid(row=0, column=0))

		index = 1
		for manga in mangas:
			for col in range(2):
				labels.append(tk.Label(self.canvas, text=manga[col]).grid(row=index, column=col, sticky=tk.W))

			index = index + 1


	def MenuBar(self):
		self.menuBar = tk.Menu(master=self)

		self.fileMenu = tk.Menu(self.menuBar, tearoff=False)
		self.fileMenu.add_command(label='Ajouter anime', underline=0, command=self.quit)
		self.fileMenu.add_command(label='Lister les animés', underline=0, command=self.list_anime)
		self.fileMenu.add_separator()
		self.fileMenu.add_command(label='Quitter', underline=0, command=self.quit)

		self.menuBar.add_cascade(label='Fichier', menu=self.fileMenu)


	def quit(self):
		self.scrapThread.stop()
		sys.exit(0)



class RunThread(threading.Thread):
	def __init__(self):
		self._stop = threading.Event()
		threading.Thread.__init__(self)

	def run(self):
		threading.Thread(target=hsrun.run, args=(self,)).start()

	def stop(self):
		self._stop.set()

	def stopped(self):
		return self._stop.isSet()

class ResizingCanvas(tk.Canvas):
	def __init__(self, parent, **kwargs):
		tk.Canvas.__init__(self, parent, **kwargs)
		self.bind('<Configure>', self.on_resize)
		self.height = self.winfo_reqheight()
		self.width = self.winfo_reqwidth()


	def on_resize(self, event):
		# determine the ratio of old width/height to new width/height
		wscale = float(event.width) / self.width
		hscale = float(event.height) / self.height
		self.width = event.width
		self.height = event.height
		# resize the canvas 
		self.config(width=self.width, height=self.height)
		# rescale all the objects tagged with the "all" tag
		self.scale('all', 0, 0, wscale, hscale)
