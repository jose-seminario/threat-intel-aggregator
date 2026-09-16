import re
class DetectorIOC:

    patterns = {
            'ip':     re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'),
            'domain': re.compile(r'^[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$'),
            'hash':   re.compile(r'^[a-fA-F0-9]{32}$|^[a-fA-F0-9]{40}$|^[a-fA-F0-9]{64}$')
    }
    def detectar(self, ioc):


        for ioc_type, pattern in self.patterns.items():
            if pattern.match(ioc):
                return ioc_type

        return "Desconocido"
