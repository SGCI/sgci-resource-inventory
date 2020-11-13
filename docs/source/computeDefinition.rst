===================================================
Compute Resource Object
===================================================

.. jsonschema:: ../../schema/resources-schema.json#/definitions/computeDefinition

---------------------------------------------------
Connection Object / connectionDefinition
---------------------------------------------------

.. jsonschema:: ../../schema/resources-schema.json#/definitions/connectionDefinition
  :lift_description: True

---------------------------------------------------
Batch System Object / batchSystemDefinition
---------------------------------------------------

.. jsonschema:: ../../schema/resources-schema.json#/definitions/batchSystemDefinition
  :lift_description: True

---------------------------------------------------
fork System Object / forkSystemDefinition
---------------------------------------------------

.. jsonschema:: ../../schema/resources-schema.json#/definitions/forkSystemDefinition
  :lift_description: True

---------------------------------------------------
Examples
---------------------------------------------------

**SDSC Comet Cluster**

.. literalinclude :: ../../data/comet.sdsc.xsede.json
  :language: javascript


**TACC Stampede2 Cluster**

.. literalinclude :: ../../data/stampede2.tacc.xsede.json
  :language: javascript
