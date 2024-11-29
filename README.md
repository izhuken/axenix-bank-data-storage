# Развертывание приложений

### Требования:
1. cluster config
2. kubectl
3. кластер k8s
4. в кластере использовался traefik ingress 
5. сервер с белым ip и установленым Docker

| В примере показывается развертывание из корневой директории проекта
### Backend
1. Конфигурации
```
kubectl apply -f ./.kube/cfg/secrets.yaml
```
2. Поднятие инфраструктуры
```
kubectl apply -f ./.kube/infrastructure/traefik.yaml
kubectl apply -f ./.kube/infrastructure/postgre.yaml
kubectl apply -f ./.kube/infrastructure/zookeeper.yaml
kubectl apply -f ./.kube/infrastructure/kafka.yaml
```
3. Поднятие backend сервисов
```
kubectl apply -f ./.kube/service/action-service.yaml
kubectl apply -f ./.kube/service/event-service.yaml
kubectl apply -f ./.kube/service/point-service.yaml
kubectl apply -f ./.kube/service/task-service.yaml
kubectl apply -f ./.kube/service/user-service.yaml
kubectl apply -f ./.kube/service/notification-service.yaml
```

### Frontend
1. Собрать image
2. Поднять вместе с traefik в compose
```
docker compose -f docker-compose.admin.yaml up -d --build
```
