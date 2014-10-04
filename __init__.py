#This file is part magento_weight module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
from .shop import *
from .product import *


def register():
    Pool.register(
        SaleShop,
        Product,
        module='magento_weight', type_='model')
