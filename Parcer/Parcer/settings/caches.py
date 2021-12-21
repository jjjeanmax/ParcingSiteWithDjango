from .secret import get_secret


#################################
# Кэширование
#################################

REDIS_HOST = get_secret(section='REDIS', setting='HOST')
REDIS_PORT = get_secret(section='REDIS', setting='PORT')
REDIS_CACHE_DB = get_secret(section='REDIS', setting='CACHE_DB')

SAVE_HOST = get_secret(section='SAVE', setting='HOST')
SAVE_PORT = get_secret(section='SAVE', setting='PORT')
SAVE_CACHE_DB = get_secret(section='SAVE', setting='CACHE_DB')
SAVE_TTL = get_secret(section='SAVE', setting='TTL')


def cache_key_maker(key, key_prefix, version):
    """Убирает приставку (префикс) и версию у redis ключа"""
    return key


def cache_custom_reverse_key(key):
    """Костыль чтоб работал django_redis keys('*') без версионности и префикса"""
    return key


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://{}:{}/{}'.format(
            REDIS_HOST, REDIS_PORT, REDIS_CACHE_DB
        ),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    # кэш для хранения данных устройств
    # TODO: Подумать над возвращением префикса и версионности
    #  (синхронизировать redis настройки в async mqtt logger и django)
    #  чтоб использовать полный функционал django-redis
    'save': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{SAVE_HOST}:{SAVE_PORT}/{SAVE_CACHE_DB}',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            # Используем последнюю версию сериализатора
            'PICKLE_VERSION': 5
        },
        'TIMEOUT': SAVE_TTL,
        'KEY_FUNCTION': 'Parcer.settings.caches.cache_key_maker',
        'REVERSE_KEY_FUNCTION': 'Parcer.settings.caches.cache_custom_reverse_key',
    },
}
