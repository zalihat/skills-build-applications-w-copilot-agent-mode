# Add MongoDB database connection
DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "octofit_db",
    }
}

# Enable CORS
INSTALLED_APPS += ["corsheaders", "octofit_tracker"]
MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
CORS_ALLOW_HEADERS = ["*",]

# Allow all hosts
ALLOWED_HOSTS = ["*"]