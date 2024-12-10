.PHONY: front
front:
	docker compose -f frontend/docker-compose.yml build --no-cache
	docker compose -f frontend/docker-compose.yml up