+++
date = "2025-07-22T14:50:13+07:00"
draft = false
title = 'Odoo Hide Column in Tree'
description = "Use column_invisible in Odoo tree views to hide a column based on the parent record state."
slug = "odoo-hide-column-in-tree"
authors = []
tags = [ "odoo", "xml", "tree" ]
categories = []
externalLink = ""
series = []
images = []
+++

```xml
<field name="line_ids">
    <tree>
        <field name="date_register" attrs="{'column_invisible':[('parent.field_in_parent_record', '=', True)]}"/>
    </tree>
</field>
```
