# -*- coding: utf-8 -*-
from openerp import models, fields
class LibraryBook(models.Model) :
    _name = 'library.book'
    _description = 'Library Book'
    _order = 'date_release desc, name'
    _rec_name = 'short_name'
    name = fields.Char('Title', required=True)
    short_name = fields.Char(
        string='Short Title',
        size=100, # For Char only
        translate=False #also for Text fields
    )
    notes = fields.Text('Internal Notes')
    state = fields.Selection(
        [('draft','Not Available'),
        ('available', 'Available'),
        ('lost','Lost')],
        'State')
    description = fields.Html(
        string='Description',
        #optional :
        sanitize=True,
        strip_style=False,
        translate=False,
    )
    cover = fields.Binary('Book Cover')
    date_release = fields.Date('Release Date')
    out_of_print = fields.Boolean('Out of Print?')
    date_updated = fields.Datetime('Last Updated')
    pages = fields.Integer(
        string='Number of Pages',
        default=0,
        help='Total book page count',
        groups='base.group_user',
        states={'cancel': [('readonly', True)]},
        copy=True,
        index=False,
        readonly=False,
        required=False,
        company_dependent=False,
    )
    reading_rating = fields.Float(
        'Reader Average Rating' ,
        (14, 4), #Optional precision (total, decimals),
    )
    author_ids = fields.Many2many('res.partner',string='Authors')
