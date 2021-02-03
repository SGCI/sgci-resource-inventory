===================================================
Storage Resource Object
===================================================

The ``storageDefinitionList`` attribute is made up of 1 or more ``storageDefinition`` objects. Each ``storageDefinition``
describes properties for interacting with one storage capability the resource provides. All resources in the SGCI
Resource Catalog are assumed to provide storage facilities, and as such, all resource descriptions must include
at least one ``storageDefinition`` object within the ``storageDefinitionList`` attribute.

.. jsonschema:: ../../schema/resources-schema.json#/definitions/storageDefinition
  :lift_description: True

---------------------------------------------------
Connection Object / connectionDefinition
---------------------------------------------------

.. jsonschema:: ../../schema/resources-schema.json#/definitions/connectionDefinition
  :lift_description: True

---------------------------------------------------
File System Object / fileSystemDefinition
---------------------------------------------------

.. jsonschema:: ../../schema/resources-schema.json#/definitions/fileSystemDefinition
  :lift_description: True

---------------------------------------------------
Directory Path Object / dirPath
---------------------------------------------------

.. jsonschema:: ../../schema/resources-schema.json#/definitions/dirPath
  :lift_description: True

---------------------------------------------------
Examples
---------------------------------------------------

**SCIGAP Development Storage**

.. literalinclude :: ../../data/scigap-dev.iu.storage.json
  :language: javascript
