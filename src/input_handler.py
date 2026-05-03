import json
from jsonschema import validate, ValidationError
import logging
import os

# Ensure logs folder exists
os.makedirs('logs', exist_ok=True)

# Configure logging
logging.basicConfig(
    filename='logs/provisioning.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

machine_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "os": {"type": "string", "enum": ["Ubuntu", "CentOS", "Windows", "Linux"]},
        "cpu": {"type": "string"},
        "ram": {"type": "string"}
    },
    "required": ["name", "os", "cpu", "ram"]
}

os_map = {
     "ubuntu": "Ubuntu",
     "centos": "CentOS",
     "windows": "Windows",
     "linux": "Linux",
     "lin": "Linux",
     "win": "Windows",
     "l": "Linux",
     "w": "Windows"
}

def get_user_input():
    machines = []
    while True:
        name = input("Enter machine name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        # --- OS loop ---
        while True:
            os_input = input("Enter OS (Ubuntu/CentOS/Windows/Linux): ").lower()
            if os_input in os_map:
                os_input = os_map[os_input]
                break
            logging.error(f"Invalid OS input: {os_input}")
        # --- CPU loop ---
        while True:
            cpu = input("Enter CPU cores (e.g., 2.0): ")
            try:
                cpu_val = float(cpu)
                if cpu_val > 0:
                    break
                else:
                    logging.error(f"CPU must be greater than 0: {cpu}")
            except ValueError:
                logging.error(f"CPU must be a number: {cpu}")
        # --- RAM loop ---
        while True:
            ram = input("Enter RAM in GB (e.g., 4.0): ")
            try:
                ram_val = float(ram)
                if ram_val > 0:
                    break
                else:
                    logging.error(f"RAM must be greater than 0: {ram}")
            except ValueError:
                logging.error(f"RAM must be a number: {ram}")
        # --- All fields valid, add machine ---
        instance_data = {"name": name, "os": os_input, "cpu": cpu, "ram": ram}
        validate(instance=instance_data, schema=machine_schema)
        machines.append(instance_data)
        logging.info(f"Added machine: {name} ({os_input}, {cpu}, {ram})")
    return machines

def save_config(machines):
    try:
        os.makedirs('configs', exist_ok=True)  # Ensure configs folder exists
        with open('configs/instances.json', 'w') as f:
            json.dump(machines, f, indent=4)
        logging.info(f"Saved {len(machines)} machines to configs/instances.json")
    except Exception as e:
        logging.error(f"Failed to save configuration: {e}")
