"""Defines the HasPaymentState class."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vending_machine.vending_machine import VendingMachine
    
class HasPaymentState(State):
    """Represents the state of a vending machine that has a payment."""

    def receive_payment(self, machine: VendingMachine) -> None:
        """Shows that the payment is already added. 

        Args:
            machine (VendingMachine): The payment received by the vending machine.

        Returns:
            None
        """
        machine.output_to_display("PAYMENT ALREADY ADDED")


    def select_item(self, machine: VendingMachine) -> None:
        """Dispenses the product to the payer.

        Args:
            machine (VendingMachine): Item is selected from the vending machine.

        Returns:
            None
        """
        machine.output_to_display("DISPENSING...", False)
        machine.dispense_product()