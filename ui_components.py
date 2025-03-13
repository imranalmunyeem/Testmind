import streamlit as st

def sidebar_options():
    """ Sidebar UI for selecting test type and framework. """
    st.sidebar.header("🛠️ Test Case Configuration")

    input_type = st.sidebar.selectbox(
        "🔍 What are you testing?",
        ["DOM Elements", "Raw Text Content", "Code Snippet"],
        help="Choose the type of input that AI should analyze for generating test cases.",
    )

    test_type = st.sidebar.radio(
        "📝 Select Test Case Type:",
        ["Automated Test Cases", "Manual Test Cases"],
        help="Choose whether to generate test cases for automation frameworks or manual testing.",
    )

    test_framework = None
    execution_mode = None

    if test_type == "Automated Test Cases":
        test_framework = st.sidebar.selectbox(
            "🛠️ Select Automation Framework:",
            ["Cypress (JavaScript)", "Selenium (Python)", "Playwright (JavaScript)", "Postman (API Testing)"],
            help="Choose the test automation framework for which test cases should be generated.",
        )

        execution_mode = st.sidebar.radio(
            "🎯 What Do You Want to Do?",
            ["Generate Test Cases", "Generate & Execute Tests"],
            help="Choose whether to just generate test cases or also execute them.",
        )

    debug_mode = st.sidebar.checkbox("🛠 Show Debug Info", help="Enable this to see API responses and errors.")

    return input_type, test_type, test_framework, execution_mode, debug_mode


def display_results(test_cases):
    """ Displays AI-generated test cases in an expandable section with a copy button. """
    st.subheader("✅ AI-Generated Test Cases")

    with st.expander("📜 Click to Expand Test Cases", expanded=True):
        st.code(test_cases, language="markdown")

    st.button("📋 Copy Test Cases", on_click=lambda: st.session_state.update({"copy": test_cases}))
    if "copy" in st.session_state:
        st.toast("✅ Test Cases Copied!")
