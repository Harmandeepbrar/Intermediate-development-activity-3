"""Defines the NoPaymentState class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from vending_machine.state import State
from vending_machine.has_payment_state import HasPaymentState

if TYPE_CHECKING:
    from vending_machine.vending_machine import VendingMachine
    
class NoPaymentState(State):
    """Represents the state of no payment in vending machine."""

    def receive_payment(self, machine: VendingMachine)-> None:
        """States the Received payment state.

        Args:
            machine(VendingMachine): The payment received by the vending machine.

        Returns:
            None
        """

        machine.output_to_display("PAYMENT ADDED")
        machine.state = HasPaymentState()

    def select_item(self, machine: VendingMachine) -> None:
        """ Payment need to be added when item is selected.

        Args:
            machine (VendingMachine): Item is selected from the vending machine.

        Returns:
            None
        """

        machine.output_to_display("INSUFFICIENT FUNDS - PLEASE ADD PAYMENT")