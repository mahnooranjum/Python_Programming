# A basic Kafka setup on Ubuntu 

## Requirements: 

| Kafka | Can download and install using Kafka quickstart |
| ----------- | ----------- |
| Zookeeper | Already comes with the Kafka quickstart archive | 
| Kafkadrop | Can be compiled on your own, or use the official docker image | 
| Faker | To generate fake data and publish to a topic |
| Kafka_Python | To make producers and consumers in python |
 
Use the docker compose file to setup the Kafka server and the Kafkadrop UI

```
sudo docker-compose up 
```


To kill a process, see the containers by

```
sudo docker ps 
```

To stop a container 

```
sudo docker stop HEX_ID_CONTAINER 
```

## References 

- https://github.com/obsidiandynamics/kafdrop/blob/master/docker-compose/kafka-kafdrop/docker-compose.yaml

- https://ep.gnt.md/index.php/how-to-install-and-configure-apache-kafka-web-ui-docker/

- https://www.youtube.com/channel/UCCa9UnklA65wsMcVKUhYsjQ

