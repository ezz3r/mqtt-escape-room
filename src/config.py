from pathlib import Path
from dotenv import dotenv_values


class Settings:
    LOCAL_DEVELOPMENT: bool = True
    DB_PASSWORD: str


def get_settings():
    env = dotenv_values(Path(__file__).resolve().parents[1] / ".env")
    settings = Settings()

    for name, value_type in Settings.__annotations__.items():
        value = env.get(name)

        if value is None:
            if hasattr(Settings, name):
                continue
            raise ValueError(f"Missing {name} in .env")

        if value_type is bool:
            value = value.lower() in ("true", "1", "yes", "on")
        else:
            value = value_type(value)

        setattr(settings, name, value)

    return settings


settings = get_settings()