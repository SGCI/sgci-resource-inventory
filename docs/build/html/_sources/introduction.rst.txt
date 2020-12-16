===================================================
Introduction to SCGI Inventory
===================================================


---------------------------------------------------
Version
---------------------------------------------------
This is version 0.1.0 of the SGCI Resource Description Specification schema. <LICENSE INFO>

---------------------------------------------------
Introduction
---------------------------------------------------

The user-facing components of the Cyberinfrastructure (CI) ecosystem, science gateways and scientific workflow systems,
share a common need of interfacing with physical resources (storage systems and execution environments) to manage data and execute codes (applications).

However, there is no uniform, platform-independent way to describe either the resources or the applications. To address this, we propose uniform semantics for describing resources and applications that will be relevant to a diverse set of stakeholders.

The SGCI Resource Description Specification provides a standard way for institutions and service providers to describe storage and computing infrastructure broadly available to the research computing and science gateway community. SGCI Resource descriptions provide a foundation for interoperability across gateway components and other cyberinfrastructure software.

The current, initial version of the resource description language focuses on “traditional” HPC and high-throughput storage and computing resources

---------------------------------------------------
Definitions
---------------------------------------------------
<definitions>

---------------------------------------------------
Specification Format
---------------------------------------------------
SGCI resource descriptions are JSON documents that conform to the JSONSchema definition describing a particular version of the SGCI Resource Description Specification.

---------------------------------------------------
Examples
---------------------------------------------------
Here are some first examples.

**SCIGAP Development Storage**

A server or virtual machine providing storage accessible over SSH can be registered as resources with ``"resourceType": "STORAGE"``.
The following example describes the storage used by the SCIGAP framework in its development environment.

.. literalinclude :: ../../data/airavata.apache.org/scigap-dev.json
   :language: javascript


**Carbonate HPC**

Resources providing compute capabilities are registered as resources with ``"resourceType": "COMPUTE"``.
Carbonate is Indiana University's large-memory computer cluster:

.. literalinclude :: ../../data/airavata.apache.org/carbonateHPC.json
   :language: javascript


**TACC Stampede2 Cluster**

In the following example of the TACC Stampede2 supercomputer, we add descriptions of the partitions (queues).
These are optional but very valuable for science gateway projects.

.. literalinclude :: ../../data/tapis.io/stampede2-compute.json
  :language: javascript


**SDSC Comet Cluster**

Our final example is of the SDSC Comet machine:

.. literalinclude :: ../../data/sdsc.edu/comet.json
  :language: javascript



.. |reg|    unicode:: U+000AE .. REGISTERED SIGN

---------------------------------------------------
Integration
---------------------------------------------------

.. image:: ../SGCI.png
   :width: 600

The SCGI Inventory is currently been integrated with Airavata, HUBzero |reg|  , and Tapis. We expect the inventory to be adapted by others soon.

**Links:**

https://github.com/SGCI/sgci-resource-inventory

https://github.com/SGCI/sgci-resource-inventory-cache-service


**Get Involved!**

Issues, Comments, PRs all welcome!

SGCI: help@sciencegateways.org

Email: jstubbs at tacc.utexas.edu, smarru at iu.edu, dmejiapa at purdue.edu
