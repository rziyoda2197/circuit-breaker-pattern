import time
import random

class CircuitBreaker:
    def __init__(self, timeout=5, max_attempts=3):
        self.timeout = timeout
        self.max_attempts = max_attempts
        self.attempts = 0
        self.last_attempt_time = 0
        self.is_open = False

    def call(self, func):
        if self.is_open:
            return None

        if self.attempts >= self.max_attempts:
            self.is_open = True
            return None

        start_time = time.time()
        result = func()
        end_time = time.time()

        if result is None:
            self.attempts += 1
            self.last_attempt_time = end_time
            if end_time - start_time < self.timeout:
                time.sleep(self.timeout - (end_time - start_time))
            return self.call(func)

        self.attempts = 0
        return result

def external_api_call():
    # Simulate external API call
    if random.random() < 0.5:
        return "API response"
    else:
        return None

circuit_breaker = CircuitBreaker()

while True:
    result = circuit_breaker.call(external_api_call)
    if result is not None:
        print(result)
    else:
        print("Circuit is open")
        time.sleep(10)
```

Kodda Circuit Breaker klassi mavjud bo'lib, u external API call qilish uchun mo'ljallangan. Uning vazifasi API call qilishdan oldin circuit breakerni ochish yoki yopishni nazorat qilishdir. Agar API call qilishda muvaffaqiyat qozonmagan bo'lsa, circuit breaker ochiladi va keyinroq qayta urinishlar uchun vaqt beriladi. Agar API call qilishda muvaffaqiyat qozonmagan bo'lsa, circuit breaker ochilib qoladi va qayta urinishlar uchun vaqt beriladi.
