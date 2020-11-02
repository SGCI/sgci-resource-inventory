===================================================
Storage Resource Object
===================================================

The Storage Resource Object is used to describe storage properties of the resource. All resources in the SGCI Resource Catalog are assumed to provide storage facilities, and as such, all resource descriptions must include values for the storage properties.

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

.. literalinclude :: ../../data/posix-storages.json
  :language: javascript
