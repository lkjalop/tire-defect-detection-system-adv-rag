# 🔒 BASIC SECURITY MODULE
"""
Essential security features for tire manufacturing system
(Not production-ready but demonstrates security concepts)
"""

import hashlib
import secrets
import time
import logging
from functools import wraps
from typing import Dict, Optional, List
from pathlib import Path
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
security_logger = logging.getLogger("security")

class BasicSecurityManager:
    """Basic security features - NOT production ready"""
    
    def __init__(self):
        self.failed_attempts = {}
        self.blocked_ips = set()
        self.session_tokens = {}
        self.audit_log = []
        
    def validate_input(self, input_text: str, max_length: int = 1000) -> bool:
        """Basic input validation"""
        if not input_text:
            return False
        
        if len(input_text) > max_length:
            self.log_security_event("input_too_long", {"length": len(input_text)})
            return False
        
        # Check for potential injection attempts
        dangerous_patterns = [
            "';", "--", "/*", "*/", "xp_", "sp_", "drop table", 
            "delete from", "insert into", "update set", "<script",
            "javascript:", "onload=", "onerror="
        ]
        
        input_lower = input_text.lower()
        for pattern in dangerous_patterns:
            if pattern in input_lower:
                self.log_security_event("potential_injection", {"pattern": pattern})
                return False
        
        return True
    
    def rate_limit(self, identifier: str, max_attempts: int = 10, time_window: int = 300):
        """Basic rate limiting"""
        current_time = time.time()
        
        if identifier in self.failed_attempts:
            attempts = self.failed_attempts[identifier]
            # Remove old attempts outside time window
            attempts = [t for t in attempts if current_time - t < time_window]
            self.failed_attempts[identifier] = attempts
            
            if len(attempts) >= max_attempts:
                self.blocked_ips.add(identifier)
                self.log_security_event("rate_limit_exceeded", {"identifier": identifier})
                return False
        
        return True
    
    def generate_session_token(self, user_id: str) -> str:
        """Generate basic session token"""
        token = secrets.token_urlsafe(32)
        self.session_tokens[token] = {
            "user_id": user_id,
            "created": time.time(),
            "expires": time.time() + 3600  # 1 hour
        }
        return token
    
    def validate_session(self, token: str) -> Optional[str]:
        """Validate session token"""
        if token not in self.session_tokens:
            return None
        
        session = self.session_tokens[token]
        if time.time() > session["expires"]:
            del self.session_tokens[token]
            return None
        
        return session["user_id"]
    
    def log_security_event(self, event_type: str, details: Dict):
        """Log security events"""
        event = {
            "timestamp": time.time(),
            "event_type": event_type,
            "details": details
        }
        self.audit_log.append(event)
        security_logger.warning(f"Security event: {event_type} - {details}")
        
        # Save to file
        log_path = Path("data/logs/security.json")
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(log_path, "a") as f:
            f.write(json.dumps(event) + "\n")
    
    def get_security_report(self) -> Dict:
        """Generate security status report"""
        current_time = time.time()
        recent_events = [e for e in self.audit_log if current_time - e["timestamp"] < 86400]  # Last 24h
        
        return {
            "blocked_ips": len(self.blocked_ips),
            "active_sessions": len(self.session_tokens),
            "recent_security_events": len(recent_events),
            "event_types": list(set(e["event_type"] for e in recent_events)),
            "last_24h_events": recent_events[-10:]  # Last 10 events
        }

# Global security manager instance
security_manager = BasicSecurityManager()

def require_valid_input(max_length: int = 1000):
    """Decorator for input validation"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check string arguments
            for arg in args:
                if isinstance(arg, str) and not security_manager.validate_input(arg, max_length):
                    raise ValueError("Invalid input detected")
            
            for key, value in kwargs.items():
                if isinstance(value, str) and not security_manager.validate_input(value, max_length):
                    raise ValueError(f"Invalid input in {key}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def rate_limited(max_attempts: int = 10):
    """Decorator for rate limiting"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Simple rate limiting by function name
            func_name = func.__name__
            if not security_manager.rate_limit(func_name, max_attempts):
                raise Exception("Rate limit exceeded")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def secure_hash(data: str) -> str:
    """Generate secure hash"""
    return hashlib.sha256(data.encode()).hexdigest()

def check_owasp_basics():
    """Basic OWASP Top 10 checklist"""
    checks = {
        "A01_Broken_Access_Control": {
            "status": "⚠️ BASIC",
            "notes": "Basic session management implemented"
        },
        "A02_Cryptographic_Failures": {
            "status": "❌ NOT IMPLEMENTED", 
            "notes": "No encryption for sensitive data"
        },
        "A03_Injection": {
            "status": "⚠️ BASIC",
            "notes": "Basic input validation implemented"
        },
        "A04_Insecure_Design": {
            "status": "❌ NOT IMPLEMENTED",
            "notes": "No security by design principles"
        },
        "A05_Security_Misconfiguration": {
            "status": "❌ NOT IMPLEMENTED",
            "notes": "No security configuration management"
        },
        "A06_Vulnerable_Components": {
            "status": "❌ NOT IMPLEMENTED",
            "notes": "No dependency scanning"
        },
        "A07_Authentication_Failures": {
            "status": "❌ NOT IMPLEMENTED",
            "notes": "No proper authentication system"
        },
        "A08_Software_Integrity_Failures": {
            "status": "❌ NOT IMPLEMENTED",
            "notes": "No integrity checks"
        },
        "A09_Logging_Failures": {
            "status": "⚠️ BASIC",
            "notes": "Basic security logging implemented"
        },
        "A10_Server_Side_Request_Forgery": {
            "status": "❌ NOT IMPLEMENTED",
            "notes": "No SSRF protection"
        }
    }
    
    return checks

def generate_security_report():
    """Generate comprehensive security report"""
    print("🔒 BASIC SECURITY STATUS REPORT")
    print("=" * 50)
    print("⚠️ WARNING: This is a BASIC implementation, NOT production-ready")
    print()
    
    # Current security status
    status = security_manager.get_security_report()
    print("📊 Current Status:")
    print(f"  Blocked IPs: {status['blocked_ips']}")
    print(f"  Active Sessions: {status['active_sessions']}")
    print(f"  Recent Events: {status['recent_security_events']}")
    print(f"  Event Types: {', '.join(status['event_types']) if status['event_types'] else 'None'}")
    
    print("\n🔍 OWASP Top 10 Check:")
    owasp_checks = check_owasp_basics()
    
    implemented = sum(1 for check in owasp_checks.values() if "BASIC" in check["status"])
    total = len(owasp_checks)
    
    for item, check in owasp_checks.items():
        print(f"  {check['status']} {item}: {check['notes']}")
    
    print(f"\n📈 Security Score: {implemented}/{total} partially implemented")
    
    if implemented < 3:
        print("🚨 CRITICAL: Major security gaps - NOT suitable for production")
    elif implemented < 7:
        print("⚠️ WARNING: Significant security improvements needed")
    else:
        print("✅ GOOD: Basic security measures in place")
    
    return status, owasp_checks

if __name__ == "__main__":
    # Demo the security features
    generate_security_report()
    
    # Test input validation
    print("\n🧪 Testing Security Features:")
    
    @require_valid_input()
    @rate_limited(max_attempts=3)
    def test_secure_function(query: str):
        return f"Processed: {query}"
    
    # Test valid input
    try:
        result = test_secure_function("What causes tire defects?")
        print(f"✅ Valid input: {result}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test invalid input
    try:
        result = test_secure_function("'; DROP TABLE users; --")
        print(f"❌ Should not see this: {result}")
    except Exception as e:
        print(f"✅ Blocked malicious input: {e}")
    
    # Test rate limiting
    print("\n🚦 Testing rate limiting:")
    for i in range(5):
        try:
            result = test_secure_function(f"Query {i}")
            print(f"✅ Query {i}: Success")
        except Exception as e:
            print(f"❌ Query {i}: {e}")
    
    print("\n📄 Final security report:")
    generate_security_report()
