logging_config = {
    "version": 1,
    "loggers": {
        "": {
            "level": "NOTSET",
            "handlers": ["debug_console_handler"]
        },
        "eye.event_watcher.views.create_schema": {
            "level": "INFO",
            "propagate": "false",
            "handlers": ["info_rotating_file_handler", "error_file_handler" ]
        },
        "eye.event_watcher.views.create_event": {
          "level": "INFO",
            "propagate": "false",
            "handlers": ["info_rotating_file_handler", "error_file_handler" ]
        }
    },
    "handlers": {
        "debug_console_handler": {
            "level": "DEBUG",
            "formatter": "info",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout"
        },
        "info_rotating_file_handler": {
            "level": "INFO",
            "formatter": "info",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "event_watcher.log",
            "mode": "a",
            "maxBytes": 1048576,
            "backupCount": 10
        },
        "error_file_handler": {
            "level": "WARNING",
            "formatter": "error",
            "class": "logging.FileHandler",
            "filename": "event_watcher-error.log",
            "mode": "a"
        }
    },
    "formatters": {
        "info": {
            "format": "%(asctime)s %(levelname)s %(name)s::%(module)s|%(lineno)s:: %(message)s"
        },
        "error": {
            "format": "%(asctime)s %(levelname)s %(name)s %(process)d::%(module)s|%(lineno)s:: %(message)s"
        }
    }

}