from odoo import models, fields, api

# Definimos el modelo de datos
class ListaTareas(models.Model):
    # Nombre y descripción del modelo de datos
    _name = 'lista_tareas.lista_tareas'
    _description = 'lista_tareas.lista_tareas'

    tarea = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()

    @api.depends('prioridad')
    def _value_urgente(self):
        # Para cada registro
        for record in self:
            if record.prioridad > 10:
                record.urgente = True
            else:
                record.urgente = False
