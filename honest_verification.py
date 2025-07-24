#!/usr/bin/env python3
"""
HONEST VERIFICATION SCRIPT
Testing what actually works vs what we claimed
"""

import sys
import os
import json
import traceback
from pathlib import Path

def test_imports():
    """Test if our claimed imports actually work"""
    print("🔍 TESTING IMPORTS")
    print("=" * 50)
    
    import_tests = {
        "Standard Library": ["json", "os", "sys", "pathlib", "asyncio"],
        "Installed Packages": ["click", "rich", "torch", "pandas"],
        "Our Components": []
    }
    
    results = {}
    
    # Test standard library
    for category, packages in import_tests.items():
        results[category] = {}
        for package in packages:
            try:
                __import__(package)
                results[category][package] = "✅ SUCCESS"
                print(f"✅ {package}")
            except ImportError as e:
                results[category][package] = f"❌ FAILED: {e}"
                print(f"❌ {package}: {e}")
    
    # Test our actual components
    component_paths = [
        "agents.manufacturing_reasoner",
        "tools.agentic_rag_engine", 
        "testing.cv_testing"
    ]
    
    results["Our Components"] = {}
    for component in component_paths:
        try:
            # Add current directory to path
            sys.path.insert(0, str(Path(__file__).parent))
            module = __import__(component, fromlist=[''])
            results["Our Components"][component] = "✅ SUCCESS"
            print(f"✅ {component}")
        except Exception as e:
            results["Our Components"][component] = f"❌ FAILED: {e}"
            print(f"❌ {component}: {e}")
    
    return results

def test_manufacturing_reasoner():
    """Test if manufacturing reasoner actually works"""
    print("\n🧠 TESTING MANUFACTURING REASONER")
    print("=" * 50)
    
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from agents.manufacturing_reasoner import ManufacturingReasoner
        
        reasoner = ManufacturingReasoner()
        
        # Test actual query
        test_query = "What causes tire sidewall cracks?"
        result = reasoner.analyze_query(test_query)
        
        print(f"Query: {test_query}")
        print(f"Result type: {type(result)}")
        print(f"Result keys: {list(result.keys()) if isinstance(result, dict) else 'Not a dict'}")
        
        if isinstance(result, dict):
            print(f"Response length: {len(str(result.get('response', '')))}")
            print(f"Confidence: {result.get('confidence', 'N/A')}")
            print(f"Query type: {result.get('query_type', 'N/A')}")
            
        return {"status": "✅ SUCCESS", "result": result}
        
    except Exception as e:
        print(f"❌ FAILED: {e}")
        traceback.print_exc()
        return {"status": "❌ FAILED", "error": str(e)}

def test_agentic_rag():
    """Test if agentic RAG actually works"""
    print("\n🔄 TESTING AGENTIC RAG ENGINE")
    print("=" * 50)
    
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from tools.agentic_rag_engine import AgenticRAGEngine
        
        engine = AgenticRAGEngine()
        
        # Test actual query
        test_query = "How can we reduce manufacturing defects?"
        result = engine.process_query(test_query)
        
        print(f"Query: {test_query}")
        print(f"Result type: {type(result)}")
        print(f"Result keys: {list(result.keys()) if isinstance(result, dict) else 'Not a dict'}")
        
        if isinstance(result, dict):
            print(f"Response length: {len(str(result.get('response', '')))}")
            print(f"Confidence: {result.get('confidence', 'N/A')}")
            print(f"Steps: {len(result.get('reasoning_steps', []))}")
            
        return {"status": "✅ SUCCESS", "result": result}
        
    except Exception as e:
        print(f"❌ FAILED: {e}")
        traceback.print_exc()
        return {"status": "❌ FAILED", "error": str(e)}

def test_cv_system():
    """Test if CV testing actually works"""
    print("\n📸 TESTING COMPUTER VISION SYSTEM")
    print("=" * 50)
    
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from testing.cv_testing import TireDefectTester
        
        tester = TireDefectTester()
        
        # Test performance
        performance = tester.test_performance()
        print(f"Performance test result: {performance}")
        
        # Test accuracy 
        accuracy = tester.test_accuracy()
        print(f"Accuracy test result: {accuracy}")
        
        return {"status": "✅ SUCCESS", "performance": performance, "accuracy": accuracy}
        
    except Exception as e:
        print(f"❌ FAILED: {e}")
        traceback.print_exc()
        return {"status": "❌ FAILED", "error": str(e)}

def test_main_cli():
    """Test if main CLI actually works"""
    print("\n💻 TESTING MAIN CLI SYSTEM")
    print("=" * 50)
    
    try:
        # Test importing main
        import main
        
        # Check if key functions exist
        functions_to_check = ['setup', 'status', 'query_cmd', 'test_cmd']
        
        results = {}
        for func_name in functions_to_check:
            if hasattr(main, func_name):
                results[func_name] = "✅ EXISTS"
                print(f"✅ Function {func_name} exists")
            else:
                results[func_name] = "❌ MISSING"
                print(f"❌ Function {func_name} missing")
                
        return {"status": "✅ SUCCESS", "functions": results}
        
    except Exception as e:
        print(f"❌ FAILED: {e}")
        traceback.print_exc()
        return {"status": "❌ FAILED", "error": str(e)}

def check_business_intelligence():
    """Check what business intelligence features we actually have"""
    print("\n📊 CHECKING BUSINESS INTELLIGENCE FEATURES")
    print("=" * 50)
    
    # Check for BI components
    bi_features = {
        "dashboards": Path("dashboards").exists(),
        "reports": Path("data/reports").exists(),
        "analytics": False,  # We need to implement this
        "kpis": False,       # We need to implement this
        "real_time_monitoring": False  # We need to implement this
    }
    
    for feature, exists in bi_features.items():
        status = "✅ EXISTS" if exists else "❌ MISSING"
        print(f"{status} {feature}")
    
    return bi_features

def check_security_features():
    """Check what security features we actually have"""
    print("\n🔒 CHECKING SECURITY FEATURES")
    print("=" * 50)
    
    security_features = {
        "owasp_compliance": False,    # Need to implement
        "authentication": False,      # Need to implement  
        "input_validation": False,    # Need to implement
        "data_encryption": False,     # Need to implement
        "audit_logging": False,       # Need to implement
        "security_testing": False     # Need to implement
    }
    
    for feature, exists in security_features.items():
        status = "✅ EXISTS" if exists else "❌ MISSING"
        print(f"{status} {feature}")
        
    return security_features

def main():
    """Run honest verification"""
    print("🚨 HONEST VERIFICATION - WHAT ACTUALLY WORKS")
    print("=" * 60)
    
    results = {
        "imports": test_imports(),
        "manufacturing_reasoner": test_manufacturing_reasoner(),
        "agentic_rag": test_agentic_rag(),
        "cv_system": test_cv_system(),
        "main_cli": test_main_cli(),
        "business_intelligence": check_business_intelligence(),
        "security": check_security_features()
    }
    
    # Save results
    with open("honest_verification_results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)
    
    print("\n" + "=" * 60)
    print("📝 HONEST SUMMARY")
    print("=" * 60)
    
    total_tests = 0
    passed_tests = 0
    
    for category, result in results.items():
        if isinstance(result, dict) and "status" in result:
            total_tests += 1
            if "SUCCESS" in result["status"]:
                passed_tests += 1
                print(f"✅ {category}: WORKING")
            else:
                print(f"❌ {category}: FAILED")
        else:
            print(f"⚠️  {category}: NEEDS REVIEW")
    
    print(f"\nOVERALL: {passed_tests}/{total_tests} components actually working")
    
    if passed_tests < total_tests:
        print("⚠️  SYSTEM NOT READY FOR PRODUCTION")
        print("🔧 FIXES NEEDED BEFORE CLAIMING IT WORKS")
    else:
        print("✅ SYSTEM APPEARS TO BE WORKING")

if __name__ == "__main__":
    main()
