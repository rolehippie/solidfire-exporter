# solidfire-exporter

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/solidfire-exporter)
[![General Workflow](https://github.com/rolehippie/solidfire-exporter/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/solidfire-exporter/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/solidfire-exporter/actions/workflows/docs.yml/badge.svg)](https://github.com/rolehippie/solidfire-exporter/actions/workflows/docs.yml)
[![Galaxy Workflow](https://github.com/rolehippie/solidfire-exporter/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/solidfire-exporter/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/solidfire-exporter)](https://github.com/rolehippie/solidfire-exporter/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.solidfire__exporter-blue)](https://galaxy.ansible.com/rolehippie/solidfire_exporter)

Ansible role to install and configure a Prometheus exporter for Solidfire.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [solidfire_exporter_endpoint](#solidfire_exporter_endpoint)
  - [solidfire_exporter_image](#solidfire_exporter_image)
  - [solidfire_exporter_insecure](#solidfire_exporter_insecure)
  - [solidfire_exporter_network](#solidfire_exporter_network)
  - [solidfire_exporter_password](#solidfire_exporter_password)
  - [solidfire_exporter_publish](#solidfire_exporter_publish)
  - [solidfire_exporter_pull_image](#solidfire_exporter_pull_image)
  - [solidfire_exporter_username](#solidfire_exporter_username)
  - [solidfire_exporter_version](#solidfire_exporter_version)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`

## Default Variables

### solidfire_exporter_endpoint

Endpoint to access Solidfire

#### Default value

```YAML
solidfire_exporter_endpoint: https://127.0.0.1/json-rpc/11.3
```

### solidfire_exporter_image

Docker image to use and run

#### Default value

```YAML
solidfire_exporter_image: ghcr.io/mjavier2k/solidfire-exporter:{{ 
  solidfire_exporter_version }}
```

### solidfire_exporter_insecure

Skip certificate verification

#### Default value

```YAML
solidfire_exporter_insecure: true
```

### solidfire_exporter_network

A Docker network to assign the container

#### Default value

```YAML
solidfire_exporter_network:
```

### solidfire_exporter_password

Password to access Solidfire

#### Default value

```YAML
solidfire_exporter_password:
```

### solidfire_exporter_publish

Publish the Docker image on thet binding

#### Default value

```YAML
solidfire_exporter_publish: 9987
```

### solidfire_exporter_pull_image

Pull image as part of the tasks

#### Default value

```YAML
solidfire_exporter_pull_image: true
```

### solidfire_exporter_username

Username to access Solidfire

#### Default value

```YAML
solidfire_exporter_username:
```

### solidfire_exporter_version

Version of the Docker image

#### Default value

```YAML
solidfire_exporter_version: v0.6.7
```

## Discovered Tags

**_solidfire-exporter_**

## Dependencies

- [rolehippie.docker](https://github.com/rolehippie/docker)
- [community.docker](https://github.com/ansible-collections/community.docker)

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
