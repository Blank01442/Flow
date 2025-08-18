import time
import psutil
import os
from collections import defaultdict
from functools import wraps

class FlowProfiler:
    def __init__(self):
        self.function_calls = defaultdict(int)
        self.function_times = defaultdict(float)
        self.line_times = defaultdict(float)
        self.memory_usage = []
        self.start_time = None
        self.process = psutil.Process(os.getpid())
        
    def start(self):
        """Start profiling"""
        self.start_time = time.time()
        self.initial_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        
    def stop(self):
        """Stop profiling and return results"""
        if self.start_time is None:
            raise Exception("Profiler was not started")
            
        total_time = time.time() - self.start_time
        final_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        
        return {
            'total_time': total_time,
            'function_calls': dict(self.function_calls),
            'function_times': dict(self.function_times),
            'line_times': dict(self.line_times),
            'initial_memory_mb': self.initial_memory,
            'final_memory_mb': final_memory,
            'memory_delta_mb': final_memory - self.initial_memory
        }
        
    def record_function_call(self, func_name):
        """Record a function call"""
        self.function_calls[func_name] += 1
        
    def record_function_time(self, func_name, elapsed_time):
        """Record time spent in a function"""
        self.function_times[func_name] += elapsed_time
        
    def record_line_time(self, line_info, elapsed_time):
        """Record time spent on a line"""
        self.line_times[line_info] += elapsed_time
        
    def record_memory_usage(self, description=""):
        """Record current memory usage"""
        memory_mb = self.process.memory_info().rss / 1024 / 1024  # MB
        self.memory_usage.append({
            'description': description,
            'memory_mb': memory_mb,
            'timestamp': time.time()
        })

def profile_function(func):
    """Decorator to profile a function"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if hasattr(self, 'profiler') and self.profiler:
            func_name = f"{self.__class__.__name__}.{func.__name__}"
            self.profiler.record_function_call(func_name)
            start_time = time.time()
            result = func(self, *args, **kwargs)
            elapsed_time = time.time() - start_time
            self.profiler.record_function_time(func_name, elapsed_time)
            return result
        else:
            return func(self, *args, **kwargs)
    return wrapper

# Global profiler instance
global_profiler = FlowProfiler()

# Context manager for profiling blocks of code
class profile_block:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        
    def __enter__(self):
        self.start_time = time.time()
        if global_profiler.start_time is not None:
            global_profiler.record_function_call(self.name)
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.start_time and global_profiler.start_time is not None:
            elapsed_time = time.time() - self.start_time
            global_profiler.record_function_time(self.name, elapsed_time)