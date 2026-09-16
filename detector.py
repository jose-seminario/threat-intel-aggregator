import re
class DetectorIOC:

    patterns = {
            'ip': re.compile(r'^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$'),
            'domain': re.compile(r'^[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$'),
            'hash':   re.compile(r'^[a-fA-F0-9]{32}$|^[a-fA-F0-9]{40}$|^[a-fA-F0-9]{64}$')
    }
    def detectar(self, ioc):


        for ioc_type, pattern in self.patterns.items():
            if pattern.match(ioc):
                return ioc_type

        return "Desconocido"
