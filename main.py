def define_env(env):
    """
    Hook for mkdocs-macros.
    This defines variables and macros that can be used inside Markdown pages.
    """
    # Expose a GitHub base path for building absolute links
    env.variables["github_base"] = "https://github.com/AustralianCancerDataNetwork/onco_nlp_resources/blob/main"
