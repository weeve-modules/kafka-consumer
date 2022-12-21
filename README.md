# Kafka Consumer

|                |                                       |
| -------------- | ------------------------------------- |
| Name           | Kafka Consumer                           |
| Version        | v1.0.0                                |
| DockerHub | [weevenetwork/kafka-consumer](https://hub.docker.com/r/weevenetwork/kafka-consumer) |
| Authors        | Jakub Grzelak                    |

- [Kafka Consumer](#kafka-consumer)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

Consumer to connect with Apache Kafka and input data from the cluster. The module uses `utf-8` decoding for value deserializer.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                 | Environment Variables     | Type     | Description                                              |
| -------------------- | ------------------------- | -------- | -------------------------------------------------------- |
| Topic    | TOPIC         | string   | Kafka topic to subscribe to.            |
| Bootstrap Servers    | BOOTSTRAP_SERVERS         | string   | List of comma (,) separated Kafka bootstrap servers that the consumer should contact to bootstrap initial cluster metadata.            |
| Client ID    | CLIENT_ID         | string   | A name for this client. This string is passed in each request to servers and can be used to identify specific server-side log entries that correspond to this client.            |
| Group ID    | GROUP_ID         | string   | The name of the consumer group to join for dynamic partition assignment, and to use for fetching and committing offsets.            |
| Auto Offset Reset    | AUTO_OFFSET_RESET         | string   | A policy for resetting offsets 'earliest' will move to the oldest available message, 'latest' will move to the most recent.            |
| Enable Auto Commit    | ENABLE_AUTO_COMMIT         | boolean   | If True, the consumer offset will be periodically committed in the background.            |


### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (INGRESS, PROCESS, EGRESS)  |
| EGRESS_URLS           | string | HTTP ReST endpoint for the next module         |

## Dependencies

```txt
requests
kafka-python
```

## Input

Input to this module is data stored on Kafka cluster.

## Output

Output to this module is data stored on Kafka cluster in JSON format.
