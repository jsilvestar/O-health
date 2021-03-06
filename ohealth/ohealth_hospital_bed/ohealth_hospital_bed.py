# -*- coding: utf-8 -*-
#/#############################################################################
#
#    HITSF
#    
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#/#############################################################################
from osv import osv
from osv import fields


class OHealthHospitalBed(osv.Model):
    _name = 'ohealth.hospital.bed'

    _columns = {
        'name': fields.many2one('product.product', string='Bed',required=True,
                                help='Bed Number'),
        'bed_type': fields.selection([
            ('gatch', 'Gatch Bed'),
            ('electric', 'Electric'),
            ('stretcher', 'Stretcher'),
            ('low', 'Low Bed'),
            ('low_air_loss', 'Low Air Loss'),
            ('circo_electric', 'Circo Electric'),
            ('clinitron', 'Clinitron'),
        ], string='Bed Type',required=True),
        'telephone_number': fields.char(size=256, string='Telephone Number', 
                                        help='Telephone number / Extension'),
        'state': fields.selection([
            ('free', 'Free'),
            ('reserved', 'Reserved'),
            ('occupied', 'Occupied'),
            ('na', 'Not available'),
        ], string='Status',readonly=True),
        'ward': fields.many2one('ohealth.hospital.ward', string='Ward', 
                                 help='Ward or room'),
        'extra_info': fields.text(string='Extra Info'),
    }

OHealthHospitalBed()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
