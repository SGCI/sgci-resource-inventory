===================================================
Outage Object
===================================================

The ``outageDefinitionList`` attribute is made up of 0 or more ``outageDefinition`` objects. Each ``outageDefinition``
describes properties for one current or future outage affecting the resource.

.. jsonschema:: ../../schema/resources-schema.json#/definitions/outageDefinition

---------------------------------------------------
Examples
---------------------------------------------------

**XSEDE Comet Resource**

.. literalinclude :: ../../data/comet.sdsc.xsede.json
  :language: javascript
