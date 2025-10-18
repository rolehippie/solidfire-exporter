import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_running_and_enabled(host):
    svc = host.service("solidfire-exporter")
    assert svc.is_running
    assert svc.is_enabled


def test_server_socket(host):
    assert host.socket("tcp://127.0.0.1:9987").is_listening
