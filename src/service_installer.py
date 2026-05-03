import subprocess
import logging
import platform
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(
    filename='logs/provisioning.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def install_service(vm_name):
    try:
        if platform.system() == "Windows":
            # Run inside Ubuntu WSL
            cmd = ["wsl", "-d", "Ubuntu", "bash", "scripts/install_nginx.sh", vm_name]
        else:
            # Linux/macOS
            cmd = ["bash", "scripts/install_nginx.sh", vm_name]

        subprocess.run(cmd, check=True)
        logging.info(f"Service installation completed successfully on {vm_name}.")
    
    except subprocess.CalledProcessError as e:
        logging.error(f"Error occurred during service installation on {vm_name}: {e}")

