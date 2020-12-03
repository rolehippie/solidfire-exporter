# solidfire-exporter

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/solidfire-exporter) [![Build Status](https://img.shields.io/drone/build/rolehippie/solidfire-exporter/master?logo=drone)](https://cloud.drone.io/rolehippie/solidfire-exporter) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/solidfire-exporter)](https://github.com/rolehippie/solidfire-exporter/blob/master/LICENSE) 

Ansible role to install and configure a Prometheus exporter for Solidfire. 

## Sponsor 

[![Proact Deutschland GmbH](https://proact.eu/wp-content/uploads/2020/03/proact-logo.png)](https://proact.eu) 

Building and improving this Ansible role have been sponsored by my employer **Proact Deutschland GmbH**.

## Table of content

* [Default Variables](#default-variables)
  * [solidfire_exporter_endpoint](#solidfire_exporter_endpoint)
  * [solidfire_exporter_image](#solidfire_exporter_image)
  * [solidfire_exporter_insecure](#solidfire_exporter_insecure)
  * [solidfire_exporter_network](#solidfire_exporter_network)
  * [solidfire_exporter_password](#solidfire_exporter_password)
  * [solidfire_exporter_publish](#solidfire_exporter_publish)
  * [solidfire_exporter_username](#solidfire_exporter_username)
  * [solidfire_exporter_version](#solidfire_exporter_version)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

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
solidfire_exporter_image: mjavier/solidfire-exporter:{{ solidfire_exporter_version
  }}
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
solidfire_exporter_version: latest
```

## Dependencies

* [rolehippie.docker](https://github.com/rolehippie/docker)

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
