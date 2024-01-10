terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.0.2"
    }
  }
}

provider "docker" {}

resource "docker_image" "hello" {
  name         = "nginxdemos/hello"
  pull_triggers = ["always"]
}

resource "docker_container" "webserver" {
  name  = "hello-container"
  image = docker_image.hello.image_id
  must_run = true
    command = [
    "tail",
    "-f",
    "/dev/null"
	]
  ports {
    internal = 80
    external = 8080
  }
}
