Check_Target
============

check_target
^^^^^^^^^^^^

Check the target system if it has sufficient tools and its statuses

Inputs:
  rsyncinfo      - status about rsync
  dockerinfo     - status about docker
  containerslist - list of containers
Outputs:
  targetinfo     - result of the statuses of the tools on a target system

**Tags:** :doc:`check_target`, :doc:`depsolver`

docker_info
^^^^^^^^^^^

Collect information about Docker on the system

Inputs:
  None
Outputs:
  dockerinfo - collected Docker information (like Docker bin path, its systemd state and general available Docker information)

**Tags:** :doc:`check_target`, :doc:`depsolver`

rsync_info
^^^^^^^^^^

Collect information about Rsync on a system 

Inputs:
  None
Outputs:
  rsyncinfo - collected information about Rsync

**Tags:** :doc:`check_target`, :doc:`depsolver`

