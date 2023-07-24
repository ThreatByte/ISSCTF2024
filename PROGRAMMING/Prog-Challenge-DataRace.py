import threading
import time
from msg import testing

# Global variables
decryption_key = testing.returnMSG() #returning the msg 
decryption_complete = False
lock = threading.Lock()
load = 0 # precentage tracker...

def decryption_process():
    global decryption_key, decryption_complete
    # Simulate decryption process
    for _ in range(5):
        # Simulate some processing time
        time.sleep(1)
        
        # Vulnerable section (data race condition)
        decryption_key += "X"
        
        print("decrypting")
        
    # Notify completion
    decryption_complete = True

def exploit_data_race():
    global decryption_key, decryption_complete
    while not decryption_complete:
        with lock:
            time.sleep(14)
            if decryption_key != "":
                print(" EXPLOITED! Decryption Key:", decryption_key)
                break 

def main():
    global decryption_key, decryption_complete
    
    # Create threads
    threads = []
    for _ in range(5):
        t = threading.Thread(target=decryption_process)
        threads.append(t)
        t.start()
    

    # Create exploit thread
    exploit_thread = threading.Thread(target=exploit_data_race)
    exploit_thread.start()

    # Wait for threads to complete
    while not decryption_complete:
        pass

    #print("Decryption Key:", decryption_key)

if __name__ == "__main__":
    main()
