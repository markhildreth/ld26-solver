cython --embed run.py
gcc $CFLAGS -I/usr/include/python2.7 -o run run.c -lpython2.7 -lpthread -lm -lutil -ldl
./run
