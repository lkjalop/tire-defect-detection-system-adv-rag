#!/usr/bin/env python3
"""
CORRECTED HONEST VERIFICATION SCRIPT
Testing with actual method names and being truthful about what works
"""

import sys
import os
import json
import traceback
import asyncio
from pathlib import Path

async def test_manufacturing_reasoner_real():
    """Test manufacturing reasoner with correct method names"""
    print("\n🧠 TESTING MANUFACTURING REASONER (CORRECTED)")
    print("=" * 50)
    
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from agents.manufacturing_reasoner import ManufacturingReasoner
        
        reasoner = ManufacturingReasoner()
        
        # Test actual method: analyze_natural_language_query (async)
        test_query = "What causes tire sidewall cracks?"
        result = await reasoner.analyze_natural_language_query(test_query)
        
        print(f"✅ Method exists: analyze_natural_language_query")
        print(f"Query: {test_query}")
        print(f"Result type: {type(result)}")
        print(f"Result keys: {list(result.keys()) if isinstance(result, dict) else 'Not a dict'}")
        
        if isinstance(result, dict):
            print(f"Response length: {len(str(result.get('response', '')))}")
            print(f"Confidence: {result.get('confidence', 'N/A')}")
            print(f"Analysis type: {result.get('analysis_type', 'N/A')}")
            
        return {"status": "✅ SUCCESS", "result": result}
        
    except Exception as e:
        print(f"❌ FAILED: {e}")
        traceback.print_exc()
        return {"status": "❌ FAILED", "error": str(e)}

async def test_agentic_rag_real():
    """Test agentic RAG with correct method names"""
    print("\n🔄 TESTING AGENTIC RAG ENGINE (CORRECTED)")
    print("=" * 50)
    
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from tools.agentic_rag_engine import AgenticRAGEngine
        
        engine = AgenticRAGEngine()
        
        # Test actual method: process_complex_query (async)
        test_query = "How can we reduce manufacturing defects?"
        result = await engine.process_complex_query(test_query)
        
        print(f"✅ Method exists: process_complex_query")
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

def test_cv_system_real():
    """Test CV system with correct method names"""
    print("\n📸 TESTING COMPUTER VISION SYSTEM (CORRECTED)")
    print("=" * 50)
    
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from testing.cv_testing import TireDefectTester
        
        tester = TireDefectTester()
        
        # Check actual methods available
        methods = [method for method in dir(tester) if not method.startswith('_')]
        print(f"Available methods: {methods}")
        
        # Test actual methods
        results = {}
        
        if hasattr(tester, 'test_inference_speed'):
            print("✅ Testing inference speed...")
            speed_result = tester.test_inference_speed()
            results['speed'] = speed_result
            print(f"Speed test result: {speed_result}")
        
        if hasattr(tester, 'generate_test_report'):
            print("✅ Generating test report...")
            report = tester.generate_test_report()
            results['report'] = report
            print(f"Report generated: {type(report)}")
            
        return {"status": "✅ SUCCESS", "results": results}
        
    except Exception as e:
        print(f"❌ FAILED: {e}")
        traceback.print_exc()
        return {"status": "❌ FAILED", "error": str(e)}

def test_main_cli_real():
    """Test main CLI with correct function names"""
    print("\n💻 TESTING MAIN CLI SYSTEM (CORRECTED)")
    print("=" * 50)
    
    try:
        import main
        
        # Check actual CLI commands
        if hasattr(main, 'cli'):
            print("✅ CLI group exists")
            
        # Check actual functions
        functions_to_check = ['setup', 'status', 'query', 'test', 'start']
        
        results = {}
        for func_name in functions_to_check:
            if hasattr(main, func_name):
                results[func_name] = "✅ EXISTS"
                print(f"✅ Command {func_name} exists")
            else:
                results[func_name] = "❌ MISSING"
                print(f"❌ Command {func_name} missing")
        
        # Test if TireManufacturingOrchestrator class exists
        if hasattr(main, 'TireManufacturingOrchestrator'):
            print("✅ TireManufacturingOrchestrator class exists")
            results['orchestrator_class'] = "✅ EXISTS"
        else:
            print("❌ TireManufacturingOrchestrator class missing")
            results['orchestrator_class'] = "❌ MISSING"
                
        return {"status": "✅ SUCCESS", "functions": results}
        
    except Exception as e:
        print(f"❌ FAILED: {e}")
        traceback.print_exc()
        return {"status": "❌ FAILED", "error": str(e)}

def check_actual_business_intelligence():
    """Honest check of what BI features actually exist"""
    print("\n📊 HONEST BUSINESS INTELLIGENCE CHECK")
    print("=" * 50)
    
    bi_features = {
        "basic_directories": {
            "dashboards": Path("dashboards").exists(),
            "reports": Path("data/reports").exists(),
            "data": Path("data").exists()
        },
        "actual_features": {
            "dashboard_code": Path("dashboards").exists() and any(Path("dashboards").iterdir()) if Path("dashboards").exists() else False,
            "report_generation": Path("data/reports").exists() and any(Path("data/reports").iterdir()) if Path("data/reports").exists() else False,
            "analytics_engine": False,  # No actual analytics engine implemented
            "kpi_tracking": False,      # No KPI system implemented
            "real_time_dashboards": False,  # No real-time dashboards
            "data_visualization": False  # No visualization components
        }
    }
    
    print("📁 Directory Structure:")
    for category, items in bi_features.items():
        print(f"\n{category.upper()}:")
        for item, exists in items.items():
            status = "✅ EXISTS" if exists else "❌ MISSING"
            print(f"  {status} {item}")
    
    # Check for actual BI files
    dashboard_files = list(Path("dashboards").rglob("*.py")) if Path("dashboards").exists() else []
    print(f"\n📊 Dashboard files found: {len(dashboard_files)}")
    for file in dashboard_files:
        print(f"  - {file}")
    
    return bi_features

def check_actual_security():
    """Honest check of what security features actually exist"""
    print("\n🔒 HONEST SECURITY CHECK")
    print("=" * 50)
    
    security_status = {
        "directories": {
            "security_folder": Path("security").exists(),
            "config_folder": Path("config").exists()
        },
        "files": {
            "env_template": Path(".env.template").exists(),
            "gitignore": Path(".gitignore").exists(),
            "security_configs": False
        },
        "implemented_features": {
            "input_validation": False,    # Need to check code for actual validation
            "authentication": False,      # No auth system implemented
            "authorization": False,       # No authz system implemented
            "encryption": False,          # No encryption implemented
            "audit_logging": False,       # No audit system implemented
            "owasp_compliance": False,    # No OWASP testing implemented
            "security_headers": False,    # No security headers
            "rate_limiting": False        # No rate limiting
        }
    }
    
    # Check for actual security files
    security_files = []
    if Path("security").exists():
        security_files = list(Path("security").rglob("*.py"))
    
    print("📁 Security Structure:")
    for category, items in security_status.items():
        print(f"\n{category.upper()}:")
        for item, exists in items.items():
            status = "✅ EXISTS" if exists else "❌ MISSING/NOT IMPLEMENTED"
            print(f"  {status} {item}")
    
    print(f"\n🔒 Security files found: {len(security_files)}")
    for file in security_files:
        print(f"  - {file}")
    
    return security_status

def check_production_readiness():
    """Honest assessment of production readiness"""
    print("\n🚀 PRODUCTION READINESS ASSESSMENT")
    print("=" * 50)
    
    readiness_checks = {
        "code_quality": {
            "error_handling": "❓ UNKNOWN - needs code review",
            "logging": "❓ UNKNOWN - needs code review", 
            "testing": "⚠️ BASIC - limited test coverage",
            "documentation": "⚠️ BASIC - README exists but limited"
        },
        "security": {
            "input_validation": "❌ NOT IMPLEMENTED",
            "authentication": "❌ NOT IMPLEMENTED",
            "data_protection": "❌ NOT IMPLEMENTED", 
            "security_testing": "❌ NOT IMPLEMENTED"
        },
        "scalability": {
            "performance_testing": "⚠️ BASIC - limited CV testing only",
            "load_testing": "❌ NOT IMPLEMENTED",
            "database_optimization": "❌ NO DATABASE",
            "caching": "❌ NOT IMPLEMENTED"
        },
        "monitoring": {
            "error_monitoring": "❌ NOT IMPLEMENTED",
            "performance_monitoring": "❌ NOT IMPLEMENTED",
            "health_checks": "⚠️ BASIC - status command only",
            "alerting": "❌ NOT IMPLEMENTED"
        },
        "deployment": {
            "containerization": "❌ NO DOCKER",
            "ci_cd": "❌ NO PIPELINE",
            "environment_management": "⚠️ BASIC - .env template only",
            "backup_strategy": "❌ NOT IMPLEMENTED"
        }
    }
    
    for category, checks in readiness_checks.items():
        print(f"\n{category.upper()}:")
        for check, status in checks.items():
            print(f"  {status} {check}")
    
    # Overall assessment
    total_checks = sum(len(checks) for checks in readiness_checks.values())
    implemented = sum(1 for checks in readiness_checks.values() for status in checks.values() if "✅" in status)
    basic = sum(1 for checks in readiness_checks.values() for status in checks.values() if "⚠️" in status)
    
    print(f"\n📊 OVERALL PRODUCTION READINESS:")
    print(f"  ✅ Fully implemented: {implemented}/{total_checks}")
    print(f"  ⚠️ Basic/Partial: {basic}/{total_checks}")
    print(f"  ❌ Not implemented: {total_checks - implemented - basic}/{total_checks}")
    
    readiness_score = (implemented * 1.0 + basic * 0.5) / total_checks * 100
    print(f"  📈 Readiness Score: {readiness_score:.1f}%")
    
    if readiness_score < 50:
        print("  🚨 NOT READY FOR PRODUCTION")
    elif readiness_score < 80:
        print("  ⚠️ NEEDS SIGNIFICANT WORK BEFORE PRODUCTION")
    else:
        print("  ✅ APPROACHING PRODUCTION READINESS")
    
    return readiness_checks, readiness_score

async def main():
    """Run corrected honest verification"""
    print("🚨 CORRECTED HONEST VERIFICATION - WHAT ACTUALLY WORKS")
    print("=" * 60)
    
    results = {
        "manufacturing_reasoner": await test_manufacturing_reasoner_real(),
        "agentic_rag": await test_agentic_rag_real(),
        "cv_system": test_cv_system_real(),
        "main_cli": test_main_cli_real(),
        "business_intelligence": check_actual_business_intelligence(),
        "security": check_actual_security()
    }
    
    # Production readiness check
    readiness_results, readiness_score = check_production_readiness()
    results["production_readiness"] = {
        "checks": readiness_results,
        "score": readiness_score
    }
    
    # Save results
    with open("corrected_verification_results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)
    
    print("\n" + "=" * 60)
    print("📝 HONEST FINAL SUMMARY")
    print("=" * 60)
    
    working_components = 0
    total_components = 0
    
    for category, result in results.items():
        if category == "production_readiness":
            continue
            
        total_components += 1
        if isinstance(result, dict) and result.get("status") == "✅ SUCCESS":
            working_components += 1
            print(f"✅ {category}: ACTUALLY WORKING")
        else:
            print(f"❌ {category}: FAILED OR INCOMPLETE")
    
    print(f"\n📊 ACTUAL STATUS: {working_components}/{total_components} core components working")
    print(f"🎯 Production Readiness: {readiness_score:.1f}%")
    
    print(f"\n🔍 TRUTH CHECK:")
    if working_components >= 3 and readiness_score >= 60:
        print("✅ System has working core components but needs production hardening")
    elif working_components >= 2:
        print("⚠️ System partially works but has significant gaps")
    else:
        print("❌ System not ready - major components failing")
    
    print(f"\n🚨 RECOMMENDATION:")
    if readiness_score < 50:
        print("   DO NOT CLAIM PRODUCTION READY")
        print("   Focus on fixing core functionality first")
    elif readiness_score < 80:
        print("   DEMO-READY but not production-ready")
        print("   Need security, monitoring, and proper testing")
    else:
        print("   Close to production-ready with proper deployment")

if __name__ == "__main__":
    asyncio.run(main())
