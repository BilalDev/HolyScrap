import sys
import hsdb, hshelper, hsrun
import threading
import sched, time

if (len(sys.argv) == 2 and sys.argv[1] == '-h') or (len(sys.argv) == 1):
    hshelper.usage()

hsdb.init_sql()

# run the application
if len(sys.argv) == 2 and sys.argv[1] == '-r':
    hsrun.run()
# run the application 'cron' way
if len(sys.argv) == 2 and sys.argv[1] == '-rb':
    s = sched.scheduler(time.time, time.sleep)
    s.enter(60, 1, hsrun.run, (s,))
    s.run()
# add a manga
if len(sys.argv) == 4 and sys.argv[1] == '-a':
    hsdb.add_anime(sys.argv[2], sys.argv[3])
# delete a manga
if len(sys.argv) == 3 and sys.argv[1] == '-da':
    hsdb.delete_anime(sys.argv[2])
# update a manga
if len(sys.argv) == 4 and sys.argv[1] == '-ua':
    hsdb.update_anime(sys.argv[2], sys.argv[3])
# list all mangas
if len(sys.argv) == 2 and sys.argv[1] == '-la':
    hsdb.get_animes_for_print()
