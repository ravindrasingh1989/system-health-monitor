import os
import time

def check_system_health():
    print("=" * 40)
    print("       SYSTEM HEALTH REPORT           ")
    print("=" * 40)
    
    # Check CPU count
    cpu_count = os.cpu_count()
    print(f"CPU Cores Available : {cpu_count}")
    
    # Check Current System Time
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Checked At          : {current_time}")
    
    print("-" * 40)
    print("Status: System check executed successfully!")
    print("=" * 40)

if __name__ == "__main__":
    check_system_health()
