Untagged
========

ansible_setup
^^^^^^^^^^^^^

Run Ansible to gather system information

Inputs:
  None
Outputs:
  ansible_setup - gathered facts about the system

**Tags:** :doc:`untagged`

check-target-output
^^^^^^^^^^^^^^^^^^^

Send information about the services (Docker, Rsync) to a socket

Inputs:
  check_tartget_service_status - status of services
  containerslist               - list of containers
  rsyncinfo                    - Rsync information (path to bin, version)
  dockerinfo                   - docker information
Outputs:
  None (sending the result to a socket)

**Tags:** :doc:`untagged`

create_container
^^^^^^^^^^^^^^^^

Create a new container (but has not started yet) based on an image

Inputs:
  container_directory - directory where a new container is going to be created
  container_name      - name of a new container
  image               - name of the docker image that is going to be used for a new container
  init_bin            - ??
  exposed_ports       - publish a container port(s) to host port(s)
Outputs:
  container_id        - ID of the new container
  error               - any error returned by 'docker create'

**Tags:** :doc:`untagged`

create_container_dir
^^^^^^^^^^^^^^^^^^^^

Create container directory
Inputs:
  container_directory - name of the container directory
Outputs:
  None or exception (in case of error when creating directory)

**Tags:** :doc:`untagged`

create_container_name
^^^^^^^^^^^^^^^^^^^^^

Create a container name based on user input or generate the name with hostname
Inputs:
  user_container_name - (optional) user defined name
  hostnameinfo        - the hostname
Outputs:
  container_name      - user defined name (if user_container_name is provided) or 'container_<hostname>'

**Tags:** :doc:`untagged`

destroy-container
^^^^^^^^^^^^^^^^^

Group actor to remote destroy of a container

Inputs:
  container_name   - name of a container that will be destroyed
  target_host      - hostname of the remote system
  target_user_name - username for the remote system
Outputs:
  None

**Tags:** :doc:`untagged`

port-inspect
^^^^^^^^^^^^

Group actor that scans ports on a target system a print the results out

Inputs:
  host         - hostname of a target system
  scan_options - options for scanning (for more info check `description` in portscan/_actor.yaml)
Outputs:
  Print the port scan result to $LEAPP_ACTOR_OUTPUT

**Tags:** :doc:`untagged`

port-inspect-output
^^^^^^^^^^^^^^^^^^^

Print port scan output

Inputs:
  port_scan_result - scanned port list
Outputs:
  Print the port scan result to $LEAPP_ACTOR_OUTPUT

**Tags:** :doc:`untagged`

port-mapping
^^^^^^^^^^^^

Group actor that scan ports on source and target system, create an port mapping and print out
the result of port mapping

Inputs:
  source_host            - source system hostname
  target_host            - target system hostname
  tcp_ports_user_mapping - user ports mapping
  excluded_tcp_ports     - excluded ports mapping
Outputs:
  Print the port mapping to $LEAPP_ACTOR_OUTPUT

**Tags:** :doc:`untagged`

port-mapping-output
^^^^^^^^^^^^^^^^^^^

Print port mapping to an output

Inputs:
  exposed_ports - list of exposed ports
Outputs:
  Print the port mapping to $LEAPP_ACTOR_OUTPUT

**Tags:** :doc:`untagged`

portmap
^^^^^^^

Map source system ports to the target system ports according to user ports mapping (user can exclude some port(s)) or using default mapping port(s) (SSH 22/tcp -> 9022/tcp for now only)

Inputs:
  source_system_ports     - the ports on source machine
  target_system_ports     - the ports on target machine
  tcp_ports_user_mapping  - user ports mapping
  excluded_tcp_ports      - excluded ports mapping
Outputs:
  exposed_ports           - final ports mapping

**Tags:** :doc:`untagged`

portscan
^^^^^^^^

Scan ports on a system

Inputs:
  host             - hostname or IP
  scan_options     - shallow_scan - 'nmap -sS' if option is set to `true`,
                                    otherwise 'nmap -sV' (default: false)
                     force_nmap   - on the localhost, force using 'nmap' (if true),
                                    otherwise use 'netstat' (default: false)
                     port_range   - specify port range to scan
Outputs:
  port_scan_result - ports on a system

**Tags:** :doc:`untagged`

post_configure_upstart
^^^^^^^^^^^^^^^^^^^^^^

Blacklist upstart services in container directory

Inputs:
  container_directory       - name of the containter directory
  upstart_service_blacklist - services to blacklist
Outputs:
  None

**Tags:** :doc:`untagged`

remote-destroy-container
^^^^^^^^^^^^^^^^^^^^^^^^

Delete a container on the target system

Inputs:
  target_host      - target system hostname
  target_user_name - username on target system
  container_name   - container name to delete
Outputs:
  None (Deleted container)

**Tags:** :doc:`untagged`

remote-target-check
^^^^^^^^^^^^^^^^^^^

Collect information about Docker, Rsync and containers list on a target system

Inputs:
  target_host      - target system hostname
  target_user_name - username on target system
Outputs:
  containerslist   - list of containers on target system
  rsyncinfo        - collected Rsync information
  dockerinfo       - collected Docker information

**Tags:** :doc:`untagged`

remote-target-check-group
^^^^^^^^^^^^^^^^^^^^^^^^^

Group actor that checks services (like Docker, Rsync) on a target system
and send the result information about the services to a socket

Inputs:
  check_target_service_status - status of services
  target_host                 - target system hostname
  target_user_name            - username on target system
Outputs:
  rsyncinfo                   - collected information about Rsync
  dockerinfo                  - collected information about Docker
  containerslist              - list of the container on a target system

**Tags:** :doc:`untagged`

set_container_directory
^^^^^^^^^^^^^^^^^^^^^^^

Set directory path for a container

Inputs:
  container_name      - name of a container
Outputs:
  container_directory - container directory full path

**Tags:** :doc:`untagged`

simple-actor
^^^^^^^^^^^^

This is a simple actor example

**Tags:** :doc:`untagged`

source_portscan
^^^^^^^^^^^^^^^

Scan ports on source system

Inputs:
  source_host         - source system hostname
Outputs:
  source_system_ports - found ports on source system

**Tags:** :doc:`untagged`

start_container
^^^^^^^^^^^^^^^

Start container with given name

Inputs:
  container_name  - name of the container (must be existing one?)
  start_container - ??
Outputs:
  None (starting the conainer)

**Tags:** :doc:`untagged`

