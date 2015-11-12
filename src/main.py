# coding: utf-8 

import sys
import hsdb, hshelper, hsrun
import sched, time
import gui.MainApplication as MainApplication
import Tkinter as tk
# from PIL import Image, ImageTk


# window = tk.Tk()
window = MainApplication.MainApplication()

# image = Image.open('./manga/One Piece/00.jpg')
# photo = ImageTk.PhotoImage(image)
# canvas = tk.Canvas(window, width=image.size[0], height=image.size[1])
# canvas.create_image(0, 0, anchor=tk.NW, image=photo)
# canvas.pack()

window.mainloop()


# if (len(sys.argv) == 2 and sys.argv[1] == '-h') or (len(sys.argv) == 1):
#     hshelper.usage()

# hsdb.init_sql()

# # run the application
# if len(sys.argv) == 2 and sys.argv[1] == '-r':
#     hsrun.run()
# # run the application 'cron' way
# if len(sys.argv) == 2 and sys.argv[1] == '-rb':
#     s = sched.scheduler(time.time, time.sleep)
#     s.enter(60, 1, hsrun.run, (s,))
#     s.run()
# # add a manga
# if len(sys.argv) == 4 and sys.argv[1] == '-a':
#     hsdb.add_anime(sys.argv[2], sys.argv[3])
# # delete a manga
# if len(sys.argv) == 3 and sys.argv[1] == '-da':
#     hsdb.delete_anime(sys.argv[2])
# # update a manga
# if len(sys.argv) == 4 and sys.argv[1] == '-ua':
#     hsdb.update_anime(sys.argv[2], sys.argv[3])
# # list all mangas
# if len(sys.argv) == 2 and sys.argv[1] == '-la':
#     hsdb.get_animes_for_print()
