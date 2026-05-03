from src.machine import Machine
from src.input_handler import save_config, get_user_input
from src.service_installer import install_service
import logging

# Configure logging
logging.basicConfig(
    filename='logs/provisioning.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    try:
        logging.info("Starting infrastructure simulation")

        # Get user input
        machines_data = get_user_input()
        logging.info(f"Received {len(machines_data)} machines from user input")

        # Create machine objects
        machine_objects = []
        for machine_data in machines_data:
            machine = Machine(**machine_data)
            if machine.create():
                machine_objects.append(machine)
                logging.info(f"Created machine: {machine.name}")

        # Save configuration
        save_config([m.to_dict() for m in machine_objects])
        logging.info("Saved machine configurations to configs/instances.json")

        # Install services for each machine
        for m in machine_objects:
            install_service(m.name)

    except Exception as e:
        logging.error(f"An error occurred during provisioning: {e}")

if __name__ == "__main__":
    main()
