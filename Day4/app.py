from config import DevelopmentConfig, ProductionConfig, TestingConfig

def create_app(config_class):
    app = {} # This would be your Flask or any other app instance in a real scenario
    app['config'] = config_class
    return app

# Example of using different configurations
if __name__ == "__main__":
    env = "development" # Change this to 'production' or 'testing' as needed

    if env == 'production':
        app = create_app(ProductionConfig)
    elif env == 'testing':
        app = create_app(TestingConfig)
    else:
        app = create_app(DevelopmentConfig)

    # Access configuration settings
    print(f"DEBUG: {app['config'].DEBUG}")
    print(f"DATABASE_URI: {app['config'].DATABASE_URI}")
    print(f"SECRET_KEY: {app['config'].SECRET_KEY}")
    print(f"API_KEY: {app['config'].API_KEY}")
