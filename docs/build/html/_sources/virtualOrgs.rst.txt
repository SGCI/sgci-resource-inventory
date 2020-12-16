============================================
Virtual Organizations and Unique Identifiers
============================================

Different projects, teams and communities contribute resource definitions to the SGCI Resources
inventory system. These "virtual organizations" have a unique identifier and a corresponding
subdirectory within the data directory. The resource definitions within a
virtual organization's subdirectory are managed by members of that group, in
consultation with SGCI project staff. Examples of virtual organizations
currently contributing resource definitions to this project include the
Airavata API framework, the Tapis framework and the XSEDE project.

Identifiers
===========

The unique identifier associated with a virtual organization (the "virtualOrganizationId") is
a fully qualified domain name (FQDN) controlled by the group;  for example, "xsede.org" for the XSEDE
project, "tapis.io" for Tapis, etc. Within a virtual organization, it is up to that organization to generate an
identifier for each resource that will make it unique. We refer to this as the
"virtualOrganizationResourceId". This could be anything from an internal database
id (e.g., 1, 2, 3, etc.), or a string whose uniqueness is enforced by a database constraint,
to a UUID.

The format for the complete SGCI resource identifier is therefore:

.. code-block:: bash

  resources.sciencegateways.org.<virtualOrganizationId>.<virtualOrganizationResourceId>

For example, for the Stampede2 resource within the Tapis virtual organization, with
virtualOrganizationId "tapis.io", the following id's are all valid:

.. code-block:: bash

    resources.sciencegateways.org.tapis.io.stampede2
    resources.sciencegateways.org.tapis.io.7
    resources.sciencegateways.org.tapis.io.04ea2969-f450-48db-a7ce-df69c761dbf4