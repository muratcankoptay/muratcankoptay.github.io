# Configuration file for the Sphinx documentation builder.

project = "Türk Hukuk Hesaplama Algoritmaları ve 7596 Metodolojisi"
copyright = "2026, Av. Murat Can Koptay (Koptay Hukuk Bürosu)"
author = "Av. Murat Can Koptay"
release = "1.0.0"
version = "1.0.0"

extensions = []

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "tr"

html_theme = "sphinx_rtd_theme"
html_title = "Türk Hukuk Hesaplama & 7596 Metodoloji Dokümantasyonu"
html_show_sourcelink = True
html_theme_options = {
    "navigation_depth": 3,
    "collapse_navigation": False,
}
