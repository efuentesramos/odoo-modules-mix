#-*- coding: utf-8 -*-
from odoo import api, fields, models
import datetime
from datetime import date
from odoo.exceptions import ValidationError
from odoo.tools.translate import _  # ✅ Importar `_` correctamente
from sqlalchemy.sql import text  


class apu(models.Model): 
    _name = 'apu'
   
   # _rec_name='version_plann'


    name = fields.Char(string='Proyecto')
    contractor = fields.Char(string='Contratista')
    description = fields.Char(string='Descripcion de Actividad')

    detail_material_id=fields.One2many( string='Materiales',comodel_name='detail.material',inverse_name='apu_id')
    
    detail_equipment_id=fields.One2many( string='Equipos',comodel_name='detail.equipment',inverse_name='apu_id')

    detail_other_item_id=fields.One2many( string='Otros Items',comodel_name='detail.other.item',inverse_name='apu_id')

    detail_manpower_id=fields.One2many( string='Mano de Obra',comodel_name='detail.manpower',inverse_name='apu_id')


    # *** Values Material **** 

    material_costs= fields.Float(string="Costo de materiales", compute='_compute_material_cost')

    material_sales = fields.Float(string = "Precio de Venta", compute='_compute_material_sales')
    
    material_costs_percent = fields.Float(string="% Costo de materiales",default=0, compute='_compute_material_cost_percent')

    material_profits = fields.Float(string="Utilidad de materiales", compute='_compute_material_profits') 

    # **** Values Equipment ****

    equipment_costs= fields.Float(string="Costo de equipos", compute='_compute_equipment_cost')

    equipment_sales = fields.Float(string = "Precio de Venta", compute='_compute_equipment_sales')
    
    equipment_costs_percent = fields.Float(string="% Costo de equipos",default=0, compute='_compute_equipment_cost_percent')

    equipment_profits = fields.Float(string="Utilidad de equipos", compute='_compute_equipment_profits') 




     # **** Values Manpower ****

    manpower_costs= fields.Float(string="Costo de equipos", compute='_compute_manpower_cost')

    manpower_sales = fields.Float(string = "Precio de Venta", compute='_compute_manpower_sales')
    
    manpower_costs_percent = fields.Float(string="% Costo de equipos",default=0, compute='_compute_manpower_cost_percent')

    manpower_profits = fields.Float(string="Utilidad de equipos", compute='_compute_manpower_profits') 



    # **** Values Other Item ****

    other_costs= fields.Float(string="Costo de Otros items", compute='_compute_other_cost')

    other_sales = fields.Float(string = "Precio de Otros items", compute='_compute_other_sales')
    
    other_costs_percent = fields.Float(string="% Costo de Otros items",default=0, compute='_compute_other_cost_percent')

    other_profits = fields.Float(string="Utilidad de Otros Items", compute='_compute_other_profits') 






    # Values for Smumary **

    sale_total = fields.Float(string = "Precio de Venta", compute='_compute_sale_total')

    cost_total= fields.Float(string = "Precio de Venta", compute='_compute_costs_total')

    profit_total =  fields.Float(string = "Precio de Venta", compute='_compute_profit_total')

    percent_total = fields.Float(string = "Precio de Venta", compute='_compute_percent_total')

    percent_profit_total = fields.Float(string = "% De Utilidad", compute='_compute_percent_prifit_total')


    trm_usd = fields.Float(string="TRM")

    sales_in_dollar = fields.Float(string="sales usd" , compute='_compute_sales_usd')


    
    


    @api.depends('detail_material_id.material_cost')
    def _compute_material_cost(self):
        for record in self:
            record.material_costs = sum(record.detail_material_id.mapped('material_cost'))

    
    @api.depends('detail_material_id.sale_price')
    def _compute_material_sales(self):
        for record in self:
            record.material_sales = sum(record.detail_material_id.mapped('sale_price'))

    

    @api.depends('detail_material_id.total_profit')
    def _compute_material_profits(self):
        for record in self:
            record.material_profits = sum(record.detail_material_id.mapped('total_profit'))



    @api.depends('material_costs', 'cost_total')
    def _compute_material_cost_percent(self):
        for record in self:
            if record.cost_total > 0 :
                record.material_costs_percent = record.material_costs / record.cost_total
            else :
                record.material_costs_percent = 0



    ####### METHODS FOR EQUIPMENT ###########

    @api.depends('detail_equipment_id.equipment_cost')
    def _compute_equipment_cost(self):
        for record in self:
            record.equipment_costs = sum(record.detail_equipment_id.mapped('equipment_cost'))

    
    @api.depends('detail_equipment_id.sale_price')
    def _compute_equipment_sales(self):
        for record in self:
            record.equipment_sales = sum(record.detail_equipment_id.mapped('sale_price'))

    

    @api.depends('detail_equipment_id.total_profit')
    def _compute_equipment_profits(self):
        for record in self:
            record.equipment_profits = sum(record.detail_equipment_id.mapped('total_profit'))



    @api.depends('equipment_costs', 'cost_total')
    def _compute_equipment_cost_percent(self):
        for record in self:
            if record.cost_total > 0 :
                record.equipment_costs_percent = record.equipment_costs / record.cost_total
            else :
                record.equipment_costs_percent = 0 


    ####### METHODS FOR MANPOWER  ##############

   
    @api.depends('detail_manpower_id.manpower_cost')
    def _compute_manpower_cost(self):
        for record in self:
            record.manpower_costs = sum(record.detail_manpower_id.mapped('manpower_cost'))

    
    @api.depends('detail_manpower_id.sale_price')
    def _compute_manpower_sales(self):
        for record in self:
            record.manpower_sales = sum(record.detail_manpower_id.mapped('sale_price'))

    

    @api.depends('detail_manpower_id.total_profit')
    def _compute_manpower_profits(self):
        for record in self:
            record.manpower_profits = sum(record.detail_manpower_id.mapped('total_profit'))



    @api.depends('manpower_costs', 'cost_total')
    def _compute_manpower_cost_percent(self):
        for record in self:
            if record.cost_total > 0 :
                record.manpower_costs_percent = record.manpower_costs / record.cost_total
            else :
                record.manpower_costs_percent = 0 







####### METHODS FOR OTHER ITEMS   ##############

   
    @api.depends('detail_other_item_id.other_item_cost')
    def _compute_other_cost(self):
        for record in self:
            record.other_costs = sum(record.detail_other_item_id.mapped('other_item_cost'))

    
    @api.depends('detail_other_item_id.sale_price')
    def _compute_other_sales(self):
        for record in self:
            record.other_sales = sum(record.detail_other_item_id.mapped('sale_price'))

    

    @api.depends('detail_other_item_id.total_profit')
    def _compute_other_profits(self):
        for record in self:
            record.other_profits = sum(record.detail_other_item_id.mapped('total_profit'))



    @api.depends('other_costs', 'cost_total')
    def _compute_other_cost_percent(self):
        for record in self:
            if record.cost_total > 0 :
                record.other_costs_percent = record.other_costs / record.cost_total
            else :
                record.other_costs_percent = 0 


    
    ######    M E T H O D S    F O R    S U M A R Y    ######

    # se suma todas las ventas

    @api.depends('material_sales','equipment_sales','manpower_sales','other_sales')
    def _compute_sale_total(self):
        for record in self:
            record.sale_total = record.material_sales + record.equipment_sales + record.manpower_sales + record.other_sales

    # Se suma todos costos
    @api.depends('material_costs', 'equipment_costs','manpower_costs','other_costs')
    def _compute_costs_total(self):
        for record in self:
            record.cost_total = record.material_costs + record.equipment_costs + record.manpower_costs + record.other_costs

    # Se Suma todos los profit

    @api.depends('material_profits','equipment_profits','manpower_profits')
    def _compute_profit_total(self):
        for record in self:
            record.profit_total = record.material_profits + record.equipment_profits + record.manpower_profits


    
    @api.depends('material_costs_percent','equipment_costs_percent','manpower_costs_percent','other_costs_percent')
    def _compute_percent_total(self):
        for record in self:
            record.percent_total = record.material_costs_percent + record.equipment_costs_percent + record.manpower_costs_percent + record.other_costs_percent



    @api.depends('profit_total', 'sale_total')
    def _compute_percent_prifit_total(self):
        for record in self:
            if record.sale_total > 0 :
                record.percent_profit_total = record.profit_total / record.sale_total
            else :
                record.percent_profit_total = 0 
    


    @api.depends('sale_total','trm_usd')
    def _compute_sales_usd(self):
        for record in self:
            if record.trm_usd > 0 :
                record.sales_in_dollar = record.sale_total / record.trm_usd
            else :
                record.sales_in_dollar = 0
                


    def update_items_apu(self):
        """Método para actualizar items en el APU"""
        print ("******  I T E M S     F O R     A P U S *******")
        
        #base_dbs_obj = self.env['base.external.dbsource']

        dbsource = self.env['base.external.dbsource'].search([('name', '=', 'astivikDB')], limit=1)
        if not dbsource:
            raise ValidationError(_('No se encuentra el registro para conexión a la base de  Datos de Astivik. \n' \
                                    'Asegurece de que el registro de configuración se llame "astivikDB"\n' \
                                    'Ajustes/Estructura de la base de datos/Database Sources'))


    


        try:
            connection = dbsource.connection_open_mssql()
            transaction = connection.begin() #conexion a base de datos 
            
           # -------------  Query for all Items --------------
                
            material_db=self.env['apu.manager.material']
            equipment_db=self.env['apu.manager.equipment']
            manpower_db=self.env['apu.manager.manpower']
            other_items_db=self.env['other.item']

            query_material_db = text("SELECT * FROM material")
            query_equipment_db = text("SELECT * FROM equipment")
            query_manpower_db = text("SELECT * FROM manpower")  
            query_other_items_db = text("SELECT * FROM other_item")
            
            all_materials = connection.execute(query_material_db).fetchall()
            all_equipment = connection.execute(query_equipment_db).fetchall()
            all_mampower = connection.execute(query_manpower_db).fetchall()
            all_other_item = connection.execute(query_other_items_db).fetchall()

            

            #---------- Creation Of Materials Record  -----------------

            for item_material in all_materials:

                material_db.create({'name':item_material[0],'unit_measurement':item_material[1],'unit_cost':item_material[2] })
            

             #---------- Creation Of Equipment Record  -----------------

            for item_material in all_equipment:

                equipment_db.create({'name':item_material[0],'unit_measurement':item_material[1],'unit_cost':item_material[2] })
            

             #---------- Creation Of Manpower Record  -----------------

            for item_material in all_mampower:

                manpower_db.create({'name':item_material[0],'unit_measurement':item_material[1],'unit_cost':item_material[2] })
            

             #---------- Creation Of Other Items  -----------------

            for item_material in all_other_item:

                other_items_db.create({'name':item_material[1],'unit_measurement':item_material[2],'unit_cost':item_material[3] })
            

            dbsource.connection_close_mssql(connection)

        except Exception as error_astivik:
            if transaction and connection:
                transaction.rollback()
                dbsource.connection_close_mssql(connection)
            
            #raise ValueError("No se encontró la conexión a MSSQL en 'base.external.dbsource'.")
            raise ValidationError(_('No se ha podido enviar a DMS \n\n %s') % 
                str(error_astivik.args and error_astivik.args[0] or error_astivik))
           

    
