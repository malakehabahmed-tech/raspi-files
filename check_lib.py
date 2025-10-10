packages = [
    'numpy', 'pandas', 'matplotlib', 'scipy', 'pywt', 'joblib', 'glob', 'warnings'
]

for pkg in packages:
    try:
        __import__(pkg)
        print(f"[✅] {pkg} is installed")
    except ImportError:
        print(f"[❌] {pkg} is NOT installed")
