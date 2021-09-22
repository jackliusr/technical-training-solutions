# -*- coding: utf-8 -*-
# More info at https://www.odoo.com/documentation/master/reference/module.html

{
    "name": "Real Estate",
    "depends": [
        "base",
        "web",
    ],
    "Category": "estate",
    "data": [
        "data/estate.property.type.csv",
        "security/security.xml",
        "security/ir.model.access.csv",      
        "views/estate_property_offer_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_views.xml",
        "views/res_users_views.xml",
        "views/estate_menus.xml",
    ],
    "demo":[
       "demo/property_demo.xml",
       "demo/property_offer_demo.xml"  
    ],
    "application": True,
}
