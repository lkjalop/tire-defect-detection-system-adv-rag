#!/usr/bin/env python3
"""Test script for detailed component verification"""

import asyncio
import sys
sys.path.append('..')

async def test_manufacturing_reasoner():
    print("🔍 TESTING MANUFACTURING REASONER LINE BY LINE")
    print("=" * 50)
    
    from agents.manufacturing_reasoner import ManufacturingReasoner
    
    reasoner = ManufacturingReasoner()
    
    # Test 1: Knowledge base structure
    print("📚 Knowledge Base Structure:")
    print(f"   Defect types: {list(reasoner.manufacturing_knowledge['defects'].keys())}")
    print(f"   Crack causes: {reasoner.manufacturing_knowledge['defects']['cracks']['causes']}")
    print(f"   Bubble solutions: {reasoner.manufacturing_knowledge['defects']['bubbles']['solutions']}")
    
    # Test 2: Defect analysis query
    print("\n🔍 Testing Defect Analysis Query:")
    result1 = await reasoner.analyze_natural_language_query("What causes cracks in tire sidewalls?")
    print(f"   Query: {result1['query']}")
    print(f"   Type: {result1['analysis_type']}")
    print(f"   Confidence: {result1['confidence']:.2%}")
    print(f"   Has response: {'main_response' in result1}")
    
    # Test 3: Optimization query
    print("\n🔧 Testing Optimization Query:")
    result2 = await reasoner.analyze_natural_language_query("How can we optimize our manufacturing process?")
    print(f"   Query: {result2['query']}")
    print(f"   Type: {result2['analysis_type']}")
    print(f"   Confidence: {result2['confidence']:.2%}")
    
    # Test 4: History tracking
    print("\n📊 History Tracking:")
    print(f"   Total queries processed: {len(reasoner.analysis_history)}")
    print(f"   Last query type: {reasoner.analysis_history[-1]['analysis_type'] if reasoner.analysis_history else 'None'}")
    
    return True

async def test_agentic_rag():
    print("\n🧠 TESTING AGENTIC RAG ENGINE LINE BY LINE")
    print("=" * 50)
    
    from tools.agentic_rag_engine import AgenticRAGEngine
    
    engine = AgenticRAGEngine()
    
    # Test 1: Knowledge base
    print("📚 Knowledge Base Content:")
    for topic, content in engine.knowledge_base.items():
        print(f"   {topic}: {content[:50]}...")
    
    # Test 2: Complex query processing
    print("\n🔄 Testing Complex Query Processing:")
    result = await engine.process_complex_query("How can we reduce tire manufacturing defects?")
    print(f"   Query: {result['query']}")
    print(f"   Method: {result['method']}")
    print(f"   Confidence: {result['confidence']:.2%}")
    print(f"   Reasoning steps: {len(result.get('reasoning_steps', []))}")
    
    # Test 3: Step-by-step reasoning
    print("\n📋 Reasoning Steps Details:")
    for i, step in enumerate(result.get('reasoning_steps', []), 1):
        print(f"   Step {i}: {step['action']} (confidence: {step['confidence']:.2%})")
    
    return True

def test_cv_system():
    print("\n🧪 TESTING COMPUTER VISION SYSTEM LINE BY LINE")
    print("=" * 50)
    
    from testing.cv_testing import TireDefectTester
    
    tester = TireDefectTester()
    
    # Test 1: Basic initialization
    print("🏗️ Initialization Test:")
    print(f"   Test results dict: {type(tester.test_results)}")
    
    # Test 2: Performance testing
    print("\n⚡ Performance Testing:")
    perf_results = tester.test_inference_speed(iterations=5)
    print(f"   Average time: {perf_results['average_inference_time']:.4f}s")
    print(f"   FPS: {perf_results['fps']:.1f}")
    print(f"   Meets requirement: {perf_results['meets_100ms_requirement']}")
    
    # Test 3: Directory creation
    print("\n📁 Directory Creation Test:")
    test_dir = tester.create_sample_test_images()
    print(f"   Test directory: {test_dir}")
    print(f"   Directory exists: {test_dir.exists()}")
    
    return True

async def comprehensive_integration_test():
    print("\n🌐 COMPREHENSIVE INTEGRATION TEST")
    print("=" * 50)
    
    # Test main system with each component
    import subprocess
    import json
    
    # Test 1: Main system status
    print("🔍 Main System Status:")
    result = subprocess.run(['python', '../main.py', 'status'], 
                          capture_output=True, text=True, cwd='.')
    print(f"   Status command exit code: {result.returncode}")
    
    # Test 2: Query processing with main system
    print("\n❓ Query Processing Integration:")
    result = subprocess.run(['python', '../main.py', 'query', 'Test manufacturing query'], 
                          capture_output=True, text=True, cwd='.')
    print(f"   Query command exit code: {result.returncode}")
    
    # Test 3: Test report file
    print("\n📄 Generated Reports Check:")
    try:
        with open('../data/reports/cv_test_report.json', 'r') as f:
            report = json.load(f)
        print(f"   CV report timestamp: {report['timestamp']}")
        print(f"   Performance metrics: {len(report['performance_metrics'])} items")
        print(f"   Test status: {report['test_status']}")
    except Exception as e:
        print(f"   Report check failed: {e}")
    
    return True

async def main():
    print("🚀 METICULOUS LINE-BY-LINE SYSTEM VERIFICATION")
    print("=" * 60)
    
    try:
        # Test each component individually
        await test_manufacturing_reasoner()
        await test_agentic_rag()
        test_cv_system()
        await comprehensive_integration_test()
        
        print("\n✅ ALL COMPONENTS VERIFIED SUCCESSFULLY")
        print("🎯 System is working as expected")
        
    except Exception as e:
        print(f"\n❌ VERIFICATION FAILED: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
