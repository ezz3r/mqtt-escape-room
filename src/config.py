# src/config.py
from pathlib import Path


class Settings:
    LOCAL_DEVELOPMENT: bool = True


def get_settings():
    env = {}

    for line in Path(".env").read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.strip().startswith("#"):
            key, value = line.split("=", 1)
            env[key.strip()] = value.strip().strip("'\"")

    settings = Settings()

    for name, value_type in Settings.__annotations__.items():
        value = env[name]

        if value_type is bool:
            value = value.lower() in ("true", "1", "yes", "on")
        else:
            value = value_type(value)

        setattr(settings, name, value)

    return settings


settings = get_settings()