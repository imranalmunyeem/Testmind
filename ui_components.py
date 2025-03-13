import streamlit as st

def sidebar_options():
    """ Sidebar UI for selecting test type and framework. """
    with st.sidebar:
        st.markdown("## ⚙️ TestMind Settings")
        st.write("Configure AI-generated test case options.")

        input_type = st.selectbox(
            "🔍 What are you testing?",
            ["DOM Elements", "Raw Text Content", "Code Snippet"],
            help="Choose the type of input AI should analyze for generating test cases."
        )

        test_type = st.radio(
            "📝 Test Case Type",
            ["Automated Test Cases", "Manual Test Cases"],
            help="Choose between automated or manual test cases."
        )

        test_framework = None
        execution_mode = None

        if test_type == "Automated Test Cases":
            test_framework = st.selectbox(
                "🛠️ Select Automation Framework",
                ["Cypress (JavaScript)", "Selenium (Python)", "Playwright (JavaScript)", "Postman (API Testing)"],
                help="Choose the test automation framework for AI-generated test cases."
            )

            execution_mode = st.radio(
                "🎯 Execution Mode",
                ["Generate Test Cases", "Generate & Execute Tests"],
                help="Choose whether to generate test cases or also execute them."
            )

        debug_mode = st.checkbox("🛠 Show Debug Info", help="Enable debugging to see AI response details.")

    return input_type, test_type, test_framework, execution_mode, debug_mode

def display_results(test_cases):
    """ Displays AI-generated test cases in a styled expandable section. """
    st.subheader("✅ AI-Generated Test Cases")

    with st.expander("📜 Click to Expand Test Cases", expanded=True):
        st.code(test_cases, language="markdown")  # Format for better readability

    if st.button("📋 Copy Test Cases", use_container_width=True):
        st.session_state["copy"] = test_cases
        st.toast("✅ Test Cases Copied!")
