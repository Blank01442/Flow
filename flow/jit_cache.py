import hashlib
import pickle
import os
from pathlib import Path
import time

class JITCache:
    def __init__(self, cache_dir="cache/jit"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.cache_manifest = self.cache_dir / "manifest.pkl"
        self.manifest = self._load_manifest()
        
    def _load_manifest(self):
        """Load the cache manifest file"""
        if self.cache_manifest.exists():
            try:
                with open(self.cache_manifest, 'rb') as f:
                    return pickle.load(f)
            except:
                return {}
        return {}
        
    def _save_manifest(self):
        """Save the cache manifest file"""
        with open(self.cache_manifest, 'wb') as f:
            pickle.dump(self.manifest, f)
            
    def _get_cache_key(self, code, optimization_level=2):
        """Generate a cache key for the code"""
        key_data = f"{code}_{optimization_level}"
        return hashlib.md5(key_data.encode()).hexdigest()
        
    def get_cached_function(self, code, optimization_level=2):
        """Retrieve a compiled function from cache if available"""
        cache_key = self._get_cache_key(code, optimization_level)
        
        # Check if entry exists in manifest
        if cache_key not in self.manifest:
            return None
            
        cache_entry = self.manifest[cache_key]
        cache_file = self.cache_dir / f"{cache_key}.bin"
        
        # Check if cache file exists and is not expired
        if not cache_file.exists():
            return None
            
        # Check expiration (24 hours)
        if time.time() - cache_entry['timestamp'] > 24 * 60 * 60:
            # Expired, remove from cache
            self.invalidate_cache_entry(cache_key)
            return None
            
        # Load the cached function
        try:
            with open(cache_file, 'rb') as f:
                return pickle.load(f)
        except:
            # Corrupted cache, remove it
            self.invalidate_cache_entry(cache_key)
            return None
            
    def cache_function(self, code, compiled_function, optimization_level=2):
        """Cache a compiled function"""
        cache_key = self._get_cache_key(code, optimization_level)
        cache_file = self.cache_dir / f"{cache_key}.bin"
        
        # Save the compiled function
        try:
            with open(cache_file, 'wb') as f:
                pickle.dump(compiled_function, f)
                
            # Update manifest
            self.manifest[cache_key] = {
                'timestamp': time.time(),
                'code_hash': hashlib.md5(code.encode()).hexdigest(),
                'optimization_level': optimization_level
            }
            self._save_manifest()
            return True
        except:
            return False
            
    def invalidate_cache_entry(self, cache_key):
        """Remove a specific cache entry"""
        if cache_key in self.manifest:
            cache_file = self.cache_dir / f"{cache_key}.bin"
            if cache_file.exists():
                cache_file.unlink()
            del self.manifest[cache_key]
            self._save_manifest()
            
    def clear_cache(self):
        """Clear all cached functions"""
        for file in self.cache_dir.glob("*.bin"):
            file.unlink()
        self.manifest = {}
        self._save_manifest()
        
    def get_cache_stats(self):
        """Get cache statistics"""
        total_size = sum(f.stat().st_size for f in self.cache_dir.glob("*.bin"))
        return {
            'entries': len(self.manifest),
            'total_size_bytes': total_size,
            'total_size_mb': total_size / (1024 * 1024)
        }