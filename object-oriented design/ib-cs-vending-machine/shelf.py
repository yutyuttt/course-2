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

class Shelf:
    def __init__(self):
        self.products = [Product.Beverage, Product.Apple, Product.Banana, Product.Chocolate]
        self.quantities = [2, 1, 3, 2]

    # returns a list of products available (for which quantity is
    # positive)
    def get_available_products(self):
        return [p for (p, q) in zip(self.products, self.quantities) if q > 0]

    # returns true if there are no more products to be sold and false
    # otherwise
    def is_empty(self):
        return len(self.products) == 0

    # dispenses a product (that is, in this simple app just decreases
    # its quantity by 1)
    def dispense(self, product):
        index = self.products.index(product)
        self.quantities[index] -= 1
