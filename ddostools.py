import socket
import time
import sys
from threading import Thread

# IMPORTANT ETHICAL CONSIDERATIONS
LEGAL_DISCLAIMER = """
               script made by : <NULL>
               ORGANIZATIONSOCIETY EXCLUSIVE
WARNING: This script is for EDUCATIONAL PURPOSES ONLY.
Unauthorized use against any network or system without explicit permission is ILLEGAL.
our scripts are made for people who want to learn and thrive in this field and not to destroy.
By using this script, you agree to:
1. Only test against systems you own or have written permission to test
2. Not use this for any malicious purposes
3. Understand the legal consequences of misuse
4. Use only in controlled lab environments
5. Script maker *<NULL>* wont have any responsibility for miss-use

Violators may face criminal prosecution.
     Hack with mind
             *ORGANIZATIONSOCIETY*
"""

print(LEGAL_DISCLAIMER)
print("Hack with fun ;)")

def simulate_requests(target_ip, target_port, duration, max_threads):
    """
    Simulates a basic load test with ethical safeguards
    """
    print(f"\nStarting controlled simulation against {target_ip}:{target_port}")
    print(f"Duration: {duration} seconds | Max threads: {max_threads}")
    print("Type CTRL+C to abort early\n")
    
    end_time = time.time() + duration
    threads = []
    
    try:
        for i in range(max_threads):
            if time.time() > end_time:
                break
                
            t = Thread(target=send_limited_request, args=(target_ip, target_port, end_time))
            t.daemon = True
            threads.append(t)
            t.start()
            time.sleep(0.1)  # Ramp up gradually
            
        for t in threads:
            t.join()
            
    except KeyboardInterrupt:
        print("\nSimulation stopped by user")
        
    print("Simulation complete")

def send_limited_request(ip, port, end_time):
    """Send requests with rate limiting and proper error handling"""
    try:
        while time.time() < end_time:
            try:
                # Create socket with timeout to prevent hanging
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                
                # Connect and immediately close (simulating request)
                s.connect((ip, port))
                s.shutdown(socket.SHUT_RDWR)
                s.close()
                
                print(".", end="", flush=True)
                time.sleep(0.1)  # Rate limiting
                
            except Exception as e:
                print("x", end="", flush=True)
                time.sleep(0.5)
                
    except Exception as e:
        print(f"Thread error: {str(e)}")

if __name__ == "__main__":
    # Default to localhost and limited parameters
    TARGET_IP = "127.0.0.1"  # ONLY test against systems you own!
    TARGET_PORT = 80          # Common web port
    DURATION = 10             # 10 second test
    THREADS = 10              # Very limited thread count
    
    print("\nEthical DDoS Simulation Tool (Educational Use Only)")
    print("Default settings target LOCALHOST only")
    
    use_custom = input("Use custom settings? (y/n): ").lower()
    
    if use_custom == "y":
        # Require explicit confirmation for non-localhost targets
        TARGET_IP = input("Target IP (127.0.0.1 strongly recommended): ")
        if TARGET_IP != "127.0.0.1":
            confirm = input(f"WARNING: You are targeting {TARGET_IP}. Do you have LEGAL PERMISSION? (y/n): ")
            if confirm.lower() != "y":
                print("Aborting - unauthorized testing is illegal")
                sys.exit(1)
                
        TARGET_PORT = int(input("Target port: "))
        DURATION = min(60, int(input("Duration (seconds, max 60): ")))
        THREADS = min(50, int(input("Threads (max 50): ")))
        
    simulate_requests(TARGET_IP, TARGET_PORT, DURATION, THREADS)
