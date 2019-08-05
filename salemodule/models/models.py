# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'
    
    priority = fields.Char() 
    
    

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    priority = fields.Selection([ ('high', 'High'),('low', 'Low '),],'Type', default='high')
    
    
    @api.multi
    def _prepare_invoice_line(self, qty):
        res = super(SaleOrderLine, self)._prepare_invoice_line(qty)
        res.update({'priority': self.priority})
        return res
    
    