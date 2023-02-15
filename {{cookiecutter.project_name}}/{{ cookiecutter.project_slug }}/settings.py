from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Settings class for the otp_service.
    """

    DATABASE_URL: str = "mongodb://localhost:27017"
    SERVICE_NAME: str = "{{ cookiecutter.project_slug }}"
    CERBOS_URL: str = "http://localhost:3592"
    CERBOS_POLICY_VERSION: str = "default"


def get_settings() -> Settings:
    """
    Returns the settings object.
    """
    return Settings()
