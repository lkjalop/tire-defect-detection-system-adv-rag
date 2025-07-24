# 🚨 HONEST BUSINESS INTELLIGENCE MODULE
"""
Actual working business intelligence features for tire manufacturing
"""

import json
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List
import streamlit as st

class TireManufacturingBI:
    """Real business intelligence for tire manufacturing"""
    
    def __init__(self):
        self.data_path = Path("data/reports")
        self.data_path.mkdir(parents=True, exist_ok=True)
        
    def generate_kpi_dashboard(self) -> Dict:
        """Generate actual KPIs from CV test data"""
        try:
            # Load actual CV test results
            cv_report_path = self.data_path / "cv_test_report.json"
            
            if cv_report_path.exists():
                with open(cv_report_path, 'r') as f:
                    cv_data = json.load(f)
                
                kpis = {
                    "performance_metrics": {
                        "inference_speed_ms": cv_data.get("performance_metrics", {}).get("average_inference_time", 0) * 1000,
                        "fps": cv_data.get("performance_metrics", {}).get("fps", 0),
                        "meets_requirements": cv_data.get("performance_metrics", {}).get("meets_100ms_requirement", False)
                    },
                    "quality_metrics": {
                        "sensitivity": cv_data.get("accuracy_results", {}).get("sensitivity", 0),
                        "specificity": cv_data.get("accuracy_results", {}).get("specificity", 0),
                        "total_tests": cv_data.get("accuracy_results", {}).get("total_tests", 0)
                    },
                    "system_health": {
                        "last_updated": cv_data.get("timestamp", "Unknown"),
                        "test_status": cv_data.get("test_status", "unknown")
                    }
                }
                
                return kpis
            else:
                return {"error": "No CV test data available"}
                
        except Exception as e:
            return {"error": f"Failed to generate KPIs: {e}"}
    
    def create_performance_chart(self) -> str:
        """Create actual performance visualization"""
        try:
            kpis = self.generate_kpi_dashboard()
            
            if "error" in kpis:
                return kpis["error"]
            
            # Create FPS chart
            fig = go.Figure()
            
            current_fps = kpis["performance_metrics"]["fps"]
            target_fps = 100  # Target: 100 FPS (10ms per frame)
            
            fig.add_trace(go.Indicator(
                mode = "gauge+number+delta",
                value = current_fps,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Inference Speed (FPS)"},
                delta = {'reference': target_fps},
                gauge = {
                    'axis': {'range': [None, 1000]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [0, 100], 'color': "lightgray"},
                        {'range': [100, 500], 'color': "gray"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': target_fps
                    }
                }
            ))
            
            # Save chart
            chart_path = self.data_path / "performance_chart.html"
            fig.write_html(str(chart_path))
            
            return f"Chart saved to {chart_path}"
            
        except Exception as e:
            return f"Failed to create chart: {e}"
    
    def generate_daily_report(self) -> Dict:
        """Generate actual daily manufacturing report"""
        try:
            kpis = self.generate_kpi_dashboard()
            
            if "error" in kpis:
                return kpis
            
            report = {
                "report_date": datetime.now().isoformat(),
                "executive_summary": {
                    "system_performance": "OPERATIONAL" if kpis["performance_metrics"]["meets_requirements"] else "DEGRADED",
                    "quality_score": round((kpis["quality_metrics"]["sensitivity"] + kpis["quality_metrics"]["specificity"]) / 2 * 100, 1),
                    "processing_speed": f"{kpis['performance_metrics']['fps']:.1f} FPS"
                },
                "detailed_metrics": kpis,
                "recommendations": self._generate_recommendations(kpis)
            }
            
            # Save report
            report_path = self.data_path / f"daily_report_{datetime.now().strftime('%Y%m%d')}.json"
            with open(report_path, 'w') as f:
                json.dump(report, f, indent=2)
            
            return report
            
        except Exception as e:
            return {"error": f"Failed to generate report: {e}"}
    
    def _generate_recommendations(self, kpis: Dict) -> List[str]:
        """Generate recommendations based on actual data"""
        recommendations = []
        
        fps = kpis["performance_metrics"]["fps"]
        sensitivity = kpis["quality_metrics"]["sensitivity"]
        specificity = kpis["quality_metrics"]["specificity"]
        
        if fps < 100:
            recommendations.append("Consider hardware upgrade - FPS below target")
        elif fps > 500:
            recommendations.append("Excellent performance - system running optimally")
        
        if sensitivity < 0.9:
            recommendations.append("Improve defect detection sensitivity - may miss defects")
        
        if specificity < 0.9:
            recommendations.append("Reduce false positives - too many good tires flagged as defective")
        
        if not recommendations:
            recommendations.append("System performing within acceptable parameters")
        
        return recommendations

def create_streamlit_dashboard():
    """Create actual Streamlit dashboard"""
    st.set_page_config(page_title="Tire Manufacturing BI", layout="wide")
    
    st.title("🏭 Tire Manufacturing Business Intelligence")
    st.markdown("**Real-time insights from CV testing system**")
    
    bi = TireManufacturingBI()
    
    # Generate KPIs
    kpis = bi.generate_kpi_dashboard()
    
    if "error" in kpis:
        st.error(f"⚠️ {kpis['error']}")
        st.info("💡 Run CV tests first: `python main.py test`")
        return
    
    # Display KPIs in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        fps = kpis["performance_metrics"]["fps"]
        st.metric("Processing Speed", f"{fps:.1f} FPS", delta=f"{fps-100:.1f}" if fps > 100 else None)
    
    with col2:
        sensitivity = kpis["quality_metrics"]["sensitivity"]
        st.metric("Defect Detection", f"{sensitivity*100:.1f}%", delta=f"{(sensitivity-0.9)*100:.1f}%" if sensitivity != 0 else None)
    
    with col3:
        specificity = kpis["quality_metrics"]["specificity"]
        st.metric("Accuracy", f"{specificity*100:.1f}%", delta=f"{(specificity-0.9)*100:.1f}%" if specificity != 0 else None)
    
    with col4:
        total_tests = kpis["quality_metrics"]["total_tests"]
        st.metric("Total Tests", total_tests)
    
    # Performance chart
    st.subheader("📊 Performance Visualization")
    chart_result = bi.create_performance_chart()
    st.info(chart_result)
    
    # Daily report
    st.subheader("📋 Daily Report")
    report = bi.generate_daily_report()
    
    if "error" not in report:
        st.success(f"✅ System Status: {report['executive_summary']['system_performance']}")
        st.metric("Quality Score", f"{report['executive_summary']['quality_score']}%")
        
        st.subheader("💡 Recommendations")
        for rec in report["recommendations"]:
            st.write(f"• {rec}")
    else:
        st.error(report["error"])

if __name__ == "__main__":
    # Run this as: streamlit run dashboards/business_intelligence.py
    create_streamlit_dashboard()
