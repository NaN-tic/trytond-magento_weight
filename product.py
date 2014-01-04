#This file is part magento_weight module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['Product']
__metaclass__ = PoolMeta


class Product:
    "Product Variant"
    __name__ = "product.product"

    @classmethod
    def magento_template_dict2vals(self, shop, values):
        '''
        Add weight in Magento values to Template
        :param shop: obj
        :param values: dict from Magento Product API
        return dict
        '''
        vals = super(Product, self).magento_template_dict2vals(shop, values)
        weight = values.get('weight')
        if weight and shop.esale_weight_uom:
            vals['weight'] = float(weight)
            vals['weight_uom'] = shop.esale_weight_uom
        return vals
