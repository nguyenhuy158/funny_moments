+++
date = "2025-07-22T14:50:17+07:00"
draft = false
title = 'Odoo Hide Column in Tree'
description = ""
slug = ""
authors = [ ]
tags = [ odoo, xml, tree ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++

```xml
<field name="line_ids">
    <tree>
        <field name="date_register" attrs="{'column_invisible':[('parent.field_in_parent_record', '=', True)]}"/>
    </tree>
</field>
```