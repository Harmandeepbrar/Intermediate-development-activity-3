"""Defines the State interface.

A common interface for all vending machine states.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from vending_machine.vending_machine import VendingMachine
    
class State(ABC):
    """Represents the common interface for all vending machine states."""

    @abstractmethod
    def receive_payment(self, vending_machine: VendingMachine) -> None:
        """payment received.

        Args:
            machine (VendingMachine): Payment received by the vending machine.
        Returns:
            None
        """
        
    @abstractmethod
    def select_item(self, vending_machine: VendingMachine) -> None:
        """Selected item from the vending machine.

        Args:
            machine (VendingMachine): Item selected from the vending machine. 

        Returns:
            None
        """