import streamlit as st

def set_pwa_config():
    pwa_code = """
        <link rel="manifest" href="/static/manifest.json">
        <script>
            if ('serviceWorker' in navigator) {
                window.addEventListener('load', function() {
                    navigator.serviceWorker.register('/static/sw.js').then(function(registration) {
                        console.log('ServiceWorker registration successful with scope: ', registration.scope);
                    }).catch(function(err) {
                        console.log('ServiceWorker registration failed: ', err);
                    });
                });
            }
        </script>
    """
    st.components.v1.html(pwa_code, height=0)