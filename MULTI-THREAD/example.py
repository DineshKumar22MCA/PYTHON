import threading
import time

class A(threading.Thread):
    def run(self):
        for i in range (1,6):
            print("updating")
            time.sleep(5)
        else:
            print("update successfully")

class B:
    def num(self):
        for i in range (1,6):
            print(i)




t = A()
t.start()

o = B()
o.num()

print("active thread count : ",threading.active_count())
print(threading.enumerate())

t.join()
print("Bye")