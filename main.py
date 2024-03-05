from socket import *
import time
import sys
start_time = time.time()

if __name__ == '__main__':
    target = input("Enter the host to be scaned:")
    t_IP = gethostbyname(target)
    print('starting scan on host: ', t_IP)
    loading_length = 20
    for i in range(1,  65535):
        s = socket(AF_INET, SOCK_STREAM)
        progress = (i - 20) % 20
        if progress > 20:
            progress = 0
        sys.stdout.write('\rScanning port %d [%s%s]' % (i, '#' * progress, '-' * (loading_length - progress)))
        sys.stdout.flush()
        connection = s.connect_ex((t_IP, i))
        if connection == 0:
            print('Port %d: open' % (i,))
        s.close()

    print('Time taken: ', time.time()-start_time)