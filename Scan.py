from scapy.sendrecv import sr
from scapy.layers.inet import IP, ICMP
from dataclasses import dataclass
from Configuration import Config, Host


@dataclass
class ScanResults:
    successful: list[Host]
    failed: list[Host]
    summary: str


class Scanner:
    def __init__(self, cfg: Config):
        self.__cfg = cfg

    def host_icmp_scan(self) -> dict[str, bool]:
        results = {}
        print("Starting ICMP scan...")
        hosts = self.__cfg.get_hosts()
        if hosts and len(hosts) > 0:
            for host in hosts:
                print(f"Scanning {host.hostname}...")
                packet = IP(dst=host.hostname) / ICMP()
                response = sr(packet, timeout=self.__cfg.timeout, verbose=False)
                if len(response[0]) > 0:
                    results[host.hostname] = True
                else:
                    results[host.hostname] = False
        print("ICMP scan completed.")
        return results