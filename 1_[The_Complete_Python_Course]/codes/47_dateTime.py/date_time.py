from datetime import datetime, timezone

# naive
print(datetime.now())
# aware 
print(datetime.now(timezone.utc))
