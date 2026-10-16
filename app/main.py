
def get_app_info():
    return {
        "name": "CloudCart",
        "version": "1.0.0",
        "environment": "local"
    }


def health_check():
    app_info = get_app_info()

    if app_info["name"] and app_info["version"]:
        return {
            "status": "healthy",
            "message": "Application configuration is valid."
        }

    return {
        "status": "unhealthy",
        "message": "Application configuration is incomplete."
    }


def main():
    app_info = get_app_info()
    health = health_check()

    print("=== CloudCart Application ===")
    print(f"Name: {app_info['name']}")
    print(f"Version: {app_info['version']}")
    print(f"Environment: {app_info['environment']}")
    print(f"Health: {health['status']}")
    print(f"Health details: {health['message']}")


if __name__ == "__main__":
    main()
