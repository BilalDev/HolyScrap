# coding: utf-8 

import sys
import hsdb, hshelper, hsrun
# import sched, time
# import gui.MainApplication as MainApplication


hsdb.init_sql()

# display help
if (len(sys.argv) == 2 and sys.argv[1] == '-h') or (len(sys.argv) == 1):
    hshelper.usage()

# run the application
if len(sys.argv) == 2 and sys.argv[1] == '-r':
    hsrun.run_one_time()
# run the application 'cron' way
if len(sys.argv) == 2 and sys.argv[1] == '-rb':
    s = sched.scheduler(time.time, time.sleep)
    s.enter(60, 1, hsrun.run, (s,))
    s.run()

# # run the application
# if len(sys.argv) == 2 and sys.argv[1] == '-rb':
#   window = MainApplication.MainApplication()
#   window.mainloop()


# add an anime
if len(sys.argv) == 4 and sys.argv[1] == '-a':
    hsdb.add_anime(sys.argv[2], sys.argv[3])
# delete an anime
if len(sys.argv) == 3 and sys.argv[1] == '-da':
    hsdb.delete_anime(sys.argv[2])
# update an anime
if len(sys.argv) == 4 and sys.argv[1] == '-ua':
    hsdb.update_anime(sys.argv[2], sys.argv[3])
# list all animes
if len(sys.argv) == 2 and sys.argv[1] == '-la':
    hsdb.get_animes_for_print()

# add a manga
if len(sys.argv) == 4 and sys.argv[1] == '-am':
    hsdb.add_manga(sys.argv[2], sys.argv[3])
# delete a manga
if len(sys.argv) == 3 and sys.argv[1] == '-dm':
    hsdb.delete_manga(sys.argv[2])
# update a manga
if len(sys.argv) == 4 and sys.argv[1] == '-um':
    hsdb.update_manga(sys.argv[2], sys.argv[3], False)
# list all mangas
if len(sys.argv) == 2 and sys.argv[1] == '-lm':
    hsdb.get_mangas_for_print()
