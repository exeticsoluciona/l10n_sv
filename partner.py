# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

class Partner(models.Model):
    _inherit = "res.partner"

    pequenio_contribuyente = fields.Boolean(string="Pequeño Contribuyente")
    # NRC PARA COMPROBANTE DE CREDITO FISCAL
    numero_registro = fields.Char('Registro')
    # consumidor_final = fields.Boolean('Consumidor final')
    dui = fields.Char('DUI')
    codigo_actividad = fields.Char('Codigo de Actividad Fel')
