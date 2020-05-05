# concatenate
テキストファイルに適当な整形をほどこして連結したりするスクリプト

# DockerHub

- [515hikaru/concatenate](https://hub.docker.com/r/515hikaru/concatenate)

# Use Cases

## Local

```
docker run --rm -v $(pwd):/work 515hikaru/concatenate python /app/concatenate.py /work/src > main.txt
```

## GitLab CI

```yaml
image: 515hikaru/concatenate:latest

build:
  script:
    - python3 /app/concatenate.py src > main.txt
```

## GitHub Actions

Probably work: [515hikaru-sandbox/create-actions-test: actions をなにか作るかもしれない](https://github.com/515hikaru-sandbox/create-actions-test)

# License

MIT
