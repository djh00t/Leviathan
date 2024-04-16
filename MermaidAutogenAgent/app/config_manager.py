import os
import yaml
from fastapi import FastAPI
from starlette.middleware.reload import StatReload
from starlette.middleware.reload import StatReload

class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance.load_config()
        return cls._instance

    def load_config(self):
        with open("config/config.yaml", "r") as f:
            self.config = yaml.safe_load(f)

    @staticmethod
    def get_config():
        return ConfigManager()._instance.config
    
    def setup_app_with_reloader(self, app: FastAPI):
        config = ConfigManager.get_config()
        if config.get("development", False):
            app.add_middleware(StatReload)
            self._override_with_env_variables()

    @staticmethod
    def add_middleware(self, middleware):
        # Add middleware logic here
            self._override_with_env_variables()

    def _override_with_env_variables(self):
        aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        if aws_access_key_id and aws_secret_access_key:
            self.config['aws']['access_key_id'] = aws_access_key_id
            self.config['aws']['secret_access_key'] = aws_secret_access_key
