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

from product import Product

class UserInterface:
    
    # returns the product chosen by the customer
    def get_chosen_product(self, available_products):
        print('Available products:')
        for (i, p) in enumerate(available_products):
            print(f'id {i}: {p}')

        chosen_product = None
        while chosen_product == None:
            try:
                chosen_id = int(input('Give id of chosen item and press enter: '))
                if chosen_id >= 0 and chosen_id < len(available_products):
                    chosen_product =  available_products [chosen_id]
                else:
                    raise ValueError()
            except ValueError:
                print('Invalid choice.')

        return chosen_product

    # returns True if the customer verifies payment and False otherwise
    def verify_payment(self, product):
        confirm = input("Confirm purchase (y/n): ")
        if confirm == 'y':
            print("Purchase confirmed.")
            return True
        print("Purchase cancelled.")
        return False
