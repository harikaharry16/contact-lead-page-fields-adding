from odoo import models, fields,api,_




# **************************************** creating Topic of interest menu in contacts/configuraion module ************************************************

class TopicOfInterest(models.Model):
    _name = 'topic.of.interest'
    _description = 'Topic of Interest'

    name = fields.Char(string='Topic Name', required=True)


# *********************************** adding software as one detailed_type in product.template model*************************
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Extending the detailed_type selection field to add "software"
    detailed_type = fields.Selection(
        selection_add=[('software', 'Software')],
        ondelete={'software': 'set default'}
    )



    type = fields.Selection(
        selection_add=[('software', 'Software')],
        ondelete={'software': 'set default'},
        default='product'  # Set a default for the type field
    )

    def _compute_type(self):
        type_mapping = {
            'consu': 'consu',
            'service': 'service',
            'software': 'software',
            'product': 'product',
        }
        for record in self:
            record.type = type_mapping.get(record.detailed_type, 'product')


# ************************Adding fields topic_of_interest,service_interest,software_interest in contacts************************

class Partner(models.Model):
    _inherit = 'res.partner'

    topic_of_interest_wf = fields.Many2one('topic.of.interest', string='Topic of Interest WF')

    service_interest = fields.Many2many(
        'product.product',
        'res_partner_service_interest_rel',  # Unique table name
        'partner_id', 'product_id',
        string='Service Interest',
        domain=[('detailed_type', '=', 'service')]
    )

    software_interest = fields.Many2many(
        'product.product',
        'res_partner_software_interest_rel',  # Another unique table name
        'partner_id', 'product_id',
        string='Software Interest',
        domain=[('detailed_type', '=', 'software')]
    )

    lead_source = fields.Many2one('utm.medium', string="Lead Source")
    # service_interest = fields.Many2many('product.product',string='Service Interest',domain=[('detailed_type', '=', 'service')])
    # software_interest = fields.Many2many('product.product',string='Software Interest')


# ************************Adding fields topic_of_interest,service_interest,software_interest in Leads tab************************



class Crm(models.Model):
    _inherit = 'crm.lead'

    topic_of_interest_wf_lead = fields.Many2one('topic.of.interest', string='Topic of Interest WF')

    service_interest_lead = fields.Many2many(
        'product.product',
        'res_partner_service_interest_lead_rel',  # Unique table name
        'partner_id', 'product_id',
        string='Service Interest',
        domain=[('detailed_type', '=', 'service')]
    )

    software_interest_lead = fields.Many2many(
        'product.product',
        'res_partner_software_interest_lead_rel',  # Another unique table name
        'partner_id', 'product_id',
        string='Software Interest',
        domain=[('detailed_type', '=', 'software')]
    )

    lead_source_lead = fields.Many2one('utm.medium', string="Lead Source")