 # -*- coding: utf-8 -*-

from odoo import models, fields, api

    
class Employe(models.Model):
    _name = 'employe'
    
    
    name = fields.Char("Employe's Name")
    image_medium = fields.Binary()
    
    type = fields.Selection([('sales','sales'),('trainer','trainer'),('employe','employe'),('conslutant','conslutant')],string="e.g. part time")
    workaddress = fields.Char("Work address")
    worklocation = fields.Char("Work location")
    workemail = fields.Char("Work email")
    workphone = fields.Char("Work phone")
    
    department = fields.Many2one('department','dept_name')
    jobposition = fields.Many2one('job.position','jobposition')
    jobtitle = fields.Char()
    manager = fields.Many2one('employe','manager')
    coach = fields.Many2one('employe','coach')
    
    
    nationality = fields.Char("country")
    identification_no = fields.Char("Identification No:")
    passport_no = fields.Integer("Passport NO:")
    bankaccount_no = fields.Integer("Bank account No:")
    
    privateaddress = fields.Char("Private Address")
    emergencycontact = fields.Char("Private Contact:")
    emergencyphone = fields.Char("Emergency Phone:")
    kmhomework = fields.Char("km HOme work")
    
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender")
    matrialstatus = fields.Selection([('maried','maried'),('devorced','devorced'),('widover','widover'),('single','single')],string="Matrial Status")
    nochildren = fields.Integer("No. Of childrens")
    
    dateofbirth = fields.Date("Date of Birth")
    placeofbirth = fields.Char("Place of Birth:")
    countryofbirth = fields.Char("country of Birth:")
    
    visano = fields.Integer("Visa NO")
    workprmitno = fields.Integer("Work permit NO:")
    visaexpirydate = fields.Date("Visa Expiry Date")
    
    certificatelevel = fields.Selection([('master','master'),('bachloar','bachloar'),('other','other')],string="Certificate Level")
    fieldofstudy = fields.Char("Field of study:")
    school = fields.Char("School:")
    
    employedoc = fields.Char("Employe Document")
    addnotes = fields.Char("Additional Notes")
    
    passprt_no = fields.Char("passport Number")
    passpro = fields.Char("passport Number")
    
    
class Contract(models.Model):
    _name = 'contract'
    
    contractreference = fields.Char("Contract Reference") 
    employee = fields.Many2one('employe','employee')
    employeecategory = fields.Char("employe Category")
    salarysturcture = fields.Char("structure")       
    department = fields.Char()
    jobposition = fields.Char()
    
    startdate = fields.Date("Start Date")
    enddate = fields.Date("End Date")
    endtrialperiod = fields.Date("End trial period")
    workingscheduling = fields.Char("Working scheduling")
    schedulingpay = fields.Selection([('monthly','monthly'),('quatrly','Quaterly'),('annually','annually'),('semiannually','Semi annually'),('weekly','weekly')],string="scheduling PAy")
    
    
    notes = fields.Char("Notes")
    
    wage = fields.Integer()
    
    @api.onchange('employee')
    def emp_change(self):
        for rec in self:
            rec.department=rec.employee.department.name
            rec.jobposition=rec.employee.jobposition.name
    
    
class Loan_type(models.Model):
    _name = 'loan.type'
    
    name = fields.Char("Loan Type")
    description = fields.Char("terms and conditions")
    
class emp_loan(models.Model):
    _name = 'emp.loan'
    
    employee = fields.Many2one('hr.employee','employee')
    department = fields.Char()
    jobposition = fields.Char()
    
    loantype = fields.Many2one('loan.type','description')
    
    amount = fields.Integer("Amount")
    tenure = fields.Integer("Months")
    descripton = fields.Char("Description")
    
    terms = fields.Char('terms')
     
    @api.onchange('loantype')
    def loantype_change(self):
        for rec in self:
            rec.terms=rec.loantype.description
     
    @api.onchange('employee')
    def employee_change(self):
        for rec in self:
            rec.department=rec.employee.department_id.name
            rec.jobposition=rec.employee.job_id.name
            
            
    
    
class Department(models.Model):
    _name = 'department'
    
    name = fields.Char("Department Name")
    manager = fields.Many2one('employe','employe')
    
class job_Position(models.Model):
    _name = 'job.position'
    
    name = fields.Char("Job Position")
    department = fields.Many2one('department','department')
    newemploye = fields.Char()
    jobdescription =fields.Char()
    
class sale_wizard(models.TransientModel):
    _name = 'sale.wizard'
    
    partner_id  = fields.Many2one('res.partner', string="Name")
    name = fields.Char()
    
    @api.multi
    def set_partner_id(self):
        for record in self:
            record.name = record.partner_id.parent_id
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
