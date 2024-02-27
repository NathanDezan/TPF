import docker

class ContainerInfoFetcherFactory:
    @staticmethod
    def create_fetcher():
        return ContainerInfoFetcher()
    
class ContainerInfoFetcher:
    """
    Class responsible for fetching information about Docker containers.
    """

    def fetch_info(self):
        """
        Fetches information about Docker containers and returns a dictionary with the container info.

        Returns:
            dict: A dictionary containing the container information.
        """
        client = docker.from_env()
        containers = client.containers.list()
        list_address_ports = []

        for container in containers:
            ports_info = container.attrs['NetworkSettings']['Ports']

            for port, mappings in ports_info.items():
                if mappings is not None:
                    for mapping in mappings:
                        if mapping['HostIp'] != '::':
                            temp_str = f"Host IP: {mapping['HostIp']}, Port: {port}, Host Port: {mapping['HostPort']}"
                            list_address_ports.append(temp_str)

            container_info = {
                "Nome da imagem": container.image.tags[0],
                "Status": container.status,
                "Endereço e portas utilizadas": list_address_ports
            }

        return container_info