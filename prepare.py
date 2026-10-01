from pathlib import Path
from urllib.parse import urlsplit
import html
import os
import shutil

public_url = os.environ.get('PUBLIC_URL', '').rstrip('/')
parsed = urlsplit(public_url)
if parsed.scheme != 'https' or not parsed.hostname or parsed.query or parsed.fragment or parsed.username:
    raise SystemExit('PUBLIC_URL must be the HTTPS publishing address, without query or fragment.')
if 'chatgpt' in parsed.hostname.lower() or any(name in parsed.hostname.lower() for name in ('okantasin', 'merve', 'okan')):
    raise SystemExit('Use a neutral account/organization name or neutral custom hostname to preserve address privacy.')
if any(name in parsed.path.lower() for name in ('merve', 'okan')):
    raise SystemExit('Use a neutral repository name to preserve address privacy.')
root = Path(__file__).resolve().parent
out = root / '_site'
shutil.copytree(root / 'site', out, dirs_exist_ok=True)
page = (out / 'index.html').read_text().replace('__PUBLIC_URL__', html.escape(public_url, quote=True))
assert '__PUBLIC_URL__' not in page
assert 'chatgpt.site' not in page
(out / 'index.html').write_text(page)
(out / '.nojekyll').touch()
print('Invitation prepared for', public_url)
