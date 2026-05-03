# Virtual Machine Infrastructure Simulator

A Python-based infrastructure simulator that allows you to create and manage virtual machine configurations with automated nginx installation simulation.

---

## Features

- 🖥️ **Virtual Machine Creation**: Create virtual machines with customizable CPU, RAM, and OS specifications.  
- 📝 **Configuration Management**: Persistent storage of VM configurations in JSON format (`configs/instances.json`).  
- 🔧 **Automated nginx Installation**: Simulate nginx installation on all created VM instances using a Bash script.  
- 📋 **Input Validation**: Robust validation using `jsonschema` to ensure correct VM data.  
- 📊 **Comprehensive Logging**: Detailed logging of all events and errors in `logs/provisioning.log`.  
- 🛡️ **Error Handling**: Graceful error handling with user-friendly messages.

---

## Project Structure

```

JB_Python_Project/
│── infra_simulation.py
│── vm_config.json              # auto-created after run
│── logs/
│   └── provisioning.log        # auto-created after run
│── configs/
│   └── instance.json           # saved configs
│── scripts/
│   └── install_nginx.sh
└── src/
    ├── input_handler.py
    ├── service_installer.py
    └── machine.py

````

---

## Requirements

## Windows:
  - WSL installed
  - Ubuntu distribution installed in WSL

## Linux/macOS:
  - bash shell available

### Python Dependencies
- Python 3.13.5
- jsonschema 4.0.0
- (install via `pip install -r requirements.txt`)

### System-Level Requirements
The following are required depending on your operating system:

| Operating System | Requirement                                      |
|------------------|--------------------------------------------------|
| Linux / macOS    | Bash shell (typically pre-installed)             |
| Windows          | One of the following Bash environments:          |
|                  | • **Git Bash** (recommended)                     |
|                  | • **WSL with Ubuntu** (run `wsl --install -d Ubuntu`) |

---

## Installation

1. **Clone the repository:**

```bash
git clone github.com/guyusopov/JB_Python_Project
cd JB_Python_Project
````

2. **Create and activate a virtual environment:**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## Usage

### Running the Simulator

Run the main simulator script:

```bash
python infra_simulation.py
```

### Interactive Workflow

1. **Create Virtual Machines:**

   * Enter VM name, OS (`Ubuntu` or `CentOS` or `Windows` or `Linux`), CPU (e.g., `2.0`), and RAM (e.g., `4.0`).
   * Type `done` to finish creating machines.

2. **Configuration Management:**

   * Machine configurations are saved automatically to `configs/instances.json`.

3. **Simulated nginx Installation:**

   * The Bash script `scripts/install_nginx.sh` simulates installing nginx on all created machines.
   * All installation events are logged in `logs/provisioning.log`.

---

## Logging

All key events, successes, and errors are logged in:

```
logs/provisioning.log
```

Example log entries:

```
2025-08-19 15:00:00 - INFO - Added machine: web01 (Ubuntu, 2vCPU, 4GB)
2025-08-19 15:00:01 - INFO - Saved 1 machines to configs/instances.json
2025-08-19 15:00:02 - INFO - Installation successful on 'web01'.
```

---

## Error Handling

* **Validation Errors**: Invalid VM specifications (wrong OS, CPU, or RAM format).
* **File System Errors**: Missing or unreadable configuration/log folders.
* **Process Execution**: Errors during the simulated nginx installation.

All errors are logged with `logging.error()` in `logs/provisioning.log`.

---

## Dependencies

* **Python 3.9+**
* **jsonschema>=4.0.0**

No other external packages are required. Logging is built-in Python library.

---

## Project Notes

* The `install_nginx.sh` script is a **simulation**; no actual VMs or services are created.
* The simulator is **modular**: you can extend `Machine` or the input handler for additional functionality.
* Logs and configurations are stored persistently for review or reuse.

---

**Note:** This project is for educational and simulation purposes only. No real virtual machines are provisioned.








