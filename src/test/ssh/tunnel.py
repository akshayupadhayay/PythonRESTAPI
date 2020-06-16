import logging


class tunnel:

    def __init__(self, host, username, key_file, remote_port, host_port=nat_ssh_port_forwarding):
        logger = logging.getLogger('sshtunnel')
        logger.setLevel(logging.ERROR)
    
        try:
            self._server = SSHTunnelForwarder((host, host_port),
                                              ssh_username=username, ssh_private_key=key_file,
                                              remote_bind_address=('127.0.0.1', remote_port), logger=logger)
        except sshtunnel.BaseSSHTunnelForwarderError as e:
            raise self.TunnelException(e)

    def TunnelException(self, e):
        pass