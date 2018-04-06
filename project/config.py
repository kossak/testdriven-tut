class BaseConfig:
    """Base configuration"""
    TESTING = False


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    pass
