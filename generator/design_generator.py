"""
Design Space Generator

This module generates every possible motorcycle design combination
from the design variables defined in the configuration file.

Author: Devadarshan & ChatGPT
"""

from itertools import product


class DesignGenerator:
    """Generates the motorcycle design space."""

    def __init__(self, design_variables: dict):
        self.design_variables = design_variables

    def _generate_range(self, variable: dict) -> list:
        """
        Generate a list of values from min, max, and step.
        """

        minimum = variable["min"]
        maximum = variable["max"]
        step = variable["step"]

        values = []

        current = minimum

        while current <= maximum:
            values.append(current)
            current += step

        return values

    def generate(self) -> list:
        """
        Generate every possible motorcycle design.
        """

        variable_names = []
        variable_values = []

        for name, settings in self.design_variables.items():
            variable_names.append(name)
            variable_values.append(self._generate_range(settings))

        combinations = product(*variable_values)

        designs = []

        for combination in combinations:
            designs.append(dict(zip(variable_names, combination)))

        return designs