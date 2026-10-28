"""Defines the OutOfStockState class."""
from __future__ import annotations

from typing import TYPE_CHECKING

from vending_machine.state import State


if TYPE_CHECKING:
    from vending_machine.vending_machine import VendingMachine


class OutOfStockState(State):
    """Represents the state that there is no stock available."""

    def receive_payment(self, machine: VendingMachine) -> None:
        """Shows the customer that the machine is out of stock.

        Args:
            machine (VendingMachine): The payment received by the vending machine.

        Returns:
            None
        """

        machine.output_to_display("OUT OF STOCK")

    def select_item(self, machine: VendingMachine) -> None:
        """Shows nothing as there is no item to dispense.

        Args:
            machine (VendingMachine): Item is selected from the vending machine.

        Returns:
            None
        """

        machine.output_to_display("")