#This file is part magento_weight module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['SaleShop']
__metaclass__ = PoolMeta


class SaleShop:
    __name__ = 'sale.shop'
    esale_weight_uom = fields.Many2One('product.uom', 'Weight Uom',
        help='Default Weight Uom')
