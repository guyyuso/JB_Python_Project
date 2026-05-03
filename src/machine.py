import logging

class Machine:
    def __init__(self, name, os, cpu, ram):
          self.name = name
          self.os = os
          self.cpu = cpu
          self.ram = ram
          self.logger = logging.getLogger(__name__)
          self.logger.setLevel(logging.INFO)

    def to_dict(self):
          return {"name": self.name, "os": self.os, "cpu": self.cpu, "ram": self.ram}

    def create(self):
          self.logger.info(f"Creating machine: {self.name}")
          # Simulate machine creation
          return True
