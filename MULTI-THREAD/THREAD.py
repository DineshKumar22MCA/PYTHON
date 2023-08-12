import threading
import time


def update_db():
    for i in range(1,6):
        print("updating")
        time.sleep(3)
    else:
        print("updated successfully")


def display_nums():
    for i in range(1, 5 + 1):
        print(i)

# update_db()
thread_db = threading.Thread(target=update_db)
thread_db.start()

display_nums()

print("active thread count : ",threading.active_count())
print(threading.enumerate())

thread_db.join()
print("Bye")