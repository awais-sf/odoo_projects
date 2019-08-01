 # -*- coding: utf-8 -*-

from odoo import models, fields, api
from unicodedata import category
import string
    
# class SaleOrder(models.Model):
#     _inherit = "sale.order"
# 
#     nationality_prefex = fields.Integer('Prefex #No.')
#     prefex_count = fields.Integer('')
    
class Scholars(models.Model):
    _name = 'scholar'
    _description="scholars"
    
    name = fields.Char("Name")
    cell = fields.Char()
    address = fields.Char("addresss")
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender")
    post = fields.Many2many('posts','scholar_posts_rel','scholar_id','posts_id', string="Posts")
    scholar_id = fields.Many2one('category','type')

class Category(models.Model):
    _name = 'category'
    _description = 'type'
    
    categoryname = fields.Char("enter category name")
    exp = fields.Char("experience of this categories")
    scholars = fields.Many2many('scholar','category_scholar_rel','category_id','scholar_id', string="scholars") 
    
class ScholarPost(models.Model):
    _name = 'posts'
    
    category = fields.Many2one('category','type')
    date = fields.Date('enter date')
    city = fields.Char('Enter city')
    scholars = fields.Many2many('scholar','posts_scholar_rel','posts_id','scholar_id', string="scholars") 
    
    
    
    
class Scholars(models.Model):
    _inherit = 'scholar'
    
    fname = fields.Char("fathername")
    work = fields.Char("bussiness")
    firstpage = fields.Char("first page")
    secondpage = fields.Char("second page")
   
   
class SaleOrder(models.Model):
    _inherit = 'sale.order'
      
    nationality_prefex = fields.Integer('Prefex #No.')
    newPage = fields.Char("new page")
    age = fields.Integer("enter Age")