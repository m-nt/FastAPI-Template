from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Settings class for the otp_service.
    """

    DATABASE_URL: str = "mongodb://localhost:27017"
    SERVICE_NAME: str = "{{ cookiecutter.project_slug }}"
    ENV_MODE: str = "dev"


def get_settings() -> Settings:
    """
    Returns the settings object.
    """
    return Settings()
