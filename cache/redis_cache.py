import json
from cache.redis_client import redis_client
def get_cache(key:str):
    value=redis_client.get(key)
    if value is None:
        return None
    return json.loads(value)

def set_cache(key:str,value,expire:int=60):
    redis_client.set(
        key,
        json.dumps(value),
        ex=expire
    )

def delete_cache(key:str):
    redis_client.delete(key)

def delete_cache_pattern(pattern:str):
    keys=redis_client.keys(pattern)
    if keys:
        redis_client.delete(*keys)