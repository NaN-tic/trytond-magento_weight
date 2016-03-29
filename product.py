# This file is part magento_weight module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['Product']


class Product:
    __metaclass__ = PoolMeta
    __name__ = "product.product"

    @classmethod
    def magento_import_product(cls, values, shop=None):
        vals = super(Product, cls).magento_import_product(values, shop)

        weight = values.get('weight')
        if shop and weight and shop.esale_weight_uom:
            vals['weight'] = float(weight)
            vals['weight_uom'] = shop.esale_weight_uom
        return vals

    @classmethod
    def magento_export_product(cls, app, product, shop=None, lang='en_US'):
        Uom = Pool().get('product.uom')

        vals = super(Product, cls).magento_export_product(app, product, shop, lang)

        weight = product.weight
        if shop and shop.esale_weight_uom:
            if product.weight_uom.id != shop.esale_weight_uom.id:
                weight = Uom.compute_qty(product.weight_uom, shop.esale_weight_uom)
        vals['weight'] = weight
        return vals
