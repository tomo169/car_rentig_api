from database import SessionLocal
from fastapi import HTTPException, status
from redis_client import redis_client

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def rate_limiter(client_id: str, max_requests: int, period: int):
    def limit():
        key = f"rate_limit:{client_id}"
        current = redis_client.get(key)
        
        if current is None:
            redis_client.set(key, 1, ex=period)
        elif int(current) < max_requests:
            redis_client.incr(key)
        else:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Too many requests"
            )
    
    return limit