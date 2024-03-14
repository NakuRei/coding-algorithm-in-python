from typing import Any, Callable, TypeVar, cast, Optional
import functools
import time

F = TypeVar("F", bound=Callable[..., Any])


def timer(
    func: Optional[F] = None,
    /,
    *,
    callback: Optional[F] = None,
) -> Callable[..., Any]:
    if func is None:
        return functools.partial(timer, callback=callback)

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time_ms = (end_time - start_time) * 1000.0
        if callback:
            callback(elapsed_time_ms)
        else:
            print(f"Time taken by {func.__name__}: {elapsed_time_ms} ms")
        return result

    return cast(F, wrapper)
