from subprocess import Popen, DEVNULL, PIPE

class Localtunnel:
    def __init__(self, port, domain, destination):
        self.port = port
        self.subdomain, *host = domain.split(".")
        self.host = ".".join(host)
        self.destination = destination
        
        self.process = None
        self.public_url = None

    def is_running(self):
        return self.process is not None

    def start(self):
        if self.is_running():
            return

        command = ["lt", "-p", str(self.port), "-h", "https://" + self.host, "-s", self.subdomain, "-l", self.destination]
        self.process = Popen(command, stdout=PIPE, stderr=DEVNULL)
        self.public_url = self.process.stdout.peek().decode().strip().split()[-1]
        return self.public_url

    def stop(self):
        if not self.is_running():
            return

        self.process.kill()
        self.process = None
        self.public_url = None
