Introduction
===========

The *Links* tab on the *Group* page provides links related to the group. Often,
these will be links concerning the neighborhood that a group represents, or
events and references for a commmunity of practice group. This product supplies
'the change page'_ that allows the contents of the tab to be altered. This
product especially copies the *Change the About Tab* page defined in
``gs.group.about``.

The Change Page
===============

The *Change the Links Tab" page is a simple form that changes the 
``related_links`` property of the group. This module provides the *Change* page
itself and the link from the *Properties* list in the *Admin* tab on the
*Group* page to the *Change* page.

Group Admin Link
================

In addition to defining the Change Links page, this egg also defines a viewlet
for the group admin section of a group. At the moment the group page that is
defined by gs.skin.ogn.edem does not use viewlets to create its admin section
(unlike the default GroupServer group home page), so this viewlet is actually
not used. However, in the future it should be.
