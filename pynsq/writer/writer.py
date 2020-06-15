import json
import urllib3
import logging
import ssl

logger = logging.getLogger(__name__)


class Writer:
    def __init__(self, server, topic, opts):
        if not server.startswith("https://"):
            server = "https://" + server
        self.server = server
        self.http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED",
                                        ca_certs=opts["ca_certs"],
                                        cert_file=opts["certfile"],
                                        key_file=opts["keyfile"])
        self.topic = topic

    def write(self, data):
        url = self.server + "/pub?topic=" + self.topic
        response = self.http.request(
            "POST",
            url,
            body=data,
            headers={"Content-Type": "application/json"})
        logger.debug("HTTP respose: {}".format(response))
        return response


if __name__ == "__main__":

    opts = {
        "cert_reqs": ssl.CERT_REQUIRED,
        "keyfile": "../client-key.pem",
        "certfile": "../client-cert.pem",
        "ca_certs": "../ca-cert.pem",
    }
    nsqWriter = Writer("10.77.134.33:4152", "topic%23ephemeral", opts)
    N = 2000
    for i in range(N):
        nsqWriter.write("hello")
