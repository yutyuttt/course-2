# Copyright (C) 2025 Jarmo Hurri

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https:#www.gnu.org/licenses/>.

from shelf import Shelf
from user_interface import UserInterface

class VendingMachine:
    def __init__(self):
        self.shelf = Shelf()
        self.ui = UserInterface()

    # application logic
    def run(self):
        while not self.shelf.is_empty():
            available_products = self.shelf.get_available_products()
            purchased_product = self.ui.get_chosen_product(available_products)
            if self.ui.verify_payment(purchased_product):
                self.shelf.dispense(purchased_product)
